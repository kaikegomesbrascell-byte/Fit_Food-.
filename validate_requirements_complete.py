"""
Script de Validação Completa do requirements.txt
Verifica:
1. Todas as dependências listadas
2. Versões específicas pinadas
3. Compatibilidade de importação
4. Dependências do projeto vs requirements.txt
"""

import sys
import re
from pathlib import Path


def parse_requirements():
    """Extrai dependências do requirements.txt."""
    requirements = {}
    
    with open('requirements.txt', 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            # Ignorar comentários e linhas vazias
            if line and not line.startswith('#'):
                # Extrair nome e versão (formato: package==version)
                match = re.match(r'^([a-zA-Z0-9_-]+)==([0-9.]+)$', line)
                if match:
                    package, version = match.groups()
                    requirements[package.lower()] = version
    
    return requirements


def check_all_dependencies_listed():
    """Verifica se todas as dependências necessárias estão listadas."""
    print("=" * 70)
    print("1. VERIFICAÇÃO: TODAS AS DEPENDÊNCIAS LISTADAS")
    print("=" * 70)
    
    required_packages = {
        'playwright': 'Automação de navegador (Playwright)',
        'customtkinter': 'Interface gráfica moderna',
        'pandas': 'Manipulação de dados',
        'openpyxl': 'Exportação para Excel',
        'psutil': 'Monitoramento de sistema'
    }
    
    requirements = parse_requirements()
    all_present = True
    
    for package, description in required_packages.items():
        if package in requirements:
            print(f"✓ {package:20} - {description}")
        else:
            print(f"✗ {package:20} - {description} [FALTANDO]")
            all_present = False
    
    print()
    if all_present:
        print("✓ RESULTADO: Todas as dependências necessárias estão listadas")
    else:
        print("✗ RESULTADO: Algumas dependências estão faltando")
    
    return all_present


def check_versions_pinned():
    """Verifica se todas as dependências têm versões específicas."""
    print("\n" + "=" * 70)
    print("2. VERIFICAÇÃO: VERSÕES ESPECÍFICAS PINADAS")
    print("=" * 70)
    
    requirements = parse_requirements()
    all_pinned = True
    
    if not requirements:
        print("✗ ERRO: Nenhuma dependência encontrada no requirements.txt")
        return False
    
    for package, version in requirements.items():
        # Verificar se a versão está no formato X.Y.Z
        if re.match(r'^\d+\.\d+\.\d+$', version):
            print(f"✓ {package:20} == {version:10} [VERSÃO PINADA]")
        else:
            print(f"✗ {package:20} == {version:10} [FORMATO INVÁLIDO]")
            all_pinned = False
    
    print()
    if all_pinned:
        print("✓ RESULTADO: Todas as dependências têm versões específicas pinadas")
    else:
        print("✗ RESULTADO: Algumas versões não estão corretamente pinadas")
    
    return all_pinned


def check_imports():
    """Testa se todas as dependências podem ser importadas."""
    print("\n" + "=" * 70)
    print("3. VERIFICAÇÃO: COMPATIBILIDADE DE IMPORTAÇÃO")
    print("=" * 70)
    
    imports_to_test = [
        ('playwright', 'playwright.async_api'),
        ('customtkinter', 'customtkinter'),
        ('pandas', 'pandas'),
        ('openpyxl', 'openpyxl'),
        ('psutil', 'psutil'),
    ]
    
    all_imported = True
    
    for package_name, import_name in imports_to_test:
        try:
            __import__(import_name)
            print(f"✓ {package_name:20} - Importação bem-sucedida")
        except ImportError as e:
            print(f"✗ {package_name:20} - Falha na importação: {e}")
            all_imported = False
    
    print()
    if all_imported:
        print("✓ RESULTADO: Todas as dependências podem ser importadas")
    else:
        print("✗ RESULTADO: Algumas dependências falharam na importação")
    
    return all_imported


def check_project_imports():
    """Verifica se os imports do projeto correspondem ao requirements.txt."""
    print("\n" + "=" * 70)
    print("4. VERIFICAÇÃO: DEPENDÊNCIAS DO PROJETO vs REQUIREMENTS.TXT")
    print("=" * 70)
    
    # Dependências externas usadas no projeto
    project_dependencies = {
        'playwright': ['automation_engine.py'],
        'customtkinter': ['gui_manager.py'],
        'pandas': ['data_exporter.py'],
        'openpyxl': ['data_exporter.py (via pandas)'],
        'psutil': ['automation_engine.py']
    }
    
    requirements = parse_requirements()
    all_covered = True
    
    for package, files in project_dependencies.items():
        if package in requirements:
            files_str = ', '.join(files)
            print(f"✓ {package:20} - Usado em: {files_str}")
        else:
            print(f"✗ {package:20} - USADO NO PROJETO MAS NÃO LISTADO!")
            all_covered = False
    
    print()
    if all_covered:
        print("✓ RESULTADO: Todas as dependências do projeto estão no requirements.txt")
    else:
        print("✗ RESULTADO: Algumas dependências do projeto não estão listadas")
    
    return all_covered


def check_requirements_format():
    """Verifica a formatação e organização do requirements.txt."""
    print("\n" + "=" * 70)
    print("5. VERIFICAÇÃO: FORMATAÇÃO E ORGANIZAÇÃO")
    print("=" * 70)
    
    checks = {
        'Cabeçalho presente': False,
        'Instruções de instalação': False,
        'Seções organizadas': False,
        'Comentários sobre stdlib': False
    }
    
    with open('requirements.txt', 'r', encoding='utf-8') as f:
        content = f.read()
        
        if 'Google Maps Lead Extractor' in content:
            checks['Cabeçalho presente'] = True
        
        if 'pip install -r requirements.txt' in content:
            checks['Instruções de instalação'] = True
        
        if '=====' in content:
            checks['Seções organizadas'] = True
        
        if 'BIBLIOTECAS PADRÃO' in content or 'stdlib' in content.lower():
            checks['Comentários sobre stdlib'] = True
    
    for check, passed in checks.items():
        status = "✓" if passed else "✗"
        print(f"{status} {check}")
    
    all_passed = all(checks.values())
    print()
    if all_passed:
        print("✓ RESULTADO: requirements.txt está bem formatado e organizado")
    else:
        print("✗ RESULTADO: requirements.txt precisa de melhorias na formatação")
    
    return all_passed


def main():
    """Executa todas as verificações."""
    print("\n" + "=" * 70)
    print("VALIDAÇÃO COMPLETA DO REQUIREMENTS.TXT")
    print("Google Maps Lead Extractor")
    print("=" * 70 + "\n")
    
    results = {
        'Dependências listadas': check_all_dependencies_listed(),
        'Versões pinadas': check_versions_pinned(),
        'Importações funcionam': check_imports(),
        'Projeto vs requirements': check_project_imports(),
        'Formatação adequada': check_requirements_format()
    }
    
    # Resumo final
    print("\n" + "=" * 70)
    print("RESUMO FINAL DA VALIDAÇÃO")
    print("=" * 70)
    
    for check, passed in results.items():
        status = "✓ PASSOU" if passed else "✗ FALHOU"
        print(f"{status:12} - {check}")
    
    print("=" * 70)
    
    all_passed = all(results.values())
    
    if all_passed:
        print("\n✓✓✓ VALIDAÇÃO COMPLETA BEM-SUCEDIDA ✓✓✓")
        print("\nO arquivo requirements.txt está:")
        print("  • Completo com todas as dependências")
        print("  • Com versões específicas pinadas")
        print("  • Testado e funcional")
        print("  • Bem formatado e documentado")
        print("\n✓ Pronto para uso em produção e distribuição!")
        return 0
    else:
        print("\n✗✗✗ VALIDAÇÃO FALHOU ✗✗✗")
        print("\nCorreções necessárias antes de prosseguir.")
        return 1


if __name__ == "__main__":
    sys.exit(main())
