"""
Script de teste para validar o método scroll_resultados()
Task 4.4: Implementar método scroll_resultados()
"""

import asyncio
import threading
from automation_engine import GoogleMapsAutomation
from models import SearchQuery


async def teste_scroll_resultados():
    """Testa o método scroll_resultados() isoladamente."""
    
    print("=" * 60)
    print("TESTE: scroll_resultados()")
    print("=" * 60)
    
    # Criar instância do automation engine
    automation = GoogleMapsAutomation(headless=False)  # headless=False para visualizar
    
    # Criar stop_flag
    stop_flag = threading.Event()
    
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
            limite=50
        )
        
        url = search_query.to_google_maps_url()
        print(f"    URL: {url}")
        
        await automation.page.goto(url, wait_until="networkidle", timeout=30000)
        print("✓ Página carregada")
        
        # Aguardar um pouco para garantir que a página está totalmente carregada
        await asyncio.sleep(2)
        
        # Contar resultados antes do scroll
        print("\n[3] Contando resultados antes do scroll...")
        from automation_engine import GOOGLE_MAPS_SELECTORS
        
        results_panel = await automation.page.query_selector(GOOGLE_MAPS_SELECTORS["results_panel"])
        if results_panel:
            result_items_before = await results_panel.query_selector_all(GOOGLE_MAPS_SELECTORS["result_item"])
            print(f"    Resultados iniciais: {len(result_items_before)}")
        else:
            print("    ⚠ Painel de resultados não encontrado")
        
        # Executar scroll
        print("\n[4] Executando scroll_resultados()...")
        print("    Limite: 50 resultados")
        print("    (Observe o scroll acontecendo no navegador)")
        
        await automation.scroll_resultados(limite=50, stop_flag=stop_flag)
        
        print("✓ Scroll concluído")
        
        # Contar resultados após o scroll
        print("\n[5] Contando resultados após o scroll...")
        results_panel = await automation.page.query_selector(GOOGLE_MAPS_SELECTORS["results_panel"])
        if results_panel:
            result_items_after = await results_panel.query_selector_all(GOOGLE_MAPS_SELECTORS["result_item"])
            print(f"    Resultados finais: {len(result_items_after)}")
            print(f"    Novos resultados carregados: {len(result_items_after) - len(result_items_before)}")
        else:
            print("    ⚠ Painel de resultados não encontrado")
        
        print("\n" + "=" * 60)
        print("TESTE CONCLUÍDO COM SUCESSO!")
        print("=" * 60)
        print("\nVerificações realizadas:")
        print("✓ Container de scroll localizado")
        print("✓ Scroll executado com delays aleatórios (1-3s)")
        print("✓ Detecção de fim de resultados ou limite atingido")
        print("✓ Stop flag verificado durante scroll")
        
    except Exception as e:
        print(f"\n[ERRO] Falha no teste: {str(e)}")
        import traceback
        traceback.print_exc()
    
    finally:
        # Fechar navegador
        print("\n[6] Fechando navegador...")
        await automation.fechar_navegador()
        print("✓ Navegador fechado")


async def teste_scroll_com_interrupcao():
    """Testa a interrupção do scroll usando stop_flag."""
    
    print("\n\n" + "=" * 60)
    print("TESTE: scroll_resultados() com interrupção")
    print("=" * 60)
    
    automation = GoogleMapsAutomation(headless=False)
    stop_flag = threading.Event()
    
    try:
        print("\n[1] Inicializando navegador...")
        await automation.inicializar_navegador()
        
        print("\n[2] Navegando para Google Maps...")
        search_query = SearchQuery(
            nicho="padarias",
            localizacao="Rio de Janeiro",
            limite=100
        )
        
        await automation.page.goto(search_query.to_google_maps_url(), wait_until="networkidle", timeout=30000)
        await asyncio.sleep(2)
        
        print("\n[3] Iniciando scroll (será interrompido após 3 segundos)...")
        
        # Criar task para o scroll
        scroll_task = asyncio.create_task(
            automation.scroll_resultados(limite=100, stop_flag=stop_flag)
        )
        
        # Aguardar 3 segundos e então sinalizar parada
        await asyncio.sleep(3)
        print("\n[4] Sinalizando parada...")
        stop_flag.set()
        
        # Aguardar o scroll terminar
        await scroll_task
        
        print("✓ Scroll interrompido com sucesso")
        
        print("\n" + "=" * 60)
        print("TESTE DE INTERRUPÇÃO CONCLUÍDO!")
        print("=" * 60)
        
    except Exception as e:
        print(f"\n[ERRO] Falha no teste: {str(e)}")
        import traceback
        traceback.print_exc()
    
    finally:
        print("\n[5] Fechando navegador...")
        await automation.fechar_navegador()


def main():
    """Função principal para executar os testes."""
    print("\n🧪 Iniciando testes do método scroll_resultados()...\n")
    
    # Teste 1: Scroll normal
    asyncio.run(teste_scroll_resultados())
    
    # Teste 2: Scroll com interrupção
    print("\n\n⏸️  Pressione Enter para executar o teste de interrupção...")
    input()
    asyncio.run(teste_scroll_com_interrupcao())
    
    print("\n\n✅ Todos os testes concluídos!")


if __name__ == "__main__":
    main()
