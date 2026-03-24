"""
Teste para verificar funcionalidade de monitoramento de memória.
"""

import asyncio
import sys
import os

# Adicionar o diretório raiz ao path para importar os módulos
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from automation_engine import GoogleMapsAutomation
from error_logger import ErrorLogger


async def test_memory_monitoring():
    """
    Testa se o monitoramento de memória está funcionando corretamente.
    """
    logger = ErrorLogger()
    logger.log_info("=== Iniciando teste de monitoramento de memória ===")
    
    # Criar instância do automation engine
    automation = GoogleMapsAutomation(headless=True)
    
    # Verificar se os atributos foram inicializados corretamente
    assert hasattr(automation, 'process'), "Atributo 'process' não foi inicializado"
    assert hasattr(automation, 'memory_threshold_mb'), "Atributo 'memory_threshold_mb' não foi inicializado"
    assert automation.memory_threshold_mb == 500, f"Limite de memória deveria ser 500MB, mas é {automation.memory_threshold_mb}MB"
    
    logger.log_info("✓ Atributos de monitoramento de memória inicializados corretamente")
    
    # Testar método verificar_uso_memoria
    logger.log_info("Testando método verificar_uso_memoria()...")
    automation.verificar_uso_memoria()
    
    logger.log_info("✓ Método verificar_uso_memoria() executado com sucesso")
    
    # Simular uso de memória (criar uma lista grande)
    logger.log_info("Simulando uso de memória...")
    
    # Verificar memória antes
    automation.verificar_uso_memoria()
    
    # Criar dados para aumentar uso de memória
    # Cada string de 1MB, criar várias para aumentar memória
    large_data = []
    for i in range(100):
        large_data.append("x" * (1024 * 1024))  # 1MB por string
        if i % 20 == 0:
            logger.log_info(f"Criados {i+1} MB de dados...")
            automation.verificar_uso_memoria()
    
    # Verificar memória depois
    logger.log_info("Verificação final de memória:")
    automation.verificar_uso_memoria()
    
    # Limpar dados
    large_data.clear()
    
    logger.log_info("=== Teste de monitoramento de memória concluído com sucesso ===")
    return True


if __name__ == "__main__":
    try:
        result = asyncio.run(test_memory_monitoring())
        if result:
            print("\n✓ TESTE PASSOU: Monitoramento de memória está funcionando corretamente")
            sys.exit(0)
        else:
            print("\n✗ TESTE FALHOU")
            sys.exit(1)
    except Exception as e:
        print(f"\n✗ ERRO NO TESTE: {str(e)}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
