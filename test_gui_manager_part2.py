"""
Teste para GUI Manager Part 2 - Tasks 9.1-9.7
Testa os métodos de lógica de negócio implementados.
"""

import unittest
from unittest.mock import Mock, patch, MagicMock
from gui_manager import LeadExtractorGUI
import threading


class TestGUIManagerPart2(unittest.TestCase):
    """Testes para os métodos de lógica de negócio do GUI Manager."""
    
    def setUp(self):
        """Configura ambiente de teste."""
        # Mock do CTk para evitar criar janela real
        with patch('gui_manager.ctk.CTk'):
            self.gui = LeadExtractorGUI()
            
            # Configurar mocks dos widgets necessários
            self.gui.nicho_entry = Mock()
            self.gui.localizacao_entry = Mock()
            self.gui.limite_slider = Mock()
            self.gui.progress_bar = Mock()
            self.gui.status_label = Mock()
            self.gui.data_table = Mock()
            self.gui.btn_iniciar = Mock()
            self.gui.btn_parar = Mock()
            self.gui.btn_exportar = Mock()
            self.gui.root = Mock()
    
    @patch('license_validator.LicenseValidator')
    @patch('gui_manager.messagebox')
    def test_validar_licenca_valida(self, mock_messagebox, mock_validator_class):
        """Testa validação de licença válida."""
        # Configurar mock para retornar licença válida
        mock_validator = Mock()
        mock_validator.validar_licenca.return_value = (True, "Licença válida até 2025-12-31")
        mock_validator_class.return_value = mock_validator
        
        # Executar validação
        resultado = self.gui.validar_licenca()
        
        # Verificar resultado
        self.assertTrue(resultado)
        mock_messagebox.showinfo.assert_called_once()
        mock_validator.validar_licenca.assert_called_once()
    
    @patch('license_validator.LicenseValidator')
    @patch('gui_manager.messagebox')
    def test_validar_licenca_invalida(self, mock_messagebox, mock_validator_class):
        """Testa validação de licença inválida."""
        # Configurar mock para retornar licença inválida
        mock_validator = Mock()
        mock_validator.validar_licenca.return_value = (False, "Licença expirada")
        mock_validator_class.return_value = mock_validator
        
        # Executar validação
        resultado = self.gui.validar_licenca()
        
        # Verificar resultado
        self.assertFalse(resultado)
        mock_messagebox.showerror.assert_called_once()
    
    def test_atualizar_progresso_thread_safe(self):
        """Testa atualização de progresso thread-safe com buffer."""
        # Preparar dados de teste
        lead = {
            "nome": "Empresa Teste",
            "telefone": "(11) 1234-5678",
            "site": "www.teste.com",
            "nota": "4.5",
            "comentarios": "100",
            "endereco": "Rua Teste, 123"
        }
        
        # Adicionar 4 leads (não deve chamar root.after ainda)
        for i in range(4):
            self.gui.atualizar_progresso_thread_safe(lead, 0.4)
        
        # Verificar que root.after não foi chamado ainda (buffer < 5)
        self.gui.root.after.assert_not_called()
        
        # Adicionar 5º lead (deve chamar root.after)
        self.gui.atualizar_progresso_thread_safe(lead, 0.5)
        
        # Verificar que root.after foi chamado uma vez
        self.gui.root.after.assert_called_once()
        
        # Resetar mock para próximo teste
        self.gui.root.after.reset_mock()
        
        # Testar que progresso 100% força atualização mesmo com buffer < 5
        self.gui.atualizar_progresso_thread_safe(lead, 1.0)
        self.gui.root.after.assert_called_once()
    
    def test_atualizar_ui(self):
        """Testa atualização da UI com novo lead."""
        # Preparar dados de teste
        lead = {
            "nome": "Empresa Teste",
            "telefone": "(11) 1234-5678",
            "site": "www.teste.com",
            "nota": "4.5",
            "comentarios": "100",
            "endereco": "Rua Teste, 123"
        }
        progresso = 0.5
        
        # Configurar mock da tabela
        self.gui.data_table.insert = Mock()
        
        # Executar atualização
        self.gui._atualizar_ui(lead, progresso)
        
        # Verificar atualizações
        self.gui.progress_bar.set.assert_called_with(0.5)
        self.gui.data_table.insert.assert_called_once()
        self.gui.status_label.configure.assert_called()
        self.assertEqual(len(self.gui.leads_data), 1)
    
    def test_parar_extracao(self):
        """Testa parada da extração."""
        # Configurar stop_flag
        self.gui.stop_flag = threading.Event()
        
        # Executar parada
        with patch('error_logger.ErrorLogger'):
            self.gui.parar_extracao()
        
        # Verificar que stop_flag foi setado
        self.assertTrue(self.gui.stop_flag.is_set())
        
        # Verificar que botão foi desabilitado
        self.gui.btn_parar.configure.assert_called_with(state="disabled")
        
        # Verificar que status foi atualizado
        self.gui.status_label.configure.assert_called_with(text="Parando extração...")
    
    @patch('gui_manager.messagebox')
    def test_exportar_dados_sem_dados(self, mock_messagebox):
        """Testa exportação sem dados disponíveis."""
        # Garantir que não há dados
        self.gui.leads_data = []
        
        # Executar exportação
        with patch('error_logger.ErrorLogger'):
            self.gui.exportar_dados()
        
        # Verificar que warning foi exibido
        mock_messagebox.showwarning.assert_called_once()
    
    @patch('gui_manager.filedialog')
    @patch('gui_manager.messagebox')
    @patch('data_exporter.DataExporter')
    def test_exportar_dados_excel(self, mock_exporter_class, mock_messagebox, mock_filedialog):
        """Testa exportação para Excel."""
        # Preparar dados
        self.gui.leads_data = [
            {
                "Nome": "Empresa 1",
                "Telefone": "(11) 1111-1111",
                "Site": "www.empresa1.com",
                "Nota": "4.5",
                "Comentários": "100",
                "Endereço": "Rua 1, 123"
            }
        ]
        
        # Configurar mocks
        mock_messagebox.askquestion.return_value = 'yes'  # Escolher Excel
        mock_filedialog.asksaveasfilename.return_value = '/tmp/test.xlsx'
        
        mock_exporter = Mock()
        mock_exporter.exportar_excel.return_value = True
        mock_exporter_class.return_value = mock_exporter
        
        # Executar exportação
        with patch('error_logger.ErrorLogger'):
            self.gui.exportar_dados()
        
        # Verificar que exporter foi criado e chamado
        mock_exporter_class.assert_called_once_with(self.gui.leads_data)
        mock_exporter.exportar_excel.assert_called_once_with('/tmp/test.xlsx')
        mock_messagebox.showinfo.assert_called_once()
    
    @patch('gui_manager.filedialog')
    @patch('gui_manager.messagebox')
    @patch('data_exporter.DataExporter')
    def test_exportar_dados_csv(self, mock_exporter_class, mock_messagebox, mock_filedialog):
        """Testa exportação para CSV."""
        # Preparar dados
        self.gui.leads_data = [
            {
                "Nome": "Empresa 1",
                "Telefone": "(11) 1111-1111",
                "Site": "www.empresa1.com",
                "Nota": "4.5",
                "Comentários": "100",
                "Endereço": "Rua 1, 123"
            }
        ]
        
        # Configurar mocks
        mock_messagebox.askquestion.return_value = 'no'  # Escolher CSV
        mock_filedialog.asksaveasfilename.return_value = '/tmp/test.csv'
        
        mock_exporter = Mock()
        mock_exporter.exportar_csv.return_value = True
        mock_exporter_class.return_value = mock_exporter
        
        # Executar exportação
        with patch('error_logger.ErrorLogger'):
            self.gui.exportar_dados()
        
        # Verificar que exporter foi criado e chamado
        mock_exporter_class.assert_called_once_with(self.gui.leads_data)
        mock_exporter.exportar_csv.assert_called_once_with('/tmp/test.csv')
        mock_messagebox.showinfo.assert_called_once()


if __name__ == '__main__':
    unittest.main()
