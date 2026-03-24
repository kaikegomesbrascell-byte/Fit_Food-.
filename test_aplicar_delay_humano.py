"""
Teste para o método aplicar_delay_humano() do Automation Engine.
Verifica se o delay aleatório está sendo aplicado corretamente.
"""

import asyncio
import time
from automation_engine import GoogleMapsAutomation


async def test_aplicar_delay_humano():
    """
    Testa o método aplicar_delay_humano() para garantir que:
    1. Gera delay aleatório entre min_sec e max_sec
    2. Usa asyncio.sleep() para delay assíncrono
    3. O delay está dentro do intervalo esperado
    """
    print("=== Teste: aplicar_delay_humano() ===\n")
    
    # Criar instância do GoogleMapsAutomation
    automation = GoogleMapsAutomation(headless=True)
    
    # Teste 1: Delay padrão (1.0 a 3.0 segundos)
    print("Teste 1: Delay padrão (1.0 a 3.0 segundos)")
    start_time = time.time()
    await automation.aplicar_delay_humano()
    elapsed_time = time.time() - start_time
    print(f"Tempo decorrido: {elapsed_time:.2f} segundos")
    
    # Verificar se está no intervalo esperado
    assert 1.0 <= elapsed_time <= 3.5, f"Delay fora do intervalo esperado: {elapsed_time:.2f}s"
    print("✓ Delay está dentro do intervalo esperado\n")
    
    # Teste 2: Delay customizado (2.0 a 5.0 segundos)
    print("Teste 2: Delay customizado (2.0 a 5.0 segundos)")
    start_time = time.time()
    await automation.aplicar_delay_humano(2.0, 5.0)
    elapsed_time = time.time() - start_time
    print(f"Tempo decorrido: {elapsed_time:.2f} segundos")
    
    # Verificar se está no intervalo esperado
    assert 2.0 <= elapsed_time <= 5.5, f"Delay fora do intervalo esperado: {elapsed_time:.2f}s"
    print("✓ Delay está dentro do intervalo esperado\n")
    
    # Teste 3: Delay curto (0.5 a 1.0 segundos)
    print("Teste 3: Delay curto (0.5 a 1.0 segundos)")
    start_time = time.time()
    await automation.aplicar_delay_humano(0.5, 1.0)
    elapsed_time = time.time() - start_time
    print(f"Tempo decorrido: {elapsed_time:.2f} segundos")
    
    # Verificar se está no intervalo esperado
    assert 0.5 <= elapsed_time <= 1.5, f"Delay fora do intervalo esperado: {elapsed_time:.2f}s"
    print("✓ Delay está dentro do intervalo esperado\n")
    
    # Teste 4: Verificar aleatoriedade (executar múltiplas vezes)
    print("Teste 4: Verificar aleatoriedade (5 execuções)")
    delays = []
    for i in range(5):
        start_time = time.time()
        await automation.aplicar_delay_humano(1.0, 2.0)
        elapsed_time = time.time() - start_time
        delays.append(elapsed_time)
        print(f"  Execução {i+1}: {elapsed_time:.2f} segundos")
    
    # Verificar se os delays são diferentes (aleatoriedade)
    unique_delays = len(set([round(d, 1) for d in delays]))
    print(f"Delays únicos (arredondados): {unique_delays}/5")
    assert unique_delays >= 3, "Delays não parecem ser aleatórios"
    print("✓ Delays são aleatórios\n")
    
    print("=== Todos os testes passaram! ===")


if __name__ == "__main__":
    # Executar teste assíncrono
    asyncio.run(test_aplicar_delay_humano())
