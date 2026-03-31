# 🪟 Comandos Windows - Referência Rápida

## 📁 Gerenciamento de Arquivos

### Ver conteúdo de arquivo
```cmd
type arquivo.txt
```

### Copiar arquivo
```cmd
copy origem.txt destino.txt
```

### Mover/Renomear arquivo
```cmd
move origem.txt destino.txt
```

### Deletar arquivo
```cmd
del arquivo.txt
```

### Criar pasta
```cmd
mkdir nome-da-pasta
```

### Listar arquivos
```cmd
dir
```

### Listar arquivos (incluindo ocultos)
```cmd
dir /a
```

## 🔍 Busca e Pesquisa

### Procurar texto em arquivo
```cmd
findstr "texto" arquivo.txt
```

### Procurar texto em múltiplos arquivos
```cmd
findstr /s "texto" *.txt
```

### Procurar arquivo por nome
```cmd
dir /s arquivo.txt
```

## 🌐 Git

### Ver status
```cmd
git status
```

### Adicionar arquivos
```cmd
git add .
```

### Commitar
```cmd
git commit -m "Mensagem"
```

### Push
```cmd
git push origin main
```

### Pull
```cmd
git pull origin main
```

### Ver diferenças
```cmd
git diff
```

### Ver log
```cmd
git log
```

## 📦 Node.js / NPM

### Instalar dependências
```cmd
npm install
```

### Executar script
```cmd
npm run dev
```

### Instalar pacote global
```cmd
npm install -g nome-pacote
```

### Executar com npx
```cmd
npx serve .
```

## 🔐 Variáveis de Ambiente

### Ver variável
```cmd
echo %VARIAVEL%
```

### Definir variável (sessão atual)
```cmd
set VARIAVEL=valor
```

### Ver todas as variáveis
```cmd
set
```

## 🌐 Navegador

### Abrir arquivo no navegador padrão
```cmd
start index.html
```

### Abrir URL
```cmd
start https://google.com
```

## 📝 Editor de Texto

### Abrir no VSCode
```cmd
code arquivo.txt
```

### Abrir no Notepad
```cmd
notepad arquivo.txt
```

### Editar no terminal (básico)
```cmd
edit arquivo.txt
```

## 🔄 Equivalências Linux → Windows

| Linux/Mac | Windows | Descrição |
|-----------|---------|-----------|
| `ls` | `dir` | Listar arquivos |
| `cat arquivo` | `type arquivo` | Ver conteúdo |
| `cp origem destino` | `copy origem destino` | Copiar |
| `mv origem destino` | `move origem destino` | Mover |
| `rm arquivo` | `del arquivo` | Deletar |
| `mkdir pasta` | `mkdir pasta` | Criar pasta |
| `pwd` | `cd` | Ver diretório atual |
| `clear` | `cls` | Limpar tela |
| `grep "texto" arquivo` | `findstr "texto" arquivo` | Buscar texto |
| `touch arquivo` | `type nul > arquivo` | Criar arquivo vazio |
| `chmod +x arquivo` | *(não necessário)* | Tornar executável |

## 🚀 Comandos Específicos do Projeto

### Ver configuração do .env
```cmd
type .env
```

### Verificar se .env está no .gitignore
```cmd
findstr ".env" .gitignore
```

### Ver logs do Git (procurar .env)
```cmd
git log --all --full-history -- .env
```

### Adicionar .env ao .gitignore (se necessário)
```cmd
echo .env >> .gitignore
```

### Verificar o que será commitado
```cmd
git status
git diff --cached
```

### Limpar cache do Git (se .env foi commitado)
```cmd
git rm --cached .env
git commit -m "Remove .env do repositório"
```

## 🔧 PowerShell (Alternativa Moderna)

Se preferir usar PowerShell em vez de CMD:

### Ver conteúdo
```powershell
Get-Content arquivo.txt
# ou
cat arquivo.txt
```

### Copiar arquivo
```powershell
Copy-Item origem.txt destino.txt
# ou
cp origem.txt destino.txt
```

### Listar arquivos
```powershell
Get-ChildItem
# ou
ls
```

### Procurar texto
```powershell
Select-String "texto" arquivo.txt
```

## 💡 Dicas

### 1. Usar PowerShell em vez de CMD
PowerShell é mais moderno e suporta comandos Linux:
```powershell
# Abrir PowerShell
powershell
```

### 2. Instalar Git Bash
Git Bash permite usar comandos Linux no Windows:
- Download: https://git-scm.com/download/win
- Depois pode usar: `cp`, `ls`, `cat`, etc.

### 3. Usar Windows Terminal
Terminal moderno da Microsoft com abas:
- Download: Microsoft Store → "Windows Terminal"

### 4. Atalhos Úteis
- `Tab` - Autocompletar
- `↑` / `↓` - Histórico de comandos
- `Ctrl + C` - Cancelar comando
- `Ctrl + L` ou `cls` - Limpar tela

## 🆘 Problemas Comuns

### 'comando' não é reconhecido
**Causa:** Programa não instalado ou não está no PATH

**Solução:**
1. Instale o programa necessário
2. Ou use o caminho completo: `C:\Program Files\...\programa.exe`

### Permissão negada
**Causa:** Arquivo em uso ou sem permissão

**Solução:**
1. Feche programas que usam o arquivo
2. Execute como Administrador (clique direito → "Executar como administrador")

### Arquivo não encontrado
**Causa:** Caminho errado ou arquivo não existe

**Solução:**
1. Verifique o caminho: `dir`
2. Use caminho completo: `C:\Users\...\arquivo.txt`

---

**Dica:** Para usar comandos Linux no Windows, instale o Git Bash ou use o WSL (Windows Subsystem for Linux)
