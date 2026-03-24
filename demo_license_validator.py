"""
Demonstração do LicenseValidator
"""

from license_validator import LicenseValidator


def main():
    print("=" * 60)
    print("DEMONSTRAÇÃO DO LICENSE VALIDATOR")
    print("=" * 60)
    
    # Criar instância do validador
    validator = LicenseValidator("license.key")
    
    print("\n1. Validando licença...")
    is_valid, mensagem = validator.validar_licenca()
    
    print(f"\n   Resultado: {'✓ VÁLIDA' if is_valid else '✗ INVÁLIDA'}")
    print(f"   Mensagem: {mensagem}")
    
    print("\n2. Obtendo status detalhado...")
    status = validator.obter_status_licenca()
    print(f"   {status}")
    
    print("\n3. Informações da licença:")
    print(f"   - Arquivo: {validator.license_file}")
    print(f"   - API Key: {validator.api_key}")
    if validator.expiration_date:
        print(f"   - Data de Expiração: {validator.expiration_date.strftime('%d/%m/%Y')}")
    print(f"   - Válida: {validator.is_valid}")
    
    print("\n" + "=" * 60)
    
    if is_valid:
        print("✓ Licença válida - Sistema pronto para uso!")
    else:
        print("✗ Licença inválida - Acesso bloqueado!")
    
    print("=" * 60)


if __name__ == "__main__":
    main()
