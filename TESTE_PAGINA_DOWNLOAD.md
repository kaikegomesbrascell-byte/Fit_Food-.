# 🧪 Teste da Página de Download

## 📋 O que foi criado

Uma página de download profissional que:
- ✅ Só é acessível com token válido (enviado por email)
- ✅ Verifica se o pagamento foi aprovado
- ✅ Mostra informações do cliente
- ✅ Exibe downloads restantes (limite de 3)
- ✅ Permite baixar o arquivo ZIP
- ✅ Design moderno e responsivo

## 🚀 Como Testar

### Passo 1: Preparar o arquivo ZIP

```bash
cd landing-page
npm run prepare-download
```

### Passo 2: Rodar os 3 servidores

**Terminal 1 - Frontend:**
```bash
npm run dev
```
Porta: 5173

**Terminal 2 - Backend API:**
```bash
npm run server
```
Porta: 3001

**Terminal 3 - Webhook Handler:**
```bash
npm run webhook
```
Porta: 3002

### Passo 3: Simular pagamento aprovado

Abra um 4º terminal e execute:

```bash
curl -X POST http://localhost:3002/webhook/sigilopay -H "Content-Type: application/json" -d "{\"event\":\"payment.approved\",\"transactionId\":\"test-123\",\"status\":\"APPROVED\",\"customer\":{\"email\":\"seu-email@gmail.com\",\"name\":\"Teste Cliente\"},\"paidAt\":\"2024-03-20T10:00:00Z\"}"
```

**⚠️ IMPORTANTE:** Troque `seu-email@gmail.com` pelo seu email real!

### Passo 4: Verificar o email

1. Abra seu email
2. Procure por: "🎉 Seu Lead Extractor está pronto para download!"
3. Clique no botão "📥 BAIXAR LEAD EXTRACTOR"

### Passo 5: Página de Download

Você será redirecionado para:
```
http://localhost:5173/download?token=XXXXXXXX
```

**O que você verá:**

1. ✅ **Pagamento Confirmado!**
2. 📊 **Informações do Download:**
   - Nome do cliente
   - Email
   - Downloads restantes (3 de 3)
   - Tamanho do arquivo

3. 🟢 **Botão "Baixar Lead Extractor"**
4. 📦 **O que está incluído**
5. 🚀 **Próximos Passos**

### Passo 6: Baixar o arquivo

1. Clique no botão "Baixar Lead Extractor"
2. O arquivo `lead-extractor.zip` será baixado
3. A contagem de downloads será atualizada (2 de 3)

## 🧪 Cenários de Teste

### Teste 1: Token Válido (Sucesso)

**URL:** `http://localhost:5173/download?token=TOKEN_VALIDO`

**Resultado esperado:**
- ✅ Página carrega com sucesso
- ✅ Mostra informações do cliente
- ✅ Botão de download está habilitado
- ✅ Download funciona

### Teste 2: Token Inválido (Erro)

**URL:** `http://localhost:5173/download?token=token-invalido`

**Resultado esperado:**
- ❌ Mensagem: "Link Inválido ou Expirado"
- ❌ Botão de download desabilitado
- ✅ Botão "Voltar para a Página Inicial"

### Teste 3: Limite de Downloads Atingido

**Ação:** Baixe o arquivo 3 vezes

**Resultado esperado:**
- ✅ 1º download: Sucesso (2 de 3 restantes)
- ✅ 2º download: Sucesso (1 de 3 restantes)
- ✅ 3º download: Sucesso (0 de 3 restantes)
- ❌ 4º download: Botão desabilitado

### Teste 4: Sem Token na URL

**URL:** `http://localhost:5173/download`

**Resultado esperado:**
- ❌ Mensagem: "Link Inválido ou Expirado"

## 📧 Formato do Email

O email enviado contém:

```html
Assunto: 🎉 Seu Lead Extractor está pronto para download!

Olá [Nome do Cliente],

Seu pagamento foi confirmado com sucesso! 🎉

Agora você pode baixar o Google Maps Lead Extractor e começar a extrair leads ilimitados.

[BOTÃO: 📥 BAIXAR LEAD EXTRACTOR]

📋 O que você vai receber:
✅ Software completo Lead Extractor
✅ Todos os arquivos necessários
✅ Instruções de instalação
✅ Suporte técnico

⚠️ Importante:
• Este link é válido para 3 downloads
• Guarde este email para referência futura
• Se tiver problemas, entre em contato conosco
```

## 🔗 URLs Importantes

### Desenvolvimento (Localhost):

- **Landing Page:** http://localhost:5173
- **Página de Download:** http://localhost:5173/download?token=XXX
- **Backend API:** http://localhost:3001
- **Webhook Handler:** http://localhost:3002
- **Verificar Token:** http://localhost:3002/api/download/verify/TOKEN
- **Download Direto:** http://localhost:3002/api/download/TOKEN

### Produção:

- **Landing Page:** https://seu-dominio.com
- **Página de Download:** https://seu-dominio.com/download?token=XXX
- **Backend API:** https://api.seu-dominio.com
- **Webhook Handler:** https://webhook.seu-dominio.com

## 🐛 Problemas Comuns

### Página mostra "Link Inválido"

**Causas:**
- Token não existe
- Token já foi usado 3 vezes
- Webhook handler não está rodando

**Solução:**
- Verifique se o webhook handler está rodando
- Simule um novo pagamento para gerar novo token
- Verifique os logs do webhook handler

### Download não inicia

**Causas:**
- Arquivo ZIP não existe
- Caminho do arquivo está incorreto
- Limite de downloads atingido

**Solução:**
- Execute `npm run prepare-download`
- Verifique se o arquivo existe em `landing-page/downloads/`
- Verifique os logs do webhook handler

### Email não chega

**Causas:**
- Email não configurado no webhook-handler.js
- Senha de app incorreta
- Verificação em 2 etapas não ativa

**Solução:**
- Configure o email nas linhas 16-22 e 82
- Obtenha nova senha de app do Gmail
- Ative verificação em 2 etapas

## ✅ Checklist de Teste

### Antes do Teste:
- [ ] Arquivo ZIP criado
- [ ] Email configurado
- [ ] 3 servidores rodando

### Durante o Teste:
- [ ] Webhook recebe notificação
- [ ] Email é enviado
- [ ] Email chega na caixa de entrada
- [ ] Link do email funciona
- [ ] Página de download carrega
- [ ] Informações corretas são exibidas
- [ ] Botão de download funciona
- [ ] Arquivo ZIP é baixado
- [ ] Contador de downloads atualiza

### Após o Teste:
- [ ] Arquivo ZIP contém todos os arquivos
- [ ] Instruções estão incluídas
- [ ] Cliente consegue instalar

## 🎯 Fluxo Completo

```
1. Cliente paga R$ 297
   ↓
2. SigiloPay confirma pagamento
   ↓
3. Webhook recebe notificação
   ↓
4. Sistema gera token único
   ↓
5. Email é enviado com link
   ↓
6. Cliente recebe email
   ↓
7. Cliente clica no link
   ↓
8. Página de download abre
   ↓
9. Sistema verifica token
   ↓
10. Cliente vê informações
   ↓
11. Cliente clica em "Baixar"
   ↓
12. Arquivo ZIP é baixado
   ↓
13. Cliente instala o Lead Extractor
```

## 🎉 Pronto!

Agora você tem uma página de download profissional que:
- ✅ Só libera após pagamento confirmado
- ✅ Controla limite de downloads
- ✅ Mostra informações do cliente
- ✅ Design moderno e responsivo
- ✅ Experiência profissional

---

**Próximos passos:**
1. Testar o fluxo completo
2. Configurar email de produção
3. Fazer deploy
4. Configurar webhook na SigiloPay
