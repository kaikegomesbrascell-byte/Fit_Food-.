"""
Teste Simplificado - Checkpoint 5
Valida apenas os delays anti-bot sem executar busca completa.
"""

import asyncio
import time
from automation_engine import GoogleMapsAutomation


async def teste_delays_simples():
    """Testa apenas os delays anti-bot."""
    print("\n" + "=" * 70)
    print("TESTE SIMPLIFICADO: Delays Anti-Bot")
    print("=" * 70)
    
    automation = GoogleMapsAutomation(headless=True)
    
    print("\n[1/2] Testando delays aleatórios (5 iterações)...")
    delays = []
    
    for i in range(5):
        inicio = time.time()
        await automation.aplicar_delay_humano(min_sec=1.0, max_sec=3.0)
        fim = time.time()
        delay = fim - inicio
        delays.append(delay)
        print(f"  Delay {i+1}: {delay:.2f} segundos")
    
    print("\n[2/2] Análise dos delays:")
    print(f"  Mínimo: {min(delays):.2f}s")
    print(f"  Máximo: {max(delays):.2f}s")
    print(f"  Média: {sum(delays)/len(delays):.2f}s")
    
    # Validar
    delays_no_range = all(1.0 <= d <= 3.5 for d in delays)
    delays_variados = len(set([round(d, 1) for d in delays])) >= 3
    
    if delays_no_range and delays_variados:
        print("\n  ✓ TESTE PASSOU: Delays funcionando corretamente")
        return True
    else:
        print("\n  ✗ TESTE FALHOU")
        if not delays_no_range:
            print("    - Alguns delays fora do range esperado")
        if not delays_variados:
            print("    - Pouca variação nos delays")
        return False


async def teste_inicializacao():
    """Testa inicialização e fechamento do navegador."""
    print("\n" + "=" * 70)
    print("TESTE: Inicialização do Navegador")
    print("=" * 70)
    
    automation = GoogleMapsAutomation(headless=True)
    
    try:
        print("\n[1/2] Inicializando navegador...")
        await automation.inicializar_navegador()
        print("  ✓ Navegador inicializado com sucesso")
        
        print("\n[2/2] Fechando navegador...")
        await automation.fechar_navegador()
        print("  ✓ Navegador fechado com sucesso")
        
        print("\n  ✓ TESTE PASSOU: Inicialização funcionando")
        return True
        
    except Exception as e:
        print(f"\n  ✗ TESTE FALHOU: {str(e)}")
        return False


async def main():
    """Executa testes simplificados."""
    print("\n🚀 Checkpoint 5 - Testes Simplificados\n")
    
    # Teste 1: Inicialização
    teste1 = await teste_inicializacao()
    
    # Teste 2: Delays
    teste2 = await teste_delays_simples()
    
    # Resumo
    print("\n" + "=" * 70)
    print("RESUMO")
    print("=" * 70)
    print(f"Teste Inicialização: {'✓ PASSOU' if teste1 else '✗ FALHOU'}")
    print(f"Teste Delays:        {'✓ PASSOU' if teste2 else '✗ FALHOU'}")
    
    if teste1 and teste2:
        print("\n✓ Componentes básicos do Automation Engine funcionando!")
        print("\nPróximo passo: Execute o teste completo com:")
        print("  python test_checkpoint_automation_engine.py")
        return 0
    else:
        print("\n✗ Alguns testes falharam")
        return 1


if __name__ == "__main__":
    exit(asyncio.run(main()))
