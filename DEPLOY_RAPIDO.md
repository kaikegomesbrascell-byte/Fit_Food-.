# ⚡ Deploy Rápido - Comandos Essenciais

## 🚀 Passo a Passo Rápido

### 1. Preparar o projeto

```bash
cd landing-page
```

### 2. Inicializar Git (se ainda não fez)

```bash
git init
git add .
git commit -m "Initial commit: LeadExtract landing page"
```

### 3. Criar repositório no GitHub

1. Acesse: https://github.com/new
2. Nome: `leadextract-landing`
3. Visibilidade: Private
4. Clique em "Create repository"

### 4. Conectar ao GitHub

```bash
git remote add origin https://github.com/SEU-USUARIO/leadextract-landing.git
git branch -M main
git push -u origin main
```

**⚠️ Troque `SEU-USUARIO` pelo seu usuário do GitHub!**

### 5. Deploy no Vercel

1. Acesse: https://vercel.com/new
2. Faça login com GitHub
3. Clique em "Import" no repositório `leadextract-landing`
4. Configure:
   - Framework: **Vite**
   - Build Command: `npm run build`
   - Output Directory: `dist`
5. Clique em "Deploy"

### 6. Aguarde o deploy (~2-3 minutos)

Você receberá uma URL como:
```
https://leadextract-landing.vercel.app
```

## 🎯 Próximos Passos

### Backend (server.js e webhook-handler.js)

O backend precisa ser hospedado separadamente. Recomendo:

**Railway (Mais fácil):**
1. Acesse: https://railway.app
2. Faça login com GitHub
3. Clique em "New Project"
4. Selecione seu repositório
5. Configure e deploy

**Ou use:**
- Render: https://render.com
- Heroku: https://heroku.com
- DigitalOcean: https://digitalocean.com

### Atualizar URLs

Depois de fazer deploy do backend, atualize as URLs no código:

**src/pages/Download.tsx:**
```typescript
// Linha ~15
fetch(`https://SEU-BACKEND.railway.app/api/download/verify/${token}`)
```

**src/components/CheckoutModal.tsx** (se existir):
```typescript
fetch('https://SEU-BACKEND.railway.app/api/payment/pix', {
```

### Fazer novo deploy

```bash
git add .
git commit -m "Update API URLs for production"
git push
```

O Vercel faz deploy automático!

## ✅ Checklist Rápido

- [ ] Repositório no GitHub criado
- [ ] Código enviado para o GitHub
- [ ] Deploy no Vercel concluído
- [ ] Backend deployado (Railway/Render)
- [ ] URLs atualizadas no código
- [ ] Novo deploy feito
- [ ] Webhook configurado na SigiloPay
- [ ] Testado em produção

## 🐛 Problemas?

Consulte o arquivo `GUIA_DEPLOY_VERCEL.md` para instruções detalhadas.

---

**Dúvidas?** Entre em contato!
