"""
Testes para o LicenseValidator
"""

from license_validator import LicenseValidator
from datetime import datetime, timedelta
import json
import os


def test_validar_licenca_valida():
    """Testa validação de licença válida"""
    print("\n=== Teste 1: Licença Válida ===")
    validator = LicenseValidator("license.key")
    is_valid, mensagem = validator.validar_licenca()
    print(f"Resultado: {is_valid}")
    print(f"Mensagem: {mensagem}")
    print(f"Status: {validator.obter_status_licenca()}")
    assert is_valid == True, "Licença deveria ser válida"
    print("✓ Teste passou")


def test_validar_licenca_expirada():
    """Testa validação de licença expirada"""
    print("\n=== Teste 2: Licença Expirada ===")
    
    # Criar arquivo de licença expirada
    license_data = {
        "api_key": "GMLE-TEST-0000-0000-0002",
        "expiration_date": "2020-01-01",
        "customer_name": "Cliente Teste Expirado",
        "license_type": "commercial"
    }
    
    with open("license_expired.key", "w", encoding="utf-8") as f:
        json.dump(license_data, f, indent=4)
    
    try:
        validator = LicenseValidator("license_expired.key")
        is_valid, mensagem = validator.validar_licenca()
        print(f"Resultado: {is_valid}")
        print(f"Mensagem: {mensagem}")
        print(f"Status: {validator.obter_status_licenca()}")
        assert is_valid == False, "Licença deveria estar expirada"
        assert "expirada" in mensagem.lower(), "Mensagem deveria indicar expiração"
        print("✓ Teste passou")
    finally:
        # Limpar arquivo de teste
        if os.path.exists("license_expired.key"):
            os.remove("license_expired.key")


def test_validar_api_key_invalida():
    """Testa validação de chave de API inválida"""
    print("\n=== Teste 3: API Key Inválida ===")
    
    # Criar arquivo com API key inválida
    license_data = {
        "api_key": "INVALID-KEY",
        "expiration_date": "2026-12-31",
        "customer_name": "Cliente Teste",
        "license_type": "commercial"
    }
    
    with open("license_invalid_key.key", "w", encoding="utf-8") as f:
        json.dump(license_data, f, indent=4)
    
    try:
        validator = LicenseValidator("license_invalid_key.key")
        is_valid, mensagem = validator.validar_licenca()
        print(f"Resultado: {is_valid}")
        print(f"Mensagem: {mensagem}")
        print(f"Status: {validator.obter_status_licenca()}")
        assert is_valid == False, "Licença deveria ser inválida"
        assert "inválida" in mensagem.lower(), "Mensagem deveria indicar chave inválida"
        print("✓ Teste passou")
    finally:
        # Limpar arquivo de teste
        if os.path.exists("license_invalid_key.key"):
            os.remove("license_invalid_key.key")


def test_arquivo_nao_encontrado():
    """Testa comportamento quando arquivo não existe"""
    print("\n=== Teste 4: Arquivo Não Encontrado ===")
    validator = LicenseValidator("arquivo_inexistente.key")
    is_valid, mensagem = validator.validar_licenca()
    print(f"Resultado: {is_valid}")
    print(f"Mensagem: {mensagem}")
    print(f"Status: {validator.obter_status_licenca()}")
    assert is_valid == False, "Licença deveria ser inválida"
    assert "não encontrado" in mensagem.lower(), "Mensagem deveria indicar arquivo não encontrado"
    print("✓ Teste passou")


def test_json_invalido():
    """Testa comportamento com JSON inválido"""
    print("\n=== Teste 5: JSON Inválido ===")
    
    # Criar arquivo com JSON inválido
    with open("license_invalid_json.key", "w", encoding="utf-8") as f:
        f.write("{ invalid json content }")
    
    try:
        validator = LicenseValidator("license_invalid_json.key")
        is_valid, mensagem = validator.validar_licenca()
        print(f"Resultado: {is_valid}")
        print(f"Mensagem: {mensagem}")
        print(f"Status: {validator.obter_status_licenca()}")
        assert is_valid == False, "Licença deveria ser inválida"
        assert "json" in mensagem.lower(), "Mensagem deveria indicar erro de JSON"
        print("✓ Teste passou")
    finally:
        # Limpar arquivo de teste
        if os.path.exists("license_invalid_json.key"):
            os.remove("license_invalid_json.key")


def test_campos_faltando():
    """Testa comportamento quando campos obrigatórios estão faltando"""
    print("\n=== Teste 6: Campos Faltando ===")
    
    # Criar arquivo sem campo api_key
    license_data = {
        "expiration_date": "2025-12-31",
        "customer_name": "Cliente Teste"
    }
    
    with open("license_missing_fields.key", "w", encoding="utf-8") as f:
        json.dump(license_data, f, indent=4)
    
    try:
        validator = LicenseValidator("license_missing_fields.key")
        is_valid, mensagem = validator.validar_licenca()
        print(f"Resultado: {is_valid}")
        print(f"Mensagem: {mensagem}")
        print(f"Status: {validator.obter_status_licenca()}")
        assert is_valid == False, "Licença deveria ser inválida"
        assert "api_key" in mensagem.lower(), "Mensagem deveria indicar campo faltando"
        print("✓ Teste passou")
    finally:
        # Limpar arquivo de teste
        if os.path.exists("license_missing_fields.key"):
            os.remove("license_missing_fields.key")


def test_formato_api_key():
    """Testa validação de diferentes formatos de API key"""
    print("\n=== Teste 7: Formatos de API Key ===")
    
    test_cases = [
        ("GMLE-ABCD-1234-EFGH-5678", True, "Formato válido padrão"),
        ("GMLE-0000-0000-0000-0000", True, "Formato válido com zeros"),
        ("GMLE-ZZZZ-9999-AAAA-BBBB", True, "Formato válido alfanumérico"),
        ("gmle-abcd-1234-efgh-5678", False, "Minúsculas (inválido)"),
        ("GMLE-ABC-1234-EFGH-5678", False, "Grupo com 3 caracteres (inválido)"),
        ("GMLE-ABCD-1234-EFGH", False, "Faltando um grupo (inválido)"),
        ("TEST-ABCD-1234-EFGH-5678", False, "Prefixo errado (inválido)"),
        ("", False, "String vazia (inválido)"),
    ]
    
    for api_key, expected_valid, descricao in test_cases:
        validator = LicenseValidator()
        validator.api_key = api_key
        result = validator.verificar_api_key()
        status = "✓" if result == expected_valid else "✗"
        print(f"{status} {descricao}: '{api_key}' -> {result}")
        assert result == expected_valid, f"Falhou para: {descricao}"
    
    print("✓ Todos os testes de formato passaram")


def test_verificar_expiracao():
    """Testa verificação de expiração diretamente"""
    print("\n=== Teste 8: Verificação de Expiração ===")
    
    validator = LicenseValidator()
    
    # Teste com data futura
    validator.expiration_date = datetime.now() + timedelta(days=30)
    assert validator.verificar_expiracao() == True, "Data futura deveria ser válida"
    print("✓ Data futura: válida")
    
    # Teste com data passada
    validator.expiration_date = datetime.now() - timedelta(days=30)
    assert validator.verificar_expiracao() == False, "Data passada deveria ser inválida"
    print("✓ Data passada: inválida")
    
    # Teste com data None
    validator.expiration_date = None
    assert validator.verificar_expiracao() == False, "Data None deveria ser inválida"
    print("✓ Data None: inválida")
    
    print("✓ Todos os testes de expiração passaram")


if __name__ == "__main__":
    print("=" * 60)
    print("TESTES DO LICENSE VALIDATOR")
    print("=" * 60)
    
    try:
        test_validar_licenca_valida()
        test_validar_licenca_expirada()
        test_validar_api_key_invalida()
        test_arquivo_nao_encontrado()
        test_json_invalido()
        test_campos_faltando()
        test_formato_api_key()
        test_verificar_expiracao()
        
        print("\n" + "=" * 60)
        print("✓ TODOS OS TESTES PASSARAM COM SUCESSO!")
        print("=" * 60)
    except AssertionError as e:
        print(f"\n✗ TESTE FALHOU: {e}")
        exit(1)
    except Exception as e:
        print(f"\n✗ ERRO INESPERADO: {e}")
        import traceback
        traceback.print_exc()
        exit(1)
