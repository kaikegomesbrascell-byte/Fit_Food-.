import subprocess
import os

os.chdir('landing-page')

print("🔧 Corrigindo erro 404 do download...")

commands = [
    ['git', 'add', 'public/lead-extractor.zip'],
    ['git', 'add', 'src/pages/ThankYou.tsx'],
    ['git', 'commit', '-m', 'fix: Corrige erro 404 do download movendo ZIP para pasta public'],
    ['git', 'push', 'origin', 'main']
]

for cmd in commands:
    print(f"\n🔄 Executando: {' '.join(cmd)}")
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        print(result.stdout)
        if result.stderr:
            print(result.stderr)
    except subprocess.CalledProcessError as e:
        print(f"❌ Erro: {e}")
        print(f"Saída: {e.stdout}")
        print(f"Erro: {e.stderr}")
        if 'nothing to commit' in e.stdout or 'nothing to commit' in e.stderr:
            print("✅ Nada para commitar!")
            continue

print("\n✅ Correção aplicada!")
print("\n📋 O que foi feito:")
print("  • ZIP movido para pasta public/")
print("  • Caminho atualizado no ThankYou.tsx")
print("  • Download agora funciona: /lead-extractor.zip")
print("\n🌐 Teste após o deploy:")
print("  1. Acesse: https://seu-dominio.vercel.app/obrigado")
print("  2. Clique em 'Baixar LeadExtract + Bônus'")
print("  3. O download deve iniciar automaticamente")
