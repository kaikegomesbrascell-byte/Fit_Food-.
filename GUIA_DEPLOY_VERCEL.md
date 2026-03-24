# 🚀 Guia Completo - Deploy no Vercel

## 📋 Visão Geral

Este guia mostra como fazer deploy da landing page no Vercel e configurar o backend.

## ⚠️ IMPORTANTE: Estrutura do Deploy

O Vercel é ideal para o **frontend (landing page)**, mas o **backend (server.js e webhook-handler.js)** precisa ser hospedado em outro lugar.

### O que vai para o Vercel:
- ✅ Landing page (frontend React)
- ✅ Página de download
- ✅ Assets estáticos

### O que NÃO vai para o Vercel:
- ❌ server.js (Backend API de pagamentos)
- ❌ webhook-handler.js (Sistema de entrega)
- ❌ downloads/ (Arquivo ZIP com executável)

## 🔧 Parte 1: Preparar o Projeto

### 1. Criar repositório no GitHub

1. Acesse: https://github.com/new
2. Nome do repositório: `leadextract-landing`
3. Descrição: "Landing page profissional para LeadExtract"
4. Visibilidade: **Private** (recomendado)
5. Clique em "Create repository"

### 2. Inicializar Git no projeto

Abra o terminal na pasta `landing-page`:

```bash
cd landing-page
git init
git add .
git commit -m "Initial commit: LeadExtract landing page"
```

### 3. Conectar ao GitHub

```bash
git remote add origin https://github.com/SEU-USUARIO/leadextract-landing.git
git branch -M main
git push -u origin main
```

**Substitua `SEU-USUARIO` pelo seu usuário do GitHub!**

## 🌐 Parte 2: Deploy no Vercel

### 1. Criar conta no Vercel

1. Acesse: https://vercel.com/signup
2. Faça login com sua conta do GitHub
3. Autorize o Vercel a acessar seus repositórios

### 2. Importar projeto

1. No dashboard do Vercel, clique em "Add New..."
2. Selecione "Project"
3. Clique em "Import" no repositório `leadextract-landing`

### 3. Configurar o projeto

**Framework Preset:** Vite  
**Root Directory:** `./` (deixe vazio ou use `./`)  
**Build Command:** `npm run build`  
**Output Directory:** `dist`  
**Install Command:** `npm install`

### 4. Variáveis de Ambiente (Opcional)

Se você tiver variáveis de ambiente, adicione aqui:

- `VITE_API_URL` - URL do backend (ex: `https://api.seudominio.com`)
- `VITE_WEBHOOK_URL` - URL do webhook (ex: `https://webhook.seudominio.com`)

### 5. Deploy

Clique em "Deploy" e aguarde (~2-3 minutos).

Quando concluir, você terá uma URL como:
```
https://leadextract-landing.vercel.app
```

## 🖥️ Parte 3: Deploy do Backend

O backend (server.js e webhook-handler.js) precisa ser hospedado em um serviço que suporte Node.js.

### Opções de Hospedagem para Backend:

#### Opção 1: Railway (Recomendado - Fácil)

1. Acesse: https://railway.app
2. Faça login com GitHub
3. Clique em "New Project"
4. Selecione "Deploy from GitHub repo"
5. Escolha seu repositório
6. Configure:
   - **Start Command:** `node server.js` (para API) ou `node webhook-handler.js` (para webhook)
   - **Port:** 3001 (API) ou 3002 (webhook)

#### Opção 2: Render

1. Acesse: https://render.com
2. Faça login com GitHub
3. Clique em "New +"
4. Selecione "Web Service"
5. Conecte seu repositório
6. Configure:
   - **Build Command:** `npm install`
   - **Start Command:** `node server.js`
   - **Port:** 3001

#### Opção 3: Heroku

1. Acesse: https://heroku.com
2. Crie um app
3. Conecte ao GitHub
4. Configure variáveis de ambiente
5. Deploy

#### Opção 4: DigitalOcean App Platform

1. Acesse: https://cloud.digitalocean.com/apps
2. Crie um novo app
3. Conecte ao GitHub
4. Configure e deploy

### Estrutura Recomendada:

```
Frontend (Vercel):
https://leadextract.vercel.app

Backend API (Railway):
https://leadextract-api.railway.app

Webhook Handler (Railway):
https://leadextract-webhook.railway.app
```

## 🔗 Parte 4: Conectar Frontend e Backend

### 1. Atualizar URLs no Frontend

Edite os arquivos que fazem chamadas à API:

**src/components/CheckoutModal.tsx** (ou onde estiver a chamada de pagamento):
```typescript
// Trocar de:
const response = await fetch('http://localhost:3001/api/payment/pix', {

// Para:
const response = await fetch('https://leadextract-api.railway.app/api/payment/pix', {
```

**src/pages/Download.tsx**:
```typescript
// Trocar de:
fetch(`http://localhost:3002/api/download/verify/${token}`)

// Para:
fetch(`https://leadextract-webhook.railway.app/api/download/verify/${token}`)
```

### 2. Atualizar CORS no Backend

Edite `server.js` e `webhook-handler.js`:

```javascript
// Trocar de:
app.use(cors());

// Para:
app.use(cors({
  origin: [
    'https://leadextract.vercel.app',
    'http://localhost:5173'  // Para desenvolvimento
  ],
  credentials: true
}));
```

### 3. Fazer commit e push

```bash
git add .
git commit -m "Update API URLs for production"
git push
```

O Vercel vai fazer deploy automático!

## 🔐 Parte 5: Configurar Webhook na SigiloPay

1. Acesse: https://app.sigilopay.com.br
2. Vá em **Configurações → Webhooks**
3. Configure:
   - **URL:** `https://leadextract-webhook.railway.app/webhook/sigilopay`
   - **Eventos:** Marque "payment.approved"
4. Salve

## 📦 Parte 6: Hospedar o Arquivo ZIP

O arquivo `lead-extractor.zip` precisa estar acessível para download.

### Opções:

#### Opção 1: AWS S3 (Recomendado)

1. Crie um bucket no S3
2. Faça upload do ZIP
3. Configure permissões públicas
4. Use a URL do S3 no webhook handler

#### Opção 2: Cloudflare R2

1. Crie um bucket no R2
2. Faça upload do ZIP
3. Configure URL pública

#### Opção 3: Servidor próprio

1. Hospede o ZIP no mesmo servidor do webhook
2. Sirva via Express

**Atualizar webhook-handler.js:**
```javascript
const filePath = 'https://seu-bucket.s3.amazonaws.com/lead-extractor.zip';
```

## 🧪 Parte 7: Testar em Produção

### 1. Testar Landing Page

Acesse: `https://leadextract.vercel.app`

Verifique:
- ✅ Página carrega corretamente
- ✅ Design está responsivo
- ✅ Botões funcionam

### 2. Testar Pagamento

1. Clique em "Comprar"
2. Preencha os dados
3. Escolha PIX
4. Verifique se o QR Code aparece

### 3. Testar Webhook

1. Faça um pagamento de teste
2. Verifique se o email chega
3. Clique no link do email
4. Verifique se a página de download abre
5. Baixe o arquivo

## 📊 Parte 8: Monitoramento

### Vercel

- Dashboard: https://vercel.com/dashboard
- Logs: Clique no projeto → "Deployments" → "View Function Logs"
- Analytics: Aba "Analytics"

### Railway/Render

- Dashboard: Acesse o projeto
- Logs: Aba "Logs"
- Métricas: Aba "Metrics"

## 🔒 Parte 9: Segurança

### Variáveis de Ambiente

**No Vercel:**
1. Vá em Settings → Environment Variables
2. Adicione:
   - `VITE_API_URL`
   - `VITE_WEBHOOK_URL`

**No Railway/Render:**
1. Vá em Settings → Environment Variables
2. Adicione:
   - `EMAIL_USER`
   - `EMAIL_PASS`
   - `SIGILOPAY_PUBLIC_KEY`
   - `SIGILOPAY_SECRET_KEY`

### HTTPS

- ✅ Vercel fornece HTTPS automático
- ✅ Railway fornece HTTPS automático
- ✅ Render fornece HTTPS automático

## 🎯 Checklist Final

### Frontend (Vercel):
- [ ] Repositório no GitHub criado
- [ ] Projeto importado no Vercel
- [ ] Deploy concluído com sucesso
- [ ] URLs da API atualizadas
- [ ] Landing page acessível

### Backend (Railway/Render):
- [ ] server.js deployado
- [ ] webhook-handler.js deployado
- [ ] CORS configurado
- [ ] Variáveis de ambiente configuradas
- [ ] Endpoints acessíveis

### Integração:
- [ ] Frontend conectado ao backend
- [ ] Webhook configurado na SigiloPay
- [ ] Arquivo ZIP hospedado
- [ ] Email configurado
- [ ] Fluxo completo testado

## 🐛 Problemas Comuns

### Deploy falha no Vercel

**Erro:** "Build failed"

**Solução:**
- Verifique os logs de build
- Confirme que `npm run build` funciona localmente
- Verifique se todas as dependências estão no package.json

### CORS Error

**Erro:** "Access to fetch blocked by CORS policy"

**Solução:**
- Configure CORS no backend
- Adicione a URL do Vercel na lista de origens permitidas

### Webhook não recebe notificações

**Erro:** SigiloPay não envia notificações

**Solução:**
- Verifique a URL do webhook na SigiloPay
- Confirme que o servidor está rodando
- Verifique os logs do webhook handler

## 🎉 Pronto!

Agora seu sistema está em produção:

- ✅ Landing page no Vercel
- ✅ Backend no Railway/Render
- ✅ Webhook configurado
- ✅ Sistema de entrega funcionando

**URLs de Produção:**
- Landing Page: `https://leadextract.vercel.app`
- API: `https://leadextract-api.railway.app`
- Webhook: `https://leadextract-webhook.railway.app`

---

**Próximos passos:**
1. Configurar domínio personalizado (opcional)
2. Adicionar analytics (Google Analytics, Hotjar)
3. Configurar email marketing
4. Monitorar vendas e conversões
