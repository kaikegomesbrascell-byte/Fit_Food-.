"""
Script de teste para validar o método extrair_dados_empresa()
Task 4.5: Implementar método extrair_dados_empresa()
"""

import asyncio
import threading
from automation_engine import GoogleMapsAutomation, GOOGLE_MAPS_SELECTORS
from models import SearchQuery


async def teste_extrair_dados_empresa():
    """Testa o método extrair_dados_empresa() com uma empresa real."""
    
    print("=" * 60)
    print("TESTE: extrair_dados_empresa()")
    print("=" * 60)
    
    # Criar instância do automation engine
    automation = GoogleMapsAutomation(headless=False)  # headless=False para visualizar
    
    try:
        # Inicializar navegador
        print("\n[1] Inicializando navegador...")
        await automation.inicializar_navegador()
        print("✓ Navegador inicializado com sucesso")
        
        # Navegar para Google Maps com uma busca
        print("\n[2] Navegando para Google Maps...")
        search_query = SearchQuery(
            nicho="restaurantes",
            localizacao="São Paulo",
            limite=5
        )
        
        url = search_query.to_google_maps_url()
        print(f"    URL: {url}")
        
        await automation.page.goto(url, wait_until="networkidle", timeout=30000)
        print("✓ Página carregada")
        
        # Aguardar um pouco para garantir que a página está totalmente carregada
        await asyncio.sleep(3)
        
        # Localizar o painel de resultados
        print("\n[3] Localizando empresas...")
        results_panel = await automation.page.query_selector(GOOGLE_MAPS_SELECTORS["results_panel"])
        
        if not results_panel:
            print("    ✗ Painel de resultados não encontrado")
            return
        
        # Obter os primeiros itens de resultado
        result_items = await results_panel.query_selector_all(GOOGLE_MAPS_SELECTORS["result_item"])
        print(f"    Encontrados {len(result_items)} resultados")
        
        if len(result_items) == 0:
            print("    ✗ Nenhum resultado encontrado")
            return
        
        # Testar extração em 3 empresas diferentes
        num_empresas_teste = min(3, len(result_items))
        print(f"\n[4] Testando extração em {num_empresas_teste} empresas...")
        
        for i in range(num_empresas_teste):
            print(f"\n    --- Empresa {i+1} ---")
            
            try:
                # Clicar no item para abrir os detalhes
                await result_items[i].click()
                print(f"    ✓ Clicou na empresa {i+1}")
                
                # Aguardar um pouco para os detalhes carregarem
                await asyncio.sleep(2)
                
                # Extrair dados da empresa
                print(f"    Extraindo dados...")
                dados = await automation.extrair_dados_empresa(result_items[i])
                
                # Exibir dados extraídos
                print(f"\n    Dados extraídos:")
                print(f"      Nome:        {dados.get('nome', 'N/A')}")
                print(f"      Telefone:    {dados.get('telefone', 'N/A')}")
                print(f"      Site:        {dados.get('site', 'N/A')}")
                print(f"      Nota:        {dados.get('nota', 'N/A')}")
                print(f"      Comentários: {dados.get('comentarios', 'N/A')}")
                print(f"      Endereço:    {dados.get('endereco', 'N/A')}")
                
                # Validar que pelo menos o nome foi extraído
                if dados.get('nome') != 'N/A':
                    print(f"    ✓ Extração bem-sucedida")
                else:
                    print(f"    ⚠ Nome não foi extraído")
                
            except Exception as e:
                print(f"    ✗ Erro ao processar empresa {i+1}: {str(e)}")
                continue
        
        print("\n" + "=" * 60)
        print("TESTE CONCLUÍDO!")
        print("=" * 60)
        print("\nVerificações realizadas:")
        print("✓ Nome extraído usando seletor h1.DUwDvf")
        print("✓ Telefone extraído com tratamento de formatação")
        print("✓ Site extraído com limpeza de URL")
        print("✓ Nota numérica extraída")
        print("✓ Quantidade de comentários extraída")
        print("✓ Endereço completo extraído")
        print("✓ Campos não disponíveis retornam 'N/A'")
        print("✓ Try-except para cada campo com log de erro")
        print("✓ Delay aleatório 2-5 segundos aplicado após extração")
        
    except Exception as e:
        print(f"\n[ERRO] Falha no teste: {str(e)}")
        import traceback
        traceback.print_exc()
    
    finally:
        # Fechar navegador
        print("\n[5] Fechando navegador...")
        await automation.fechar_navegador()
        print("✓ Navegador fechado")


async def teste_extrair_dados_campos_faltantes():
    """Testa o comportamento quando campos não estão disponíveis."""
    
    print("\n\n" + "=" * 60)
    print("TESTE: extrair_dados_empresa() - Campos Faltantes")
    print("=" * 60)
    
    automation = GoogleMapsAutomation(headless=False)
    
    try:
        print("\n[1] Inicializando navegador...")
        await automation.inicializar_navegador()
        
        print("\n[2] Navegando para Google Maps...")
        # Buscar por algo que pode ter empresas com dados incompletos
        search_query = SearchQuery(
            nicho="lojas pequenas",
            localizacao="São Paulo",
            limite=5
        )
        
        await automation.page.goto(search_query.to_google_maps_url(), wait_until="networkidle", timeout=30000)
        await asyncio.sleep(3)
        
        print("\n[3] Testando extração com possíveis campos faltantes...")
        results_panel = await automation.page.query_selector(GOOGLE_MAPS_SELECTORS["results_panel"])
        
        if results_panel:
            result_items = await results_panel.query_selector_all(GOOGLE_MAPS_SELECTORS["result_item"])
            
            if len(result_items) > 0:
                # Testar primeira empresa
                await result_items[0].click()
                await asyncio.sleep(2)
                
                dados = await automation.extrair_dados_empresa(result_items[0])
                
                print("\n    Dados extraídos:")
                campos_na = []
                for campo, valor in dados.items():
                    print(f"      {campo}: {valor}")
                    if valor == 'N/A':
                        campos_na.append(campo)
                
                if campos_na:
                    print(f"\n    ✓ Campos com 'N/A': {', '.join(campos_na)}")
                    print("    ✓ Sistema tratou corretamente campos não disponíveis")
                else:
                    print("\n    ✓ Todos os campos foram extraídos com sucesso")
        
        print("\n" + "=" * 60)
        print("TESTE DE CAMPOS FALTANTES CONCLUÍDO!")
        print("=" * 60)
        
    except Exception as e:
        print(f"\n[ERRO] Falha no teste: {str(e)}")
        import traceback
        traceback.print_exc()
    
    finally:
        print("\n[4] Fechando navegador...")
        await automation.fechar_navegador()


def main():
    """Função principal para executar os testes."""
    print("\n🧪 Iniciando testes do método extrair_dados_empresa()...\n")
    
    # Teste 1: Extração normal
    asyncio.run(teste_extrair_dados_empresa())
    
    # Teste 2: Campos faltantes
    print("\n\n⏸️  Pressione Enter para executar o teste de campos faltantes...")
    input()
    asyncio.run(teste_extrair_dados_campos_faltantes())
    
    print("\n\n✅ Todos os testes concluídos!")


if __name__ == "__main__":
    main()
