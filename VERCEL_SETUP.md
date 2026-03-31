# ⚡ Setup Rápido na Vercel

## Passo 1: Fazer Merge da Branch

```bash
# Mudar para a branch main
git checkout main

# Fazer merge da branch com as correções
git merge blackboxai/pix-qr-fix

# Push para o GitHub
git push origin main
```

## Passo 2: Configurar Variáveis de Ambiente na Vercel

1. Acesse: https://vercel.com/seu-projeto/settings/environment-variables

2. Adicione estas variáveis (uma por vez):

| Nome | Valor |
|------|-------|
| `VITE_SUPABASE_URL` | Sua URL do Supabase |
| `VITE_SUPABASE_ANON_KEY` | Sua chave anônima do Supabase |
| `SUPABASE_SERVICE_ROLE_KEY` | Sua chave de serviço do Supabase |
| `SIGILOPAY_PUBLIC_KEY` | Sua chave pública do SigiloPay |
| `SIGILOPAY_SECRET_KEY` | Sua chave secreta do SigiloPay |

**Importante:** Copie os valores do seu arquivo `.env` local.

3. Marque todas as variáveis para: **Production**, **Preview**, e **Development**

## Passo 3: Fazer Redeploy

1. Vá para: https://vercel.com/seu-projeto/deployments
2. Clique nos 3 pontinhos do último deploy
3. Clique em "Redeploy"
4. Aguarde o deploy completar

## Passo 4: Testar

1. Acesse seu site: `https://seu-projeto.vercel.app`
2. Clique em "Começar Agora - R$ 1.000"
3. Preencha os dados:
   - Nome: Teste
   - Email: teste@teste.com
   - CPF: 123.456.789-00
   - Telefone: (11) 99999-9999
4. Clique em "Continuar para Pagamento"
5. Clique em "PIX"
6. Verifique se o QR Code aparece ✅

## ✅ Pronto!

Agora seu site funciona 100% na nuvem, sem precisar rodar backend local!

## 🔍 Como Verificar se Está Funcionando

### Ver Logs da Função Serverless

1. Acesse: https://vercel.com/seu-projeto/logs
2. Filtre por: `/api/payment-pix`
3. Você verá os logs em tempo real quando alguém tentar fazer um pagamento

### Testar a API Diretamente

```bash
curl -X POST https://seu-projeto.vercel.app/api/payment-pix \
  -H "Content-Type: application/json" \
  -d '{
    "identifier": "test-123",
    "amount": 1000,
    "client": {
      "name": "Teste",
      "email": "teste@teste.com",
      "document": "12345678900"
    },
    "expiresIn": 3600
  }'
```

## 🚨 Troubleshooting

### Erro: "Failed to fetch"
- Verifique se as variáveis de ambiente foram salvas
- Faça um novo deploy após adicionar as variáveis

### Erro: "Module not found: axios"
- A Vercel instala automaticamente as dependências de `api/package.json`
- Verifique se o arquivo `api/package.json` existe no repositório

### Erro: "SigiloPay API error"
- Verifique se as credenciais SigiloPay estão corretas nas variáveis de ambiente
- Teste as credenciais diretamente na API SigiloPay

## 📱 Suporte

Se tiver problemas, verifique:
1. Logs da Vercel: https://vercel.com/seu-projeto/logs
2. Console do navegador (F12)
3. Network tab para ver as requisições
