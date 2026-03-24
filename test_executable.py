"""
Script de teste para validar o executável do Lead Extractor.
Testa se o executável pode ser iniciado e se os arquivos necessários estão presentes.
"""

import subprocess
import os
import sys
import time

def test_executable_exists():
    """Verifica se o executável foi criado."""
    exe_path = "dist/LeadExtractor.exe"
    if not os.path.exists(exe_path):
        print(f"❌ FALHA: Executável não encontrado em {exe_path}")
        return False
    
    print(f"✓ Executável encontrado: {exe_path}")
    
    # Verificar tamanho
    size_bytes = os.path.getsize(exe_path)
    size_mb = size_bytes / (1024 * 1024)
    print(f"✓ Tamanho do executável: {size_mb:.2f} MB")
    
    # Verificar se está dentro do limite de 200MB
    if size_mb > 200:
        print(f"⚠ AVISO: Executável maior que 200MB (requisito 9.5)")
    else:
        print(f"✓ Tamanho dentro do limite de 200MB")
    
    return True

def test_license_file_included():
    """Verifica se o arquivo de licença está incluído."""
    if os.path.exists("license.key"):
        print("✓ Arquivo license.key encontrado no diretório raiz")
        return True
    else:
        print("⚠ AVISO: Arquivo license.key não encontrado")
        return False

def test_executable_launch():
    """Tenta iniciar o executável e verifica se ele não trava imediatamente."""
    exe_path = "dist/LeadExtractor.exe"
    print("\n🔄 Testando inicialização do executável...")
    print("   (O executável será iniciado e fechado após 3 segundos)")
    
    try:
        # Iniciar o processo
        process = subprocess.Popen(
            [exe_path],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            creationflags=subprocess.CREATE_NO_WINDOW if sys.platform == 'win32' else 0
        )
        
        # Aguardar 3 segundos
        time.sleep(3)
        
        # Verificar se o processo ainda está rodando
        if process.poll() is None:
            print("✓ Executável iniciou com sucesso e está rodando")
            process.terminate()
            process.wait(timeout=5)
            return True
        else:
            # Processo terminou, verificar código de saída
            stdout, stderr = process.communicate()
            print(f"❌ FALHA: Executável terminou inesperadamente")
            print(f"   Código de saída: {process.returncode}")
            if stderr:
                print(f"   Erro: {stderr.decode('utf-8', errors='ignore')}")
            return False
            
    except Exception as e:
        print(f"❌ FALHA ao iniciar executável: {e}")
        return False

def test_dependencies_check():
    """Verifica se as dependências principais estão no executável."""
    print("\n📦 Verificando dependências incluídas...")
    
    # Verificar se o diretório build contém informações sobre as dependências
    if os.path.exists("build/lead_extractor"):
        print("✓ Diretório de build encontrado")
        
        # Verificar arquivo de warnings
        warn_file = "build/lead_extractor/warn-lead_extractor.txt"
        if os.path.exists(warn_file):
            with open(warn_file, 'r', encoding='utf-8', errors='ignore') as f:
                warnings = f.read()
                if "missing" in warnings.lower() or "not found" in warnings.lower():
                    print("⚠ AVISO: Alguns avisos encontrados no build")
                    print("   Verifique: build/lead_extractor/warn-lead_extractor.txt")
                else:
                    print("✓ Nenhum aviso crítico encontrado")
        
        return True
    else:
        print("⚠ Diretório de build não encontrado")
        return False

def main():
    """Executa todos os testes."""
    print("=" * 60)
    print("TESTE DO EXECUTÁVEL - Google Maps Lead Extractor")
    print("=" * 60)
    print()
    
    results = []
    
    # Teste 1: Verificar se o executável existe
    print("1. Verificando existência do executável...")
    results.append(("Executável existe", test_executable_exists()))
    print()
    
    # Teste 2: Verificar arquivo de licença
    print("2. Verificando arquivo de licença...")
    results.append(("Arquivo de licença", test_license_file_included()))
    print()
    
    # Teste 3: Verificar dependências
    print("3. Verificando dependências...")
    results.append(("Dependências", test_dependencies_check()))
    print()
    
    # Teste 4: Testar inicialização
    print("4. Testando inicialização do executável...")
    results.append(("Inicialização", test_executable_launch()))
    print()
    
    # Resumo
    print("=" * 60)
    print("RESUMO DOS TESTES")
    print("=" * 60)
    
    passed = sum(1 for _, result in results if result)
    total = len(results)
    
    for test_name, result in results:
        status = "✓ PASSOU" if result else "❌ FALHOU"
        print(f"{status}: {test_name}")
    
    print()
    print(f"Total: {passed}/{total} testes passaram")
    
    if passed == total:
        print("\n🎉 SUCESSO: Todos os testes passaram!")
        print("\n✅ O executável está pronto para distribuição")
        print(f"   Localização: dist/LeadExtractor.exe")
        return 0
    else:
        print("\n⚠ ATENÇÃO: Alguns testes falharam")
        print("   Revise os erros acima antes de distribuir")
        return 1

if __name__ == "__main__":
    sys.exit(main())
