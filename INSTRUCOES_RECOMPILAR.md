# 🚀 Instruções para Recompilar o LeadExtractor.exe

## ✅ Correção Implementada

O erro **"Arquivo de licença 'license.key' não encontrado"** foi corrigido!

### O que foi feito:

1. ✅ Atualizado `license_validator.py` para detectar automaticamente o caminho correto do arquivo de licença
2. ✅ Copiado `license.key` para a pasta `lead-extractor-app/`
3. ✅ Atualizado `LeadExtractor.spec` para incluir o arquivo de licença no executável
4. ✅ Criado script de recompilação automática
5. ✅ Atualizado documentação com instruções corretas

## 🔧 Como Recompilar o Executável

### Passo 1: Abrir Terminal

Abra o terminal (CMD ou PowerShell) na pasta `lead-extractor-app`:

```bash
cd lead-extractor-app
```

### Passo 2: Recompilar

**Opção A - Usando o arquivo batch (MAIS FÁCIL):**

```bash
RECOMPILAR_COM_LICENCA.bat
```

**Opção B - Usando o arquivo .spec:**

```bash
pyinstaller LeadExtractor.spec
```

**Opção C - Comando completo do PyInstaller:**

```bash
pyinstaller --onefile --windowed --name="LeadExtractor" --add-data="license.key;." main.py
```

### Passo 3: Localizar o Executável

O novo executável estará em:
```
lead-extractor-app/dist/LeadExtractor.exe
```

### Passo 4: Testar

1. Execute o `LeadExtractor.exe`
2. Preencha os campos (Nicho, Localização, Limite)
3. Clique em **"Iniciar Extração"**
4. Você deve ver a mensagem: **"Licença Válida"** ✅

## 📦 Atualizar o Pacote de Download

Após recompilar e testar, atualize o pacote ZIP:

```bash
python create_zip.py
```

Isso irá:
- Copiar o novo `LeadExtractor.exe` para `landing-page/public/`
- Incluir os PDFs de bônus
- Criar o `lead-extractor.zip` atualizado

## 🌐 Deploy para GitHub

Após atualizar o ZIP, faça o deploy:

```bash
git add .
git commit -m "fix: Corrigido erro de licença no executável"
git push origin main
```

## ✅ Checklist de Verificação

Antes de distribuir para clientes:

- [ ] Recompilei o executável usando um dos métodos acima
- [ ] Testei o executável localmente e a licença foi validada
- [ ] Atualizei o pacote ZIP com `python create_zip.py`
- [ ] Verifiquei que o ZIP contém:
  - `LeadExtractor.exe` (novo, com licença)
  - `BONUS-1-Guia-Anti-Ban-WhatsApp.pdf`
  - `BONUS-2-Scripts-de-Vendas.pdf`
  - `LEIA-ME.txt`
- [ ] Fiz deploy para o GitHub
- [ ] Testei o download da landing page

## 🎯 Resultado Esperado

Após seguir estes passos:

✅ O executável incluirá o arquivo de licença internamente
✅ Funcionará em qualquer computador sem arquivos externos
✅ Não exibirá mais o erro "Arquivo de licença não encontrado"
✅ Validará a licença corretamente ao iniciar extração

## 📝 Notas Importantes

### Tamanho do Executável
- O arquivo .exe terá aproximadamente 150-200MB
- Isso é normal porque inclui Python, bibliotecas e Chromium

### Primeira Execução
- Pode demorar alguns segundos para iniciar
- O Windows pode pedir confirmação de segurança

### Antivírus
- Alguns antivírus podem detectar falso positivo
- Isso é comum com executáveis do PyInstaller
- Adicione exceção no antivírus se necessário

## 🆘 Problemas Comuns

### "pyinstaller não é reconhecido"
**Solução:**
```bash
pip install pyinstaller
```

### "license.key não encontrado" durante compilação
**Solução:**
- Certifique-se de que `license.key` está na pasta `lead-extractor-app/`
- O arquivo já foi copiado pela correção

### Executável não abre
**Solução:**
- Recompile sem `--windowed` para ver o erro:
```bash
pyinstaller --onefile --name="LeadExtractor" --add-data="license.key;." main.py
```

## 📚 Documentação Adicional

- `CORRECAO_LICENCA.md` - Detalhes técnicos da correção
- `COMO_GERAR_EXE.md` - Guia completo de compilação
- `test_license_fix.py` - Script de teste da correção

---

**Pronto para recompilar!** 🚀

Execute `RECOMPILAR_COM_LICENCA.bat` e teste o novo executável.
