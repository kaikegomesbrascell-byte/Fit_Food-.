"""
Script de demonstração visual da GUI (Tasks 8.1-8.5)
Execute este script para visualizar a interface gráfica criada.
"""

from gui_manager import LeadExtractorGUI


def main():
    """Demonstra a GUI criada nas Tasks 8.1-8.5."""
    print("=" * 60)
    print("Google Maps Lead Extractor - Demonstração da GUI")
    print("=" * 60)
    print("\nTasks implementadas:")
    print("  ✓ 8.1: Classe LeadExtractorGUI com inicialização")
    print("  ✓ 8.2: Seção de Inputs (nicho, localização, limite)")
    print("  ✓ 8.3: Seção de Controles (botões)")
    print("  ✓ 8.4: Seção de Progresso (barra e status)")
    print("  ✓ 8.5: Tabela de Dados (Treeview)")
    print("\nAbrindo interface gráfica...")
    print("Feche a janela para encerrar.\n")
    
    # Criar e executar GUI
    gui = LeadExtractorGUI()
    gui.criar_interface()
    gui.run()


if __name__ == "__main__":
    main()
