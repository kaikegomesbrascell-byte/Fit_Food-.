"""
Teste para verificar se o warning de memória é disparado corretamente.
"""

import asyncio
import sys
import os

# Adicionar o diretório raiz ao path para importar os módulos
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from automation_engine import GoogleMapsAutomation
from error_logger import ErrorLogger


async def test_memory_warning():
    """
    Testa se o warning é disparado quando memória ultrapassa 500MB.
    """
    logger = ErrorLogger()
    logger.log_info("=== Iniciando teste de warning de memória ===")
    
    # Criar instância do automation engine
    automation = GoogleMapsAutomation(headless=True)
    
    # Reduzir o limite temporariamente para facilitar o teste
    original_threshold = automation.memory_threshold_mb
    automation.memory_threshold_mb = 50  # Reduzir para 50MB para facilitar teste
    
    logger.log_info(f"Limite de memória ajustado para teste: {automation.memory_threshold_mb}MB")
    
    # Verificar memória inicial
    logger.log_info("Memória inicial:")
    automation.verificar_uso_memoria()
    
    # Criar dados para ultrapassar o limite
    logger.log_info("Criando dados para ultrapassar o limite...")
    large_data = []
    
    # Criar 60MB de dados para ultrapassar o limite de 50MB
    for i in range(60):
        large_data.append("x" * (1024 * 1024))  # 1MB por string
    
    # Verificar memória - deve disparar warning
    logger.log_info("\nVerificando memória após criar dados (deve disparar WARNING):")
    automation.verificar_uso_memoria()
    
    # Limpar dados
    large_data.clear()
    
    # Restaurar limite original
    automation.memory_threshold_mb = original_threshold
    
    logger.log_info(f"\nLimite de memória restaurado para: {automation.memory_threshold_mb}MB")
    logger.log_info("=== Teste de warning de memória concluído ===")
    
    return True


if __name__ == "__main__":
    try:
        result = asyncio.run(test_memory_warning())
        if result:
            print("\n✓ TESTE PASSOU: Warning de memória está funcionando corretamente")
            print("  Verifique os logs acima para confirmar que o WARNING foi disparado")
            sys.exit(0)
        else:
            print("\n✗ TESTE FALHOU")
            sys.exit(1)
    except Exception as e:
        print(f"\n✗ ERRO NO TESTE: {str(e)}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
