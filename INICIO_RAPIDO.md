# 🚀 Início Rápido - 5 Minutos

## 1️⃣ Configurar Ambiente Local (2 min)

### Windows
```cmd
REM Seu .env já existe! Não precisa copiar
REM Para ver o conteúdo:
type .env
```

### Linux/Mac
```bash
# Copiar arquivo de exemplo (se necessário)
cp .env.example .env

# Editar com suas credenciais
nano .env
```

**Preencha com suas credenciais reais:**
- Supabase: https://app.supabase.com/project/seu-projeto/settings/api
- SigiloPay: https://app.sigilopay.com.br (painel de API)

## 2️⃣ Testar Localmente (1 min)

### Windows
```cmd
REM Abrir no navegador
start index.html

REM Ou usar servidor local
npx serve .
```

### Linux/Mac
```bash
# Abrir no navegador
open index.html  # Mac
xdg-open index.html  # Linux

# Ou usar servidor local
npx serve .
```

Acesse: http://localhost:3000

## 3️⃣ Deploy na Vercel (2 min)

### Opção A: Via GitHub (Recomendado)

```bash
# 1. Commitar código
git add .
git commit -m "Setup inicial"
git push origin main

# 2. Conectar na Vercel
# Acesse: https://vercel.com/new
# Selecione seu repositório
# Clique em "Import"
```

### Opção B: Via CLI

```bash
# 1. Instalar Vercel CLI
npm i -g vercel

# 2. Fazer login
vercel login

# 3. Deploy
vercel
```

## 4️⃣ Configurar Variáveis na Vercel

1. Acesse: https://vercel.com/seu-projeto/settings/environment-variables

2. Adicione cada variável:
   - `VITE_SUPABASE_URL`
   - `VITE_SUPABASE_ANON_KEY`
   - `SUPABASE_SERVICE_ROLE_KEY`
   - `SIGILOPAY_PUBLIC_KEY`
   - `SIGILOPAY_SECRET_KEY`

3. Marque para: Production, Preview, Development

4. Clique em "Save"

## 5️⃣ Redeploy

```bash
# Via CLI
vercel --prod

# Ou via Dashboard
# Deployments → ... → Redeploy
```

## ✅ Pronto!

Seu site está no ar: `https://seu-projeto.vercel.app`

## 🧪 Testar

1. Acesse a landing page
2. Clique em "Quero Emagrecer Agora"
3. Preencha o formulário
4. Clique em "Finalizar Compra"
5. Verifique se o QR Code PIX aparece

## 🐛 Problemas?

### QR Code não aparece
```bash
# Ver logs da Vercel
vercel logs

# Ou no dashboard
# https://vercel.com/seu-projeto/logs
```

### Erro de CORS
- Verifique se as variáveis de ambiente foram salvas
- Faça um novo deploy após adicionar variáveis

### Vídeo não carrega
- Confirme que o arquivo .mp4 foi commitado
- Verifique o tamanho do arquivo (max 100MB no GitHub)

## 📚 Documentação Completa

- [README.md](./README.md) - Visão geral
- [COMO_FAZER_DEPLOY.md](./COMO_FAZER_DEPLOY.md) - Deploy detalhado
- [SEGURANCA.md](./SEGURANCA.md) - Proteção de credenciais
- [VERCEL_SETUP.md](./VERCEL_SETUP.md) - Setup Vercel
- [SIGILOPAY_API_DOCS.md](./SIGILOPAY_API_DOCS.md) - API de pagamento

## 🆘 Precisa de Ajuda?

1. Verifique os logs: `vercel logs`
2. Consulte a documentação acima
3. Verifique o console do navegador (F12)

---

⚡ **Tempo total: ~5 minutos**
