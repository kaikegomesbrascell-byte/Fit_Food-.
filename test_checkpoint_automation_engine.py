"""
Checkpoint Test - Task 5: Testar Automation Engine isoladamente

Este script valida:
- Extração de dados de 50 leads (mínimo permitido pelo sistema)
- Verificação de dados extraídos corretamente
- Validação de delays e comportamento anti-bot
- Funcionamento completo do motor de automação
"""

import asyncio
import threading
import time
from datetime import datetime
from typing import List, Dict
from automation_engine import GoogleMapsAutomation


class TestResults:
    """Classe para armazenar resultados dos testes."""
    
    def __init__(self):
        self.leads_extraidos: List[Dict[str, str]] = []
        self.callbacks_recebidos: int = 0
        self.tempo_inicio: datetime = None
        self.tempo_fim: datetime = None
        self.delays_observados: List[float] = []
        self.erros: List[str] = []
        
    def adicionar_lead(self, lead: Dict[str, str], progresso: float):
        """Adiciona lead extraído aos resultados."""
        self.leads_extraidos.append(lead)
        self.callbacks_recebidos += 1
        # Mostrar apenas a cada 5 leads para não poluir o output
        if len(self.leads_extraidos) % 5 == 0 or len(self.leads_extraidos) <= 3:
            print(f"  ✓ Lead {len(self.leads_extraidos)}: {lead.get('nome', 'N/A')[:50]}")
            print(f"    Progresso: {progresso*100:.1f}%")
    
    def adicionar_erro(self, erro: str):
        """Adiciona erro aos resultados."""
        self.erros.append(erro)
        print(f"  ✗ ERRO: {erro}")
    
    def calcular_tempo_total(self) -> float:
        """Calcula tempo total de execução em segundos."""
        if self.tempo_inicio and self.tempo_fim:
            delta = self.tempo_fim - self.tempo_inicio
            return delta.total_seconds()
        return 0.0


def validar_lead(lead: Dict[str, str]) -> tuple[bool, List[str]]:
    """
    Valida se um lead possui os campos esperados e dados válidos.
    
    Returns:
        Tupla (is_valid, problemas) onde problemas é lista de strings descrevendo issues.
    """
    problemas = []
    
    # Verificar campos obrigatórios
    campos_esperados = ["nome", "telefone", "site", "nota", "comentarios", "endereco"]
    for campo in campos_esperados:
        if campo not in lead:
            problemas.append(f"Campo '{campo}' ausente")
    
    # Verificar se nome não está vazio (campo mais crítico)
    if "nome" in lead:
        nome = lead["nome"].strip()
        if not nome or nome == "N/A":
            problemas.append("Nome está vazio ou N/A")
    
    # Verificar se pelo menos um campo de contato está preenchido
    tem_contato = False
    if "telefone" in lead and lead["telefone"] != "N/A":
        tem_contato = True
    if "site" in lead and lead["site"] != "N/A":
        tem_contato = True
    
    if not tem_contato:
        problemas.append("Nenhum campo de contato (telefone/site) disponível")
    
    return len(problemas) == 0, problemas


async def teste_extracao_basica():
    """
    Teste 1: Extração básica de 50 leads
    Valida se o sistema consegue extrair dados corretamente.
    """
    print("\n" + "=" * 70)
    print("TESTE 1: Extração Básica de 50 Leads")
    print("=" * 70)
    
    results = TestResults()
    automation = GoogleMapsAutomation(headless=False)  # headless=False para visualizar
    stop_flag = threading.Event()
    
    def callback_teste(lead_dict, progresso):
        """Callback para receber atualizações."""
        results.adicionar_lead(lead_dict, progresso)
    
    try:
        # Inicializar navegador
        print("\n[1/4] Inicializando navegador...")
        results.tempo_inicio = datetime.now()
        await automation.inicializar_navegador()
        print("  ✓ Navegador inicializado")
        
        # Executar busca
        print("\n[2/4] Executando busca...")
        print("  Nicho: restaurantes")
        print("  Localização: São Paulo")
        print("  Limite: 50 leads")
        print()
        
        leads = await automation.buscar_empresas(
            nicho="restaurantes",
            localizacao="São Paulo",
            limite=50,
            callback=callback_teste,
            stop_flag=stop_flag
        )
        
        results.tempo_fim = datetime.now()
        
        # Validar resultados
        print("\n[3/4] Validando dados extraídos...")
        leads_validos = 0
        leads_com_problemas = 0
        
        for i, lead in enumerate(leads, 1):
            is_valid, problemas = validar_lead(lead)
            if is_valid:
                leads_validos += 1
            else:
                leads_com_problemas += 1
                if i <= 5:  # Mostrar apenas os primeiros 5 com problemas
                    print(f"  ⚠ Lead {i} com problemas:")
                    for problema in problemas:
                        print(f"    - {problema}")
        
        # Exibir estatísticas
        print("\n[4/4] Estatísticas:")
        print(f"  Total de leads extraídos: {len(leads)}")
        print(f"  Leads válidos: {leads_validos}")
        print(f"  Leads com problemas: {leads_com_problemas}")
        print(f"  Callbacks recebidos: {results.callbacks_recebidos}")
        print(f"  Tempo total: {results.calcular_tempo_total():.2f} segundos")
        
        # Verificar se atingiu o objetivo
        sucesso = len(leads) >= 45 and leads_validos >= 40  # Pelo menos 90% do esperado e 80% válidos
        
        if sucesso:
            print("\n  ✓ TESTE 1 PASSOU: Extração básica funcionando corretamente")
        else:
            print("\n  ✗ TESTE 1 FALHOU:")
            if len(leads) < 45:
                print(f"    - Esperado pelo menos 45 leads, obteve {len(leads)}")
            if leads_validos < 40:
                print(f"    - Esperado pelo menos 40 leads válidos, obteve {leads_validos}")
        
        return sucesso, results
        
    except Exception as e:
        results.adicionar_erro(f"Exceção durante teste: {str(e)}")
        import traceback
        traceback.print_exc()
        return False, results
    
    finally:
        print("\n[Limpeza] Fechando navegador...")
        await automation.fechar_navegador()
        print("  ✓ Navegador fechado")


async def teste_delays_anti_bot():
    """
    Teste 2: Validação de delays e comportamento anti-bot
    Verifica se delays aleatórios estão sendo aplicados.
    """
    print("\n" + "=" * 70)
    print("TESTE 2: Validação de Delays e Comportamento Anti-Bot")
    print("=" * 70)
    
    automation = GoogleMapsAutomation(headless=True)
    
    try:
        print("\n[1/3] Testando delays aleatórios...")
        
        # Testar aplicar_delay_humano múltiplas vezes
        delays = []
        for i in range(5):
            inicio = time.time()
            await automation.aplicar_delay_humano(min_sec=1.0, max_sec=3.0)
            fim = time.time()
            delay = fim - inicio
            delays.append(delay)
            print(f"  Delay {i+1}: {delay:.2f} segundos")
        
        # Validar que delays são diferentes (comportamento aleatório)
        print("\n[2/3] Validando aleatoriedade dos delays...")
        delays_unicos = len(set([round(d, 1) for d in delays]))
        
        if delays_unicos >= 3:
            print(f"  ✓ Delays variados detectados ({delays_unicos} valores únicos)")
            delays_ok = True
        else:
            print(f"  ⚠ Pouca variação nos delays ({delays_unicos} valores únicos)")
            delays_ok = False
        
        # Validar que delays estão no range esperado
        print("\n[3/3] Validando range dos delays (1.0 - 3.0 segundos)...")
        delays_no_range = all(1.0 <= d <= 3.5 for d in delays)  # 3.5 para margem
        
        if delays_no_range:
            print(f"  ✓ Todos os delays no range esperado")
            print(f"    Min: {min(delays):.2f}s, Max: {max(delays):.2f}s, Média: {sum(delays)/len(delays):.2f}s")
        else:
            print(f"  ✗ Alguns delays fora do range")
            print(f"    Min: {min(delays):.2f}s, Max: {max(delays):.2f}s")
        
        sucesso = delays_ok and delays_no_range
        
        if sucesso:
            print("\n  ✓ TESTE 2 PASSOU: Delays anti-bot funcionando corretamente")
        else:
            print("\n  ✗ TESTE 2 FALHOU: Problemas com delays anti-bot")
        
        return sucesso
        
    except Exception as e:
        print(f"\n  ✗ ERRO no teste: {str(e)}")
        import traceback
        traceback.print_exc()
        return False


async def teste_campos_extraidos():
    """
    Teste 3: Verificação detalhada dos campos extraídos
    Valida a qualidade dos dados de cada campo.
    """
    print("\n" + "=" * 70)
    print("TESTE 3: Verificação Detalhada dos Campos Extraídos")
    print("=" * 70)
    
    results = TestResults()
    automation = GoogleMapsAutomation(headless=False)
    stop_flag = threading.Event()
    
    def callback_teste(lead_dict, progresso):
        """Callback para receber atualizações."""
        results.adicionar_lead(lead_dict, progresso)
    
    try:
        print("\n[1/3] Extraindo 50 leads para análise...")
        await automation.inicializar_navegador()
        
        leads = await automation.buscar_empresas(
            nicho="cafeterias",
            localizacao="Rio de Janeiro",
            limite=50,
            callback=callback_teste,
            stop_flag=stop_flag
        )
        
        print("\n[2/3] Analisando qualidade dos campos...")
        
        # Estatísticas por campo
        campos_stats = {
            "nome": {"preenchidos": 0, "vazios": 0},
            "telefone": {"preenchidos": 0, "vazios": 0},
            "site": {"preenchidos": 0, "vazios": 0},
            "nota": {"preenchidos": 0, "vazios": 0},
            "comentarios": {"preenchidos": 0, "vazios": 0},
            "endereco": {"preenchidos": 0, "vazios": 0}
        }
        
        for lead in leads:
            for campo in campos_stats.keys():
                valor = lead.get(campo, "N/A")
                if valor and valor != "N/A" and valor.strip():
                    campos_stats[campo]["preenchidos"] += 1
                else:
                    campos_stats[campo]["vazios"] += 1
        
        print("\n[3/3] Estatísticas por campo:")
        for campo, stats in campos_stats.items():
            total = stats["preenchidos"] + stats["vazios"]
            percentual = (stats["preenchidos"] / total * 100) if total > 0 else 0
            print(f"  {campo.capitalize():12} - Preenchidos: {stats['preenchidos']:2}/{total} ({percentual:.0f}%)")
        
        # Exibir exemplo de lead
        if leads:
            print("\n  Exemplo de lead extraído (primeiro):")
            primeiro = leads[0]
            print(f"    Nome: {primeiro.get('nome', 'N/A')[:50]}")
            print(f"    Telefone: {primeiro.get('telefone', 'N/A')}")
            print(f"    Site: {primeiro.get('site', 'N/A')[:50]}")
            print(f"    Nota: {primeiro.get('nota', 'N/A')}")
            print(f"    Comentários: {primeiro.get('comentarios', 'N/A')}")
            print(f"    Endereço: {primeiro.get('endereco', 'N/A')[:50]}")
        
        # Critério de sucesso: nome deve estar 100% preenchido, outros campos pelo menos 50%
        nome_ok = campos_stats["nome"]["preenchidos"] == len(leads)
        outros_ok = all(
            campos_stats[campo]["preenchidos"] >= len(leads) * 0.5
            for campo in ["telefone", "site", "endereco"]
        )
        
        sucesso = nome_ok and outros_ok
        
        if sucesso:
            print("\n  ✓ TESTE 3 PASSOU: Qualidade dos dados adequada")
        else:
            print("\n  ✗ TESTE 3 FALHOU:")
            if not nome_ok:
                print("    - Campo 'nome' não está 100% preenchido")
            if not outros_ok:
                print("    - Alguns campos têm menos de 50% de preenchimento")
        
        return sucesso
        
    except Exception as e:
        print(f"\n  ✗ ERRO no teste: {str(e)}")
        import traceback
        traceback.print_exc()
        return False
    
    finally:
        await automation.fechar_navegador()


async def executar_todos_testes():
    """Executa todos os testes do checkpoint."""
    print("\n" + "=" * 70)
    print("CHECKPOINT 5: TESTE DO AUTOMATION ENGINE")
    print("=" * 70)
    print("\nEste teste validará:")
    print("  1. Extração de dados de 50 leads")
    print("  2. Delays e comportamento anti-bot")
    print("  3. Qualidade dos campos extraídos")
    print()
    
    resultados = {}
    
    # Teste 1: Extração básica
    sucesso1, results1 = await teste_extracao_basica()
    resultados["teste_1"] = sucesso1
    
    # Teste 2: Delays anti-bot
    sucesso2 = await teste_delays_anti_bot()
    resultados["teste_2"] = sucesso2
    
    # Teste 3: Campos extraídos
    sucesso3 = await teste_campos_extraidos()
    resultados["teste_3"] = sucesso3
    
    # Resumo final
    print("\n" + "=" * 70)
    print("RESUMO DOS TESTES")
    print("=" * 70)
    print(f"\nTeste 1 - Extração Básica:        {'✓ PASSOU' if sucesso1 else '✗ FALHOU'}")
    print(f"Teste 2 - Delays Anti-Bot:        {'✓ PASSOU' if sucesso2 else '✗ FALHOU'}")
    print(f"Teste 3 - Qualidade dos Campos:   {'✓ PASSOU' if sucesso3 else '✗ FALHOU'}")
    
    todos_passaram = all(resultados.values())
    
    print("\n" + "=" * 70)
    if todos_passaram:
        print("✓ CHECKPOINT 5 CONCLUÍDO COM SUCESSO!")
        print("  O Automation Engine está funcionando corretamente.")
    else:
        print("✗ CHECKPOINT 5 FALHOU")
        print("  Alguns testes não passaram. Revise os erros acima.")
    print("=" * 70)
    
    return todos_passaram


def main():
    """Função principal para executar os testes."""
    print("\n🚀 Iniciando Checkpoint 5: Teste do Automation Engine\n")
    
    try:
        sucesso = asyncio.run(executar_todos_testes())
        
        if sucesso:
            print("\n✓ Todos os testes passaram!")
            return 0
        else:
            print("\n✗ Alguns testes falharam. Veja detalhes acima.")
            return 1
            
    except KeyboardInterrupt:
        print("\n\n⚠ Testes interrompidos pelo usuário")
        return 2
    except Exception as e:
        print(f"\n\n✗ Erro fatal durante execução dos testes: {str(e)}")
        import traceback
        traceback.print_exc()
        return 3


if __name__ == "__main__":
    exit(main())
