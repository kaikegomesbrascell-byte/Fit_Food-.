"""
Teste de integração para GUI Manager
Verifica que todos os componentes funcionam juntos.
"""

from gui_manager import LeadExtractorGUI
from unittest.mock import patch, Mock
import threading


def test_gui_initialization():
    """Testa inicialização da GUI."""
    with patch('gui_manager.ctk.CTk'):
        gui = LeadExtractorGUI()
        
        # Verificar atributos inicializados
        assert gui.extraction_thread is None
        assert isinstance(gui.stop_flag, threading.Event)
        assert gui.leads_data == []
        print("✓ GUI inicializada corretamente")


def test_gui_interface_creation():
    """Testa criação da interface."""
    with patch('gui_manager.ctk.CTk'):
        gui = LeadExtractorGUI()
        
        # Mock dos widgets
        with patch('gui_manager.ctk.CTkFrame'), \
             patch('gui_manager.ctk.CTkLabel'), \
             patch('gui_manager.ctk.CTkEntry'), \
             patch('gui_manager.ctk.CTkSlider'), \
             patch('gui_manager.ctk.CTkButton'), \
             patch('gui_manager.ctk.CTkProgressBar'), \
             patch('gui_manager.ttk.Treeview'), \
             patch('gui_manager.ttk.Scrollbar'):
            
            gui.criar_interface()
            
            # Verificar que widgets foram criados
            assert gui.nicho_entry is not None
            assert gui.localizacao_entry is not None
            assert gui.limite_slider is not None
            assert gui.progress_bar is not None
            assert gui.data_table is not None
            assert gui.btn_iniciar is not None
            assert gui.btn_parar is not None
            assert gui.btn_exportar is not None
            print("✓ Interface criada corretamente")


def test_complete_workflow():
    """Testa fluxo completo: validação -> atualização -> exportação."""
    with patch('gui_manager.ctk.CTk'):
        gui = LeadExtractorGUI()
        
        # Mock dos widgets necessários
        gui.progress_bar = Mock()
        gui.status_label = Mock()
        gui.data_table = Mock()
        gui.data_table.insert = Mock()
        gui.root = Mock()
        
        # 1. Adicionar alguns leads via atualização de UI
        lead1 = {
            "nome": "Empresa 1",
            "telefone": "(11) 1111-1111",
            "site": "www.empresa1.com",
            "nota": "4.5",
            "comentarios": "100",
            "endereco": "Rua 1, 123"
        }
        
        lead2 = {
            "nome": "Empresa 2",
            "telefone": "(11) 2222-2222",
            "site": "www.empresa2.com",
            "nota": "4.8",
            "comentarios": "200",
            "endereco": "Rua 2, 456"
        }
        
        gui._atualizar_ui(lead1, 0.5)
        gui._atualizar_ui(lead2, 1.0)
        
        # Verificar que leads foram adicionados
        assert len(gui.leads_data) == 2
        assert gui.leads_data[0]["Nome"] == "Empresa 1"
        assert gui.leads_data[1]["Nome"] == "Empresa 2"
        print("✓ Leads adicionados corretamente")
        
        # 2. Testar exportação com dados
        with patch('gui_manager.messagebox') as mock_msg, \
             patch('gui_manager.filedialog') as mock_file, \
             patch('data_exporter.DataExporter') as mock_exporter_class, \
             patch('error_logger.ErrorLogger'):
            
            mock_msg.askquestion.return_value = 'yes'
            mock_file.asksaveasfilename.return_value = '/tmp/test.xlsx'
            
            mock_exporter = Mock()
            mock_exporter.exportar_excel.return_value = True
            mock_exporter_class.return_value = mock_exporter
            
            gui.exportar_dados()
            
            # Verificar que exportação foi chamada
            mock_exporter_class.assert_called_once_with(gui.leads_data)
            mock_exporter.exportar_excel.assert_called_once()
            print("✓ Exportação funcionou corretamente")


def test_stop_flag_mechanism():
    """Testa mecanismo de parada."""
    with patch('gui_manager.ctk.CTk'):
        gui = LeadExtractorGUI()
        
        # Mock dos widgets
        gui.btn_parar = Mock()
        gui.status_label = Mock()
        
        # Inicializar stop_flag
        gui.stop_flag = threading.Event()
        
        # Verificar que flag não está setada
        assert not gui.stop_flag.is_set()
        
        # Parar extração
        with patch('error_logger.ErrorLogger'):
            gui.parar_extracao()
        
        # Verificar que flag foi setada
        assert gui.stop_flag.is_set()
        print("✓ Mecanismo de parada funciona corretamente")


if __name__ == '__main__':
    print("\n=== Testes de Integração GUI Manager ===\n")
    
    test_gui_initialization()
    test_gui_interface_creation()
    test_complete_workflow()
    test_stop_flag_mechanism()
    
    print("\n✅ Todos os testes de integração passaram!\n")
