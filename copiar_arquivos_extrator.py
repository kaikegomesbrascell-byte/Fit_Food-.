import shutil
import os

# Criar pasta se não existir
os.makedirs("lead-extractor-app", exist_ok=True)

# Lista de arquivos para copiar
arquivos = [
    "main.py",
    "automation_engine.py",
    "gui_manager.py",
    "data_exporter.py",
    "error_logger.py",
    "models.py",
    "requirements.txt",
    "whatsapp_sender.py"
]

print("Copiando arquivos do extrator...")
for arquivo in arquivos:
    if os.path.exists(arquivo):
        shutil.copy2(arquivo, f"lead-extractor-app/{arquivo}")
        print(f"✓ {arquivo}")
    else:
        print(f"✗ {arquivo} não encontrado")

print("\n✅ Arquivos copiados para lead-extractor-app/")
