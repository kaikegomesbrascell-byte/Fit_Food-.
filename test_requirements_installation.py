"""
Test script para validar instalação do requirements.txt
Verifica se todas as dependências podem ser importadas corretamente.
"""

import sys
import subprocess


def test_imports():
    """Testa se todos os módulos necessários podem ser importados."""
    print("=" * 60)
    print("TESTE DE IMPORTAÇÃO DE DEPENDÊNCIAS")
    print("=" * 60)
    
    modules_to_test = [
        ("playwright", "Playwright - Automação de navegador"),
        ("customtkinter", "CustomTkinter - Interface gráfica"),
        ("pandas", "Pandas - Manipulação de dados"),
        ("openpyxl", "OpenPyXL - Exportação Excel"),
        ("psutil", "PSUtil - Monitoramento de sistema"),
    ]
    
    all_passed = True
    
    for module_name, description in modules_to_test:
        try:
            __import__(module_name)
            print(f"✓ {description}: OK")
        except ImportError as e:
            print(f"✗ {description}: FALHOU - {e}")
            all_passed = False
    
    print("=" * 60)
    
    if all_passed:
        print("✓ TODOS OS MÓDULOS FORAM IMPORTADOS COM SUCESSO!")
        return True
    else:
        print("✗ ALGUNS MÓDULOS FALHARAM NA IMPORTAÇÃO")
        return False


def check_versions():
    """Verifica as versões instaladas das dependências."""
    print("\n" + "=" * 60)
    print("VERSÕES INSTALADAS")
    print("=" * 60)
    
    packages = [
        "playwright",
        "customtkinter",
        "pandas",
        "openpyxl",
        "psutil"
    ]
    
    for package in packages:
        try:
            result = subprocess.run(
                [sys.executable, "-m", "pip", "show", package],
                capture_output=True,
                text=True,
                check=True
            )
            # Extrair versão da saída
            for line in result.stdout.split('\n'):
                if line.startswith('Version:'):
                    version = line.split(':', 1)[1].strip()
                    print(f"{package}: {version}")
                    break
        except subprocess.CalledProcessError:
            print(f"{package}: NÃO INSTALADO")
    
    print("=" * 60)


if __name__ == "__main__":
    print("\nValidando instalação do requirements.txt...\n")
    
    # Testar importações
    imports_ok = test_imports()
    
    # Verificar versões
    check_versions()
    
    # Resultado final
    print("\n" + "=" * 60)
    if imports_ok:
        print("RESULTADO: ✓ VALIDAÇÃO BEM-SUCEDIDA")
        print("=" * 60)
        sys.exit(0)
    else:
        print("RESULTADO: ✗ VALIDAÇÃO FALHOU")
        print("=" * 60)
        sys.exit(1)
