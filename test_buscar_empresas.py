"""
Script de teste para validar o método buscar_empresas()
"""

import asyncio
import threading
from automation_engine import GoogleMapsAutomation


def callback_teste(lead_dict, progresso):
    """Callback de teste para receber atualizações de progresso."""
    print(f"[CALLBACK] Progresso: {progresso*100:.1f}% - Lead: {lead_dict.get('nome', 'N/A')}")


async def teste_buscar_empresas():
    """Testa o método buscar_empresas() com parâmetros de exemplo."""
    
    print("=" * 60)
    print("TESTE: buscar_empresas()")
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
        
        # Executar busca
        print("\n[2] Executando busca de empresas...")
        print("    Nicho: restaurantes")
        print("    Localização: São Paulo")
        print("    Limite: 10 leads")
        
        leads = await automation.buscar_empresas(
            nicho="restaurantes",
            localizacao="São Paulo",
            limite=10,
            callback=callback_teste,
            stop_flag=stop_flag
        )
        
        # Exibir resultados
        print(f"\n[3] Extração concluída!")
        print(f"    Total de leads extraídos: {len(leads)}")
        
        if leads:
            print("\n[4] Exemplo de lead extraído:")
            primeiro_lead = leads[0]
            for chave, valor in primeiro_lead.items():
                print(f"    {chave}: {valor}")
        
        print("\n" + "=" * 60)
        print("TESTE CONCLUÍDO COM SUCESSO!")
        print("=" * 60)
        
    except Exception as e:
        print(f"\n[ERRO] Falha no teste: {str(e)}")
        import traceback
        traceback.print_exc()
    
    finally:
        # Fechar navegador
        print("\n[5] Fechando navegador...")
        await automation.fechar_navegador()
        print("✓ Navegador fechado")


def main():
    """Função principal para executar o teste."""
    print("\nIniciando teste do método buscar_empresas()...\n")
    asyncio.run(teste_buscar_empresas())


if __name__ == "__main__":
    main()
