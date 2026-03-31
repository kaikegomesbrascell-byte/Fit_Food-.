# 🪟 LEIA PRIMEIRO - Usuário Windows

## ✅ Boa Notícia!

Seu projeto já está configurado e pronto! O arquivo `.env` com suas credenciais já existe.

## 🚀 O Que Fazer Agora (3 Passos)

### 1️⃣ Verificar que está tudo OK
```cmd
REM Ver o .env (suas credenciais)
type .env

REM Verificar proteção do Git
findstr ".env" .gitignore
```

**Resultado esperado:** Deve mostrar `.env` no .gitignore ✅

### 2️⃣ Commitar o Código (SEM o .env)
```cmd
git add .
git commit -m "Landing Page Receitas Fit - Pronta"
git push origin main
```

**Importante:** O `.env` NÃO será incluído (está protegido)

### 3️⃣ Configurar na Vercel

1. Acesse: https://vercel.com/seu-projeto/settings/environment-variables

2. Adicione estas variáveis (copie do seu `.env`):
   ```cmd
   REM Para ver os valores:
   type .env
   ```

3. Variáveis necessárias:
   - `VITE_SUPABASE_URL`
   - `VITE_SUPABASE_ANON_KEY`
   - `SUPABASE_SERVICE_ROLE_KEY`
   - `SIGILOPAY_PUBLIC_KEY` (do painel SigiloPay)
   - `SIGILOPAY_SECRET_KEY` (do painel SigiloPay)

4. Marque: Production, Preview, Development

5. Clique em "Save"

## 🎯 Pronto!

Seu site estará no ar em: `https://seu-projeto.vercel.app`

## 📚 Documentação

### Guias Rápidos
- [SETUP_WINDOWS.md](./SETUP_WINDOWS.md) - Guia específico Windows
- [COMANDOS_WINDOWS.md](./COMANDOS_WINDOWS.md) - Comandos úteis
- [INICIO_RAPIDO.md](./INICIO_RAPIDO.md) - Setup em 5 minutos

### Guias Completos
- [README.md](./README.md) - Visão geral
- [COMO_FAZER_DEPLOY.md](./COMO_FAZER_DEPLOY.md) - Deploy detalhado
- [SEGURANCA.md](./SEGURANCA.md) - Proteção de credenciais

### Referência Técnica
- [SIGILOPAY_API_DOCS.md](./SIGILOPAY_API_DOCS.md) - API de pagamento
- [VERCEL_SETUP.md](./VERCEL_SETUP.md) - Setup Vercel
- [PROJETO_FINAL.md](./PROJETO_FINAL.md) - Visão completa

## ⚠️ Importante: Comandos Windows

No Windows, use estes comandos em vez dos comandos Linux:

| Ação | Linux/Mac | Windows |
|------|-----------|---------|
| Ver arquivo | `cat .env` | `type .env` |
| Copiar | `cp a.txt b.txt` | `copy a.txt b.txt` |
| Listar | `ls` | `dir` |
| Buscar | `grep "texto" arquivo` | `findstr "texto" arquivo` |
| Limpar tela | `clear` | `cls` |

**Dica:** Veja todos os comandos em [COMANDOS_WINDOWS.md](./COMANDOS_WINDOWS.md)

## 🐛 Problemas Comuns

### 'cp' não é reconhecido
**Solução:** Use `copy` em vez de `cp`
```cmd
copy origem.txt destino.txt
```

### 'cat' não é reconhecido
**Solução:** Use `type` em vez de `cat`
```cmd
type arquivo.txt
```

### 'ls' não é reconhecido
**Solução:** Use `dir` em vez de `ls`
```cmd
dir
```

### Quer usar comandos Linux?
**Opção 1:** Instale o Git Bash
- Download: https://git-scm.com/download/win
- Depois pode usar: `cp`, `cat`, `ls`, etc.

**Opção 2:** Use PowerShell
```powershell
# PowerShell suporta alguns comandos Linux
cp arquivo.txt copia.txt
ls
cat arquivo.txt
```

## ✅ Checklist

- [x] `.env` existe com credenciais
- [x] `.env` está protegido no `.gitignore`
- [ ] Código commitado no Git
- [ ] Variáveis configuradas na Vercel
- [ ] Deploy realizado
- [ ] Site testado

## 🆘 Precisa de Ajuda?

### Ver logs
```cmd
REM Logs do Git
git log

REM Status do Git
git status

REM Ver diferenças
git diff
```

### Testar localmente
```cmd
REM Abrir no navegador
start index.html

REM Ou usar servidor
npx serve .
```

### Verificar segurança
```cmd
REM Confirmar que .env não será commitado
git status
REM .env NÃO deve aparecer na lista
```

## 🎉 Tudo Pronto!

Seu projeto está configurado e seguro. Agora é só fazer o deploy!

---

**Próximo passo:** [COMO_FAZER_DEPLOY.md](./COMO_FAZER_DEPLOY.md)
