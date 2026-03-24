# 🚀 Guia Completo - Sistema de Entrega Automática

## 📋 Visão Geral

Este sistema permite que, após o pagamento ser confirmado pela SigiloPay, o cliente receba automaticamente um email com o link para baixar o Lead Extractor.

## 🔧 Passo 1: Instalar Dependências

```bash
cd landing-page
npm install
```

Isso vai instalar:
- `archiver` - Para criar arquivos ZIP
- `nodemailer` - Para enviar emails
- Outras dependências já existentes

## 📦 Passo 2: Preparar o Arquivo ZIP

Execute o script para criar o arquivo ZIP com todos os arquivos do Lead Extractor:

```bash
npm run prepare-download
```

Isso vai:
- Criar a pasta `landing-page/downloads/`
- Gerar o arquivo `lead-extractor.zip` com todos os arquivos Python
- Incluir README com instruções de instalação

**Resultado esperado:**
```
✅ Arquivo ZIP criado com sucesso!
📦 Tamanho: X.XX MB
📍 Local: C:\Users\...\landing-page\downloads\lead-extractor.zip
```

## 📧 Passo 3: Configurar Email

Edite o arquivo `webhook-handler.js` (linhas 16-22):

```javascript
const transporter = nodemailer.createTransport({
  host: 'smtp.gmail.com',
  port: 587,
  secure: false,
  auth: {
    user: 'seu-email@gmail.com',     // ← COLOQUE SEU EMAIL AQUI
    pass: 'sua-senha-app',            // ← COLOQUE SUA SENHA DE APP AQUI
  },
});
```

### Como obter senha de app do Gmail:

1. Acesse: https://myaccount.google.com/security
2. Ative a **verificação em 2 etapas** (obrigatório)
3. Vá em **Senhas de app**
4. Selecione "Email" como app
5. Copie a senha gerada (16 caracteres)
6. Cole no campo `pass` do código

**Também atualize a linha 82:**
```javascript
from: '"Lead Extractor" <seu-email@gmail.com>',  // ← COLOQUE SEU EMAIL AQUI
```

## 🌐 Passo 4: Configurar Webhook na SigiloPay

### Para Desenvolvimento (Localhost)

1. **Instale o ngrok** (para expor localhost):
```bash
npm install -g ngrok
```

2. **Inicie o webhook handler**:
```bash
npm run webhook
```

3. **Em outro terminal, inicie o ngrok**:
```bash
ngrok http 3002
```

4. **Copie a URL gerada** (exemplo: `https://abc123.ngrok.io`)

5. **Configure no painel da SigiloPay**:
   - Acesse: https://app.sigilopay.com.br
   - Vá em **Configurações → Webhooks**
   - URL do webhook: `https://abc123.ngrok.io/webhook/sigilopay`
   - Eventos: Marque **payment.approved**
   - Salve

### Para Produção

1. **Faça deploy do webhook handler** em:
   - Heroku: https://heroku.com
   - Railway: https://railway.app
   - Render: https://render.com
   - DigitalOcean: https://digitalocean.com

2. **Configure a URL de produção** na SigiloPay:
   - URL: `https://seu-dominio.com/webhook/sigilopay`

## 🚀 Passo 5: Rodar os Servidores

Você precisa rodar **3 servidores** em terminais separados:

### Terminal 1 - Frontend (Vite)
```bash
cd landing-page
npm run dev
```
- Porta: 5173 (padrão do Vite)
- Acesse: http://localhost:5173

### Terminal 2 - Backend API (Pagamentos)
```bash
cd landing-page
npm run server
```
- Porta: 3001
- Processa pagamentos PIX e cartão

### Terminal 3 - Webhook Handler (Entrega)
```bash
cd landing-page
npm run webhook
```
- Porta: 3002
- Recebe notificações da SigiloPay
- Envia emails com link de download

## 🔄 Fluxo Completo

```
1. Cliente acessa landing page
   ↓
2. Cliente clica em "Comprar"
   ↓
3. Modal de checkout abre
   ↓
4. Cliente preenche dados (nome, email, CPF, telefone)
   ↓
5. Cliente escolhe PIX
   ↓
6. QR Code é gerado (via server.js → SigiloPay API)
   ↓
7. Cliente paga via PIX
   ↓
8. SigiloPay confirma pagamento
   ↓
9. SigiloPay envia webhook para http://seu-dominio.com/webhook/sigilopay
   ↓
10. webhook-handler.js recebe notificação
   ↓
11. Sistema gera token de download único
   ↓
12. Sistema envia email para o cliente
   ↓
13. Cliente recebe email com link de download
   ↓
14. Cliente clica no link
   ↓
15. Sistema verifica token e limite de downloads
   ↓
16. Cliente baixa o arquivo lead-extractor.zip
   ↓
17. Cliente descompacta e instala o Lead Extractor
```

## 🧪 Passo 6: Testar o Sistema

### Teste 1: Verificar se os servidores estão rodando

```bash
# Testar webhook handler
curl http://localhost:3002/health
```

**Resposta esperada:**
```json
{
  "status": "ok",
  "message": "Webhook handler está rodando",
  "pagamentosAprovados": 0,
  "tokensAtivos": 0
}
```

### Teste 2: Simular webhook da SigiloPay

```bash
curl -X POST http://localhost:3002/webhook/sigilopay \
  -H "Content-Type: application/json" \
  -d '{
    "event": "payment.approved",
    "transactionId": "test-123",
    "status": "APPROVED",
    "customer": {
      "email": "seu-email@teste.com",
      "name": "Teste"
    },
    "paidAt": "2024-03-20T10:00:00Z"
  }'
```

**O que deve acontecer:**
1. Webhook handler recebe a notificação
2. Gera token de download
3. Envia email para `seu-email@teste.com`
4. Você recebe o email com o link de download

### Teste 3: Testar download

1. Abra o email recebido
2. Clique no link de download
3. O arquivo `lead-extractor.zip` deve ser baixado

Ou teste diretamente no navegador:
```
http://localhost:3002/api/download/[TOKEN]
```

## 📁 Estrutura de Arquivos

```
landing-page/
├── server.js                    # Backend API (pagamentos)
├── webhook-handler.js           # Webhook handler (entrega)
├── prepare-download.js          # Script para criar ZIP
├── downloads/
│   └── lead-extractor.zip      # Arquivo para download
├── package.json                 # Dependências
└── GUIA_COMPLETO_ENTREGA.md    # Este arquivo

lead-extractor-app/
├── main.py                      # Arquivo principal do extrator
├── automation_engine.py         # Motor de automação
├── gui_manager.py              # Interface gráfica
├── data_exporter.py            # Exportador de dados
├── error_logger.py             # Sistema de logs
├── models.py                   # Modelos de dados
├── whatsapp_sender.py          # Envio de WhatsApp
├── requirements.txt            # Dependências Python
└── README.md                   # Instruções
```

## 🐛 Solução de Problemas

### Email não está sendo enviado

**Problema:** Email não chega na caixa de entrada

**Soluções:**
1. Verifique se configurou o email e senha de app corretamente
2. Confirme que a verificação em 2 etapas está ativa no Gmail
3. Verifique a pasta de spam
4. Teste com outro provedor de email (SendGrid, Mailgun)

### Webhook não está sendo recebido

**Problema:** SigiloPay não está enviando notificações

**Soluções:**
1. Verifique se o webhook handler está rodando (`npm run webhook`)
2. Confirme a URL do webhook na SigiloPay
3. Use ngrok para expor localhost em desenvolvimento
4. Verifique os logs do webhook handler no terminal

### Download não funciona

**Problema:** Link de download retorna erro

**Soluções:**
1. Confirme que o arquivo ZIP foi criado (`npm run prepare-download`)
2. Verifique se o arquivo existe em `landing-page/downloads/lead-extractor.zip`
3. Confirme que o token é válido
4. Verifique se não atingiu o limite de 3 downloads

### Arquivo ZIP está vazio ou incompleto

**Problema:** ZIP não contém todos os arquivos

**Soluções:**
1. Execute novamente: `npm run prepare-download`
2. Verifique se todos os arquivos Python existem em `lead-extractor-app/`
3. Verifique os logs do script de preparação

## 🔒 Segurança

### Recomendações para Produção:

1. **Use HTTPS** em produção (obrigatório)
2. **Valide assinatura do webhook** da SigiloPay
3. **Limite downloads por token** (já implementado: 3 downloads)
4. **Adicione expiração aos tokens** (ex: 7 dias)
5. **Use banco de dados** ao invés de Map em memória
6. **Implemente rate limiting** para evitar abuso
7. **Use variáveis de ambiente** para credenciais

### Exemplo de .env:

```env
PORT=3002
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USER=seu-email@gmail.com
EMAIL_PASS=sua-senha-app
DOWNLOAD_URL=https://seu-dominio.com
SIGILOPAY_WEBHOOK_SECRET=sua-chave-secreta
```

## 📊 Monitoramento

### Logs do Webhook Handler

O webhook handler registra todos os eventos no console:

```
📥 Webhook recebido da SigiloPay: {...}
✅ Pagamento aprovado: test-123
📧 Email enviado para: cliente@email.com
📦 Download iniciado: cliente@email.com (1/3)
✅ Download concluído: cliente@email.com
```

### Endpoints de Monitoramento

```bash
# Status do webhook handler
GET http://localhost:3002/health

# Status de um pagamento específico
GET http://localhost:3002/api/payment/status/[transactionId]
```

## 🎯 Próximos Passos

1. ✅ Instalar dependências (`npm install`)
2. ✅ Preparar arquivo ZIP (`npm run prepare-download`)
3. ✅ Configurar email no `webhook-handler.js`
4. ✅ Rodar os 3 servidores
5. ✅ Configurar webhook na SigiloPay
6. ✅ Testar fluxo completo
7. ✅ Fazer deploy em produção

## 📞 Suporte

Se tiver problemas:
1. Verifique os logs no terminal
2. Consulte a seção "Solução de Problemas"
3. Entre em contato com o suporte

---

**Versão**: 1.0.0  
**Última Atualização**: ${new Date().toLocaleDateString('pt-BR')}
