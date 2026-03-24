"""
Teste para validar implementação do DataExporter
"""

from data_exporter import DataExporter
import os
import pandas as pd


def test_data_exporter():
    """Testa funcionalidades básicas do DataExporter"""
    
    # Dados de teste
    leads_teste = [
        {
            'Nome': 'Empresa Teste 1',
            'Telefone': '(11) 1234-5678',
            'Site': 'https://exemplo1.com',
            'Nota': '4.5',
            'Comentários': '100',
            'Endereço': 'Rua Teste, 123 - São Paulo'
        },
        {
            'Nome': 'Empresa Teste 2',
            'Telefone': '(21) 9876-5432',
            'Site': 'https://exemplo2.com',
            'Nota': '4.8',
            'Comentários': '250',
            'Endereço': 'Av. Exemplo, 456 - Rio de Janeiro'
        },
        {
            'Nome': 'Empresa Teste 3',
            'Telefone': 'N/A',
            'Site': 'N/A',
            'Nota': '4.2',
            'Comentários': '50',
            'Endereço': 'Praça Central, 789 - Belo Horizonte'
        }
    ]
    
    print("=== Teste do DataExporter ===\n")
    
    # Criar instância do exportador
    print("1. Criando DataExporter...")
    exporter = DataExporter(leads_teste)
    print("   ✓ DataExporter criado com sucesso\n")
    
    # Testar preparação do DataFrame
    print("2. Preparando DataFrame...")
    exporter.preparar_dataframe()
    print(f"   ✓ DataFrame preparado com {len(exporter.df)} registros")
    print(f"   Colunas: {list(exporter.df.columns)}\n")
    
    # Testar exportação para Excel
    print("3. Testando exportação para Excel...")
    excel_path = "test_leads_export.xlsx"
    sucesso_excel = exporter.exportar_excel(excel_path)
    
    if sucesso_excel and os.path.exists(excel_path):
        print(f"   ✓ Excel exportado com sucesso: {excel_path}")
        
        # Verificar conteúdo do Excel
        df_lido = pd.read_excel(excel_path)
        print(f"   ✓ Arquivo contém {len(df_lido)} registros")
    else:
        print("   ✗ Falha ao exportar Excel")
        return False
    
    print()
    
    # Testar exportação para CSV
    print("4. Testando exportação para CSV...")
    csv_path = "test_leads_export.csv"
    sucesso_csv = exporter.exportar_csv(csv_path)
    
    if sucesso_csv and os.path.exists(csv_path):
        print(f"   ✓ CSV exportado com sucesso: {csv_path}")
        
        # Verificar conteúdo do CSV
        df_lido = pd.read_csv(csv_path)
        print(f"   ✓ Arquivo contém {len(df_lido)} registros")
    else:
        print("   ✗ Falha ao exportar CSV")
        return False
    
    print()
    
    # Limpar arquivos de teste
    print("5. Limpando arquivos de teste...")
    try:
        if os.path.exists(excel_path):
            os.remove(excel_path)
        if os.path.exists(csv_path):
            os.remove(csv_path)
        print("   ✓ Arquivos de teste removidos\n")
    except Exception as e:
        print(f"   ! Aviso: Não foi possível remover arquivos de teste: {e}\n")
    
    print("=== Todos os testes passaram com sucesso! ===")
    return True


if __name__ == "__main__":
    try:
        test_data_exporter()
    except Exception as e:
        print(f"\n✗ Erro durante teste: {e}")
        import traceback
        traceback.print_exc()
