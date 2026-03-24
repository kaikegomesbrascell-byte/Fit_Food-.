import subprocess
import os

os.chdir('landing-page')

print("🔍 Verificando status do Git...")

result = subprocess.run(['git', 'status'], capture_output=True, text=True)
print(result.stdout)

print("\n📝 Últimos commits:")
result = subprocess.run(['git', 'log', '--oneline', '-5'], capture_output=True, text=True)
print(result.stdout)
