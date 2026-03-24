"""
Teste para validar a atualização em lote da UI (Task 13.1).

Este teste verifica se o método atualizar_progresso_thread_safe
acumula 5 leads antes de atualizar a Treeview, otimizando a performance.

Requirements: 11.2
"""

import threading
import time
from typing import Dict, List
from gui_manager import LeadExtractorGUI


def test_batch_ui_update():
    """
    Testa se a UI é atualizada em lote a cada 5 leads.
    
    Valida:
    - Buffer acumula leads corretamente
    - UI é atualizada apenas quando buffer atinge 5 leads
    - Progresso final força atualização dos leads restantes
    """
    print("\n=== Teste de Atualização em Lote da UI ===\n")
    
    # Criar instância da GUI
    gui = LeadExtractorGUI()
    gui.criar_interface()
    
    # Contador de atualizações da UI
    update_count = 0
    original_update = gui._atualizar_ui_lote
    
    def mock_update(leads: List[Dict[str, str]], progresso: float):
        """Mock para contar quantas vezes a UI é atualizada."""
        nonlocal update_count
        update_count += 1
        print(f"[UPDATE {update_count}] Atualizando UI com {len(leads)} leads (progresso: {progresso*100:.1f}%)")
        # Chamar o método original
        original_update(leads, progresso)
    
    # Substituir método de atualização pelo mock
    gui._atualizar_ui_lote = mock_update
    
    # Simular extração de 12 leads
    print("Simulando extração de 12 leads...\n")
    
    for i in range(12):
        lead = {
            "nome": f"Empresa {i+1}",
            "telefone": f"(11) 9999-{i:04d}",
            "site": f"https://empresa{i+1}.com",
            "nota": "4.5",
            "comentarios": "100",
            "endereco": f"Rua Teste {i+1}, São Paulo"
        }
        
        progresso = (i + 1) / 12
        
        # Chamar callback (simula thread de extração)
        gui.atualizar_progresso_thread_safe(lead, progresso)
        
        # Processar eventos pendentes da GUI
        gui.root.update()
        
        # Pequeno delay para simular extração real
        time.sleep(0.05)
    
    # Processar eventos finais
    gui.root.update()
    
    # Validações
    print(f"\n=== Resultados ===")
    print(f"Total de atualizações da UI: {update_count}")
    print(f"Total de leads na tabela: {len(gui.leads_data)}")
    print(f"Tamanho do buffer: {len(gui.leads_buffer)}")
    
    # Verificar se houve atualização em lote
    # Com 12 leads, esperamos:
    # - 1ª atualização: leads 1-5 (quando buffer atinge 5)
    # - 2ª atualização: leads 6-10 (quando buffer atinge 5 novamente)
    # - 3ª atualização: leads 11-12 (quando progresso atinge 100%)
    expected_updates = 3
    
    assert update_count == expected_updates, \
        f"Esperado {expected_updates} atualizações, mas obteve {update_count}"
    
    assert len(gui.leads_data) == 12, \
        f"Esperado 12 leads na tabela, mas obteve {len(gui.leads_data)}"
    
    assert len(gui.leads_buffer) == 0, \
        f"Buffer deveria estar vazio, mas contém {len(gui.leads_buffer)} leads"
    
    print("\n✓ Teste passou! Atualização em lote funcionando corretamente.")
    print(f"✓ UI foi atualizada {update_count} vezes para 12 leads (otimização de ~{12/update_count:.1f}x)")
    
    # Fechar GUI
    gui.root.destroy()


def test_batch_update_with_exact_multiple():
    """
    Testa atualização em lote quando o número de leads é múltiplo exato de 5.
    """
    print("\n=== Teste com Múltiplo Exato de 5 ===\n")
    
    gui = LeadExtractorGUI()
    gui.criar_interface()
    
    update_count = 0
    original_update = gui._atualizar_ui_lote
    
    def mock_update(leads: List[Dict[str, str]], progresso: float):
        nonlocal update_count
        update_count += 1
        print(f"[UPDATE {update_count}] {len(leads)} leads (progresso: {progresso*100:.1f}%)")
        original_update(leads, progresso)
    
    gui._atualizar_ui_lote = mock_update
    
    # Simular extração de exatamente 10 leads
    print("Simulando extração de 10 leads...\n")
    
    for i in range(10):
        lead = {
            "nome": f"Empresa {i+1}",
            "telefone": f"(11) 9999-{i:04d}",
            "site": f"https://empresa{i+1}.com",
            "nota": "4.5",
            "comentarios": "100",
            "endereco": f"Rua Teste {i+1}, São Paulo"
        }
        
        progresso = (i + 1) / 10
        gui.atualizar_progresso_thread_safe(lead, progresso)
        gui.root.update()
        time.sleep(0.05)
    
    gui.root.update()
    
    print(f"\n=== Resultados ===")
    print(f"Total de atualizações: {update_count}")
    print(f"Total de leads: {len(gui.leads_data)}")
    
    # Com 10 leads, esperamos 2 atualizações (5+5)
    # Mas o último lead tem progresso=1.0, então pode forçar atualização
    assert len(gui.leads_data) == 10, f"Esperado 10 leads, obteve {len(gui.leads_data)}"
    assert len(gui.leads_buffer) == 0, f"Buffer deveria estar vazio"
    
    print(f"✓ Teste passou! {update_count} atualizações para 10 leads.")
    
    gui.root.destroy()


def test_buffer_thread_safety():
    """
    Testa se o buffer é thread-safe com múltiplas threads acessando.
    """
    print("\n=== Teste de Thread Safety do Buffer ===\n")
    
    gui = LeadExtractorGUI()
    gui.criar_interface()
    
    # Simular múltiplas threads adicionando leads
    def add_leads(thread_id: int, count: int):
        for i in range(count):
            lead = {
                "nome": f"Thread{thread_id}-Lead{i+1}",
                "telefone": f"(11) {thread_id}{i:03d}-0000",
                "site": f"https://t{thread_id}lead{i+1}.com",
                "nota": "4.0",
                "comentarios": "50",
                "endereco": f"Endereço {thread_id}-{i+1}"
            }
            progresso = 0.5  # Progresso intermediário
            gui.atualizar_progresso_thread_safe(lead, progresso)
            time.sleep(0.01)
    
    # Criar 3 threads adicionando 5 leads cada
    threads = []
    for t_id in range(3):
        thread = threading.Thread(target=add_leads, args=(t_id, 5))
        threads.append(thread)
        thread.start()
    
    # Aguardar todas as threads
    for thread in threads:
        thread.join()
    
    # Forçar atualização final
    gui.atualizar_progresso_thread_safe(
        {"nome": "Final", "telefone": "N/A", "site": "N/A", 
         "nota": "N/A", "comentarios": "N/A", "endereco": "N/A"},
        1.0
    )
    
    # Processar eventos
    gui.root.update()
    time.sleep(0.1)
    gui.root.update()
    
    print(f"Total de leads processados: {len(gui.leads_data)}")
    print(f"Buffer final: {len(gui.leads_buffer)}")
    
    # Verificar que todos os 16 leads foram processados (3*5 + 1)
    assert len(gui.leads_data) == 16, f"Esperado 16 leads, obteve {len(gui.leads_data)}"
    
    print("✓ Teste de thread safety passou!")
    
    gui.root.destroy()


if __name__ == "__main__":
    try:
        test_batch_ui_update()
        test_batch_update_with_exact_multiple()
        test_buffer_thread_safety()
        
        print("\n" + "="*50)
        print("✓ TODOS OS TESTES PASSARAM!")
        print("="*50)
        
    except AssertionError as e:
        print(f"\n✗ TESTE FALHOU: {e}")
        exit(1)
    except Exception as e:
        print(f"\n✗ ERRO: {e}")
        import traceback
        traceback.print_exc()
        exit(1)
