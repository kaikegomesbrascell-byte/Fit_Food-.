import subprocess
import os

os.chdir('landing-page')

print("📦 Fazendo commit final do .gitignore...")

commands = [
    ['git', 'add', '.gitignore'],
    ['git', 'commit', '-m', 'chore: Atualiza .gitignore para permitir distribuição do executável'],
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

print("\n✅ Deploy completo!")
