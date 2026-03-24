"""
Teste para verificar encerramento imediato ao atingir limite de leads.
Valida Requirement 11.4: THE Automation_Engine SHALL encerrar a extração imediatamente quando o limite é atingido.
"""

import asyncio
import threading
from automation_engine import GoogleMapsAutomation


class TestContext:
    """Contexto para rastrear comportamento do teste."""
    def __init__(self):
        self.leads_recebidos = []
        self.callbacks_chamados = 0
        self.processamentos_apos_limite = 0
        

def criar_callback_teste(context: TestContext, limite: int):
    """Cria callback que rastreia chamadas e verifica se processou além do limite."""
    def callback(lead_dict, progresso):
        context.callbacks_chamados += 1
        context.leads_recebidos.append(lead_dict)
        
        # Verificar se está processando além do limite
        if len(context.leads_recebidos) > limite:
            context.processamentos_apos_limite += 1
            print(f"⚠️  AVISO: Processou lead #{len(context.leads_recebidos)} além do limite de {limite}")
        else:
            print(f"✓ Callback {context.callbacks_chamados}: Lead #{len(context.leads_recebidos)}/{limite} - {lead_dict.get('nome', 'N/A')}")
    
    return callback


async def teste_encerramento_imediato():
    """
    Testa se a extração encerra imediatamente ao atingir o limite.
    
    Cenário de teste:
    - Buscar 5 leads (limite pequeno para teste rápido)
    - Verificar que exatamente 5 leads são extraídos
    - Verificar que nenhum processamento adicional ocorre após atingir o limite
    """
    
    print("=" * 70)
    print("TESTE: Encerramento Imediato ao Atingir Limite")
    print("=" * 70)
    print("\nObjetivo: Verificar que a extração para IMEDIATAMENTE ao atingir o limite")
    print("Requirement 11.4: Encerramento imediato quando limite é atingido\n")
    
    # Configurar teste
    LIMITE_TESTE = 50  # Usar limite válido (50, 100 ou 500)
    context = TestContext()
    automation = GoogleMapsAutomation(headless=True)
    stop_flag = threading.Event()
    
    try:
        # Inicializar navegador
        print("[1] Inicializando navegador...")
        await automation.inicializar_navegador()
        print("    ✓ Navegador inicializado\n")
        
        # Executar busca com limite pequeno
        print(f"[2] Executando busca com limite de {LIMITE_TESTE} leads...")
        print("    Nicho: cafeterias")
        print("    Localização: São Paulo")
        print()
        
        leads = await automation.buscar_empresas(
            nicho="cafeterias",
            localizacao="São Paulo",
            limite=LIMITE_TESTE,
            callback=criar_callback_teste(context, LIMITE_TESTE),
            stop_flag=stop_flag
        )
        
        # Validar resultados
        print("\n" + "=" * 70)
        print("[3] RESULTADOS DO TESTE")
        print("=" * 70)
        
        total_leads = len(leads)
        print(f"\n✓ Total de leads extraídos: {total_leads}")
        print(f"✓ Limite configurado: {LIMITE_TESTE}")
        print(f"✓ Callbacks chamados: {context.callbacks_chamados}")
        print(f"✓ Processamentos além do limite: {context.processamentos_apos_limite}")
        
        # Verificações
        print("\n[4] VERIFICAÇÕES:")
        
        sucesso = True
        
        # Verificação 1: Não deve exceder o limite
        if total_leads <= LIMITE_TESTE:
            print(f"    ✓ PASSOU: Total de leads ({total_leads}) não excede o limite ({LIMITE_TESTE})")
        else:
            print(f"    ✗ FALHOU: Total de leads ({total_leads}) excede o limite ({LIMITE_TESTE})")
            sucesso = False
        
        # Verificação 2: Deve extrair exatamente o limite (ou menos se não houver leads suficientes)
        if total_leads == LIMITE_TESTE:
            print(f"    ✓ PASSOU: Extraiu exatamente {LIMITE_TESTE} leads conforme esperado")
        elif total_leads < LIMITE_TESTE:
            print(f"    ⚠️  AVISO: Extraiu apenas {total_leads} leads (pode não haver leads suficientes no Google Maps)")
        else:
            print(f"    ✗ FALHOU: Extraiu mais leads que o limite")
            sucesso = False
        
        # Verificação 3: Não deve processar além do limite
        if context.processamentos_apos_limite == 0:
            print(f"    ✓ PASSOU: Nenhum processamento além do limite detectado")
        else:
            print(f"    ✗ FALHOU: {context.processamentos_apos_limite} processamentos além do limite detectados")
            sucesso = False
        
        # Resultado final
        print("\n" + "=" * 70)
        if sucesso:
            print("✓✓✓ TESTE PASSOU COM SUCESSO ✓✓✓")
            print("\nA otimização de encerramento imediato está funcionando corretamente!")
            print("O sistema para de processar assim que atinge o limite de leads.")
        else:
            print("✗✗✗ TESTE FALHOU ✗✗✗")
            print("\nA otimização precisa de ajustes.")
        print("=" * 70)
        
        return sucesso
        
    except Exception as e:
        print(f"\n✗ ERRO durante o teste: {str(e)}")
        import traceback
        traceback.print_exc()
        return False
    
    finally:
        # Fechar navegador
        print("\n[5] Limpeza...")
        await automation.fechar_navegador()
        print("    ✓ Navegador fechado")


def main():
    """Função principal para executar o teste."""
    print("\n🧪 Iniciando teste de encerramento imediato ao atingir limite...\n")
    
    sucesso = asyncio.run(teste_encerramento_imediato())
    
    # Retornar código de saída apropriado
    exit(0 if sucesso else 1)


if __name__ == "__main__":
    main()
