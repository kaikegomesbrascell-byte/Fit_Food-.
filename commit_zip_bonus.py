import subprocess
import os

os.chdir('landing-page')

print("📦 Commitando ZIP atualizado com bônus...")

commands = [
    ['git', 'add', 'downloads/lead-extractor.zip', '-f'],
    ['git', 'commit', '-m', 'chore: Atualiza ZIP com PDFs bônus (Guia Anti-Ban + Scripts de Vendas)'],
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
            print("✅ ZIP já está atualizado!")
            continue

print("\n✅ ZIP atualizado no GitHub!")
