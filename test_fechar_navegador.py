"""
Teste para o método fechar_navegador() do Automation Engine.
Verifica se o navegador é fechado corretamente e os recursos são liberados.
"""

import asyncio
from automation_engine import GoogleMapsAutomation


async def test_fechar_navegador():
    """
    Testa o método fechar_navegador() para garantir que:
    1. Fecha a página do navegador
    2. Fecha o browser
    3. Para o Playwright
    4. Libera todos os recursos
    """
    print("=== Teste: fechar_navegador() ===\n")
    
    # Criar instância do GoogleMapsAutomation
    automation = GoogleMapsAutomation(headless=True)
    
    # Teste 1: Fechar navegador após inicialização
    print("Teste 1: Fechar navegador após inicialização")
    print("[1] Inicializando navegador...")
    await automation.inicializar_navegador()
    print("✓ Navegador inicializado")
    
    # Verificar que os recursos foram criados
    assert automation.playwright is not None, "Playwright não foi inicializado"
    assert automation.browser is not None, "Browser não foi inicializado"
    assert automation.page is not None, "Page não foi inicializada"
    print("✓ Recursos do navegador criados\n")
    
    print("[2] Fechando navegador...")
    await automation.fechar_navegador()
    print("✓ Navegador fechado")
    
    # Verificar que os recursos foram liberados
    assert automation.playwright is None, "Playwright não foi liberado"
    assert automation.browser is None, "Browser não foi liberado"
    assert automation.page is None, "Page não foi liberada"
    print("✓ Recursos do navegador liberados\n")
    
    # Teste 2: Fechar navegador quando já está fechado (deve ser seguro)
    print("Teste 2: Fechar navegador quando já está fechado")
    print("[1] Tentando fechar navegador novamente...")
    await automation.fechar_navegador()
    print("✓ Método executado sem erros")
    
    # Verificar que os recursos continuam None
    assert automation.playwright is None, "Playwright deveria ser None"
    assert automation.browser is None, "Browser deveria ser None"
    assert automation.page is None, "Page deveria ser None"
    print("✓ Método é seguro para chamadas múltiplas\n")
    
    # Teste 3: Fechar navegador após navegação
    print("Teste 3: Fechar navegador após navegação")
    print("[1] Inicializando navegador...")
    await automation.inicializar_navegador()
    print("✓ Navegador inicializado")
    
    print("[2] Navegando para uma página...")
    await automation.page.goto("https://www.google.com", timeout=10000)
    print("✓ Navegação concluída")
    
    print("[3] Fechando navegador...")
    await automation.fechar_navegador()
    print("✓ Navegador fechado após navegação")
    
    # Verificar que os recursos foram liberados
    assert automation.playwright is None, "Playwright não foi liberado"
    assert automation.browser is None, "Browser não foi liberado"
    assert automation.page is None, "Page não foi liberada"
    print("✓ Recursos liberados corretamente\n")
    
    print("=== Todos os testes passaram! ===")


if __name__ == "__main__":
    # Executar teste assíncrono
    asyncio.run(test_fechar_navegador())
