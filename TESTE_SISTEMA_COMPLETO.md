# 🧪 Teste Completo do Sistema de Entrega Automática

## 📋 Pré-requisitos

Antes de testar, certifique-se de que:

1. ✅ O arquivo ZIP foi criado (`npm run prepare-download`)
2. ✅ O email foi configurado no `webhook-handler.js`
3. ✅ Os 3 servidores estão rodando

## 🚀 Passo 1: Preparar o Arquivo ZIP

```bash
cd landing-page
npm run prepare-download
```

**Resultado esperado:**
```
✅ Arquivo ZIP criado com sucesso!
📦 Tamanho: X.XX MB
📍 Local: C:\Users\kaike\Downloads\AP@\landing-page\downloads\lead-extractor.zip
```

**Verificar:**
- Vá até `landing-page/downloads/`
- Confirme que o arquivo `lead-extractor.zip` existe
- Tente abrir o ZIP para verificar se contém os arquivos Python

## 🔧 Passo 2: Configurar Email

Edite `landing-page/webhook-handler.js`:

**Linhas 16-22:**
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

**Linha 82:**
```javascript
from: '"Lead Extractor" <seu-email@gmail.com>',  // ← COLOQUE SEU EMAIL AQUI
```

**Como obter senha de app do Gmail:**
1. Acesse: https://myaccount.google.com/security
2. Ative a verificação em 2 etapas
3. Vá em "Senhas de app"
4. Gere uma senha para "Email"
5. Copie e cole no código

## 🚀 Passo 3: Rodar os 3 Servidores

### Terminal 1 - Frontend
```bash
cd landing-page
npm run dev
```
**Porta:** 5173  
**URL:** http://localhost:5173

### Terminal 2 - Backend API
```bash
cd landing-page
npm run server
```
**Porta:** 3001  
**Logs esperados:**
```
🚀 Servidor rodando em http://localhost:3001
```

### Terminal 3 - Webhook Handler
```bash
cd landing-page
npm run webhook
```
**Porta:** 3002  
**Logs esperados:**
```
🚀 Webhook Handler rodando em http://localhost:3002
📧 Configure seu email em webhook-handler.js (linhas 16-22)
🔗 URL do webhook: http://localhost:3002/webhook/sigilopay
```

## 🧪 Passo 4: Testar o Webhook (Simulação)

Abra um **4º terminal** e execute:

```bash
curl -X POST http://localhost:3002/webhook/sigilopay -H "Content-Type: application/json" -d "{\"event\":\"payment.approved\",\"transactionId\":\"test-123\",\"status\":\"APPROVED\",\"customer\":{\"email\":\"seu-email@teste.com\",\"name\":\"Teste\"},\"paidAt\":\"2024-03-20T10:00:00Z\"}"
```

**Substitua `seu-email@teste.com` pelo seu email real!**

### O que deve acontecer:

1. **No Terminal 3 (Webhook Handler):**
```
📥 Webhook recebido da SigiloPay: {...}
✅ Pagamento aprovado: test-123
📧 Email enviado para: seu-email@teste.com
```

2. **No seu email:**
- Você deve receber um email com o assunto: "🎉 Seu Lead Extractor está pronto para download!"
- O email contém um botão "📥 BAIXAR LEAD EXTRACTOR"

3. **Clicar no link:**
- O download do arquivo `lead-extractor.zip` deve iniciar automaticamente

## 🌐 Passo 5: Testar Fluxo Completo (Com Pagamento Real)

### Opção A: Teste com PIX (Recomendado)

1. **Acesse a landing page:**
   ```
   http://localhost:5173
   ```

2. **Clique em "Comprar Agora"**

3. **Preencha os dados:**
   - Nome: Seu nome
   - Email: Seu email real
   - CPF: Seu CPF
   - Telefone: Seu telefone

4. **Escolha PIX**

5. **QR Code aparece:**
   - Copie o código PIX ou escaneie o QR Code
   - Faça o pagamento (R$ 297,00)

6. **Aguarde confirmação:**
   - A SigiloPay confirma o pagamento (pode demorar alguns segundos)
   - O webhook recebe a notificação
   - Email é enviado automaticamente

7. **Verifique seu email:**
   - Você deve receber o email com o link de download
   - Clique no link
   - Baixe o arquivo ZIP

### Opção B: Configurar Webhook com ngrok (Para Teste Real)

Para que a SigiloPay consiga enviar notificações para seu localhost:

1. **Instale o ngrok:**
```bash
npm install -g ngrok
```

2. **Execute o ngrok:**
```bash
ngrok http 3002
```

3. **Copie a URL gerada:**
```
Forwarding: https://abc123.ngrok.io -> http://localhost:3002
```

4. **Configure na SigiloPay:**
   - Acesse: https://app.sigilopay.com.br
   - Vá em Configurações → Webhooks
   - URL: `https://abc123.ngrok.io/webhook/sigilopay`
   - Eventos: Marque "payment.approved"
   - Salve

5. **Faça um pagamento de teste:**
   - Acesse a landing page
   - Faça um pagamento via PIX
   - Aguarde a confirmação
   - Verifique se o email chegou

## ✅ Checklist de Verificação

### Antes do Teste:
- [ ] Arquivo ZIP criado em `landing-page/downloads/lead-extractor.zip`
- [ ] Email configurado no `webhook-handler.js`
- [ ] Senha de app do Gmail configurada
- [ ] 3 servidores rodando (frontend, backend, webhook)

### Durante o Teste:
- [ ] Webhook recebe a notificação (logs no Terminal 3)
- [ ] Email é enviado (logs mostram "Email enviado para...")
- [ ] Email chega na caixa de entrada (verificar spam também)
- [ ] Link de download funciona
- [ ] Arquivo ZIP é baixado corretamente

### Após o Teste:
- [ ] Arquivo ZIP contém todos os arquivos Python
- [ ] Arquivo ZIP pode ser descompactado
- [ ] Instruções estão incluídas (INSTRUCOES.md)

## 🐛 Problemas Comuns

### Email não chega

**Verificar:**
1. Email e senha de app estão corretos no código
2. Verificação em 2 etapas está ativa no Gmail
3. Pasta de spam
4. Logs do webhook handler mostram "Email enviado"

**Solução:**
- Teste com outro email
- Verifique as credenciais do Gmail
- Use outro provedor de email (SendGrid, Mailgun)

### Webhook não recebe notificação

**Verificar:**
1. Webhook handler está rodando (Terminal 3)
2. URL do webhook está correta na SigiloPay
3. ngrok está rodando (se estiver usando)

**Solução:**
- Verifique os logs do webhook handler
- Teste com curl (simulação manual)
- Confirme a URL no painel da SigiloPay

### Download não funciona

**Verificar:**
1. Arquivo ZIP existe em `landing-page/downloads/`
2. Token é válido
3. Não atingiu o limite de 3 downloads

**Solução:**
- Execute `npm run prepare-download` novamente
- Verifique os logs do webhook handler
- Teste o link diretamente no navegador

### Arquivo ZIP está vazio

**Verificar:**
1. Arquivos Python existem em `lead-extractor-app/`
2. Script `prepare-download.js` executou sem erros

**Solução:**
- Execute `npm run prepare-download` novamente
- Verifique os logs do script
- Confirme que os arquivos Python estão na pasta correta

## 📊 Logs Esperados

### Terminal 1 (Frontend):
```
VITE v5.x.x  ready in XXX ms
➜  Local:   http://localhost:5173/
```

### Terminal 2 (Backend API):
```
🚀 Servidor rodando em http://localhost:3001
📥 Recebendo requisição PIX: {...}
📤 Enviando para SigiloPay: {...}
📥 Resposta da SigiloPay: {...}
✅ Pagamento PIX criado com sucesso
```

### Terminal 3 (Webhook Handler):
```
🚀 Webhook Handler rodando em http://localhost:3002
📥 Webhook recebido da SigiloPay: {...}
✅ Pagamento aprovado: test-123
📧 Email enviado para: cliente@email.com
```

## 🎯 Teste de Sucesso

O teste é considerado bem-sucedido quando:

1. ✅ Cliente paga via PIX
2. ✅ SigiloPay confirma o pagamento
3. ✅ Webhook recebe a notificação
4. ✅ Email é enviado automaticamente
5. ✅ Cliente recebe o email
6. ✅ Cliente clica no link
7. ✅ Arquivo ZIP é baixado
8. ✅ Cliente descompacta e instala o Lead Extractor

## 🎉 Pronto!

Se todos os passos funcionaram, seu sistema de entrega automática está 100% operacional!

**Próximos passos:**
1. Fazer deploy em produção
2. Configurar webhook com URL de produção
3. Testar com clientes reais

---

**Dúvidas?** Consulte o `GUIA_COMPLETO_ENTREGA.md` para mais detalhes.
