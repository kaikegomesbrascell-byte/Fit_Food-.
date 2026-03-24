"""
Script de teste para validar a estrutura da GUI (Tasks 8.1-8.5)
"""

from gui_manager import LeadExtractorGUI


def test_gui_structure():
    """Testa a criação da estrutura da GUI."""
    print("Iniciando teste da estrutura da GUI...")
    
    # Criar instância da GUI
    gui = LeadExtractorGUI()
    
    # Verificar atributos inicializados
    assert gui.root is not None, "Janela principal não foi criada"
    assert gui.extraction_thread is None, "Thread deve ser None inicialmente"
    assert gui.stop_flag is not None, "Stop flag não foi criado"
    assert gui.leads_data == [], "Lista de leads deve estar vazia"
    
    print("✓ Atributos inicializados corretamente")
    
    # Criar interface
    gui.criar_interface()
    
    # Verificar widgets de inputs
    assert gui.nicho_entry is not None, "Entry de nicho não foi criado"
    assert gui.localizacao_entry is not None, "Entry de localização não foi criado"
    assert gui.limite_slider is not None, "Slider de limite não foi criado"
    assert gui.limite_label is not None, "Label de limite não foi criado"
    
    print("✓ Seção de inputs criada corretamente")
    
    # Verificar widgets de controles
    assert gui.btn_iniciar is not None, "Botão Iniciar não foi criado"
    assert gui.btn_parar is not None, "Botão Parar não foi criado"
    assert gui.btn_exportar is not None, "Botão Exportar não foi criado"
    assert str(gui.btn_parar.cget("state")) == "disabled", "Botão Parar deve estar desabilitado"
    
    print("✓ Seção de controles criada corretamente")
    
    # Verificar widgets de progresso
    assert gui.progress_bar is not None, "Barra de progresso não foi criada"
    assert gui.status_label is not None, "Label de status não foi criado"
    assert gui.progress_bar.get() == 0, "Barra de progresso deve estar em 0"
    
    print("✓ Seção de progresso criada corretamente")
    
    # Verificar tabela de dados
    assert gui.data_table is not None, "Tabela de dados não foi criada"
    colunas = gui.data_table["columns"]
    assert len(colunas) == 6, "Tabela deve ter 6 colunas"
    assert "Nome" in colunas, "Coluna Nome não encontrada"
    assert "Telefone" in colunas, "Coluna Telefone não encontrada"
    assert "Site" in colunas, "Coluna Site não encontrada"
    assert "Nota" in colunas, "Coluna Nota não encontrada"
    assert "Comentários" in colunas, "Coluna Comentários não encontrada"
    assert "Endereço" in colunas, "Coluna Endereço não encontrada"
    
    print("✓ Tabela de dados criada corretamente")
    
    # Testar atualização do label do slider
    gui.limite_slider.set(1)  # Valor 100
    gui._atualizar_label_limite(1)
    assert "100 leads" in gui.limite_label.cget("text"), "Label do slider não atualizado corretamente"
    
    gui.limite_slider.set(2)  # Valor 500
    gui._atualizar_label_limite(2)
    assert "500 leads" in gui.limite_label.cget("text"), "Label do slider não atualizado corretamente"
    
    print("✓ Atualização do slider funcionando corretamente")
    
    print("\n✅ Todos os testes passaram! A estrutura da GUI está correta.")
    print("\nPara visualizar a GUI, execute:")
    print("  python -c \"from gui_manager import LeadExtractorGUI; gui = LeadExtractorGUI(); gui.criar_interface(); gui.run()\"")
    
    # Fechar janela
    gui.root.destroy()


if __name__ == "__main__":
    test_gui_structure()
