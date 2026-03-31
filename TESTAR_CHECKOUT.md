# 🧪 Como Testar o Checkout

## ✅ O Que Foi Atualizado

### Preço Atualizado
- ✅ Landing page: R$ 29,87
- ✅ Checkout: R$ 29,87
- ✅ API: 29.87 (valor enviado para SigiloPay)

### Melhorias Implementadas
- ✅ Validação de email
- ✅ Validação de nome (mínimo 3 caracteres)
- ✅ Validação de CPF (11 dígitos)
- ✅ Mensagens de erro mais claras
- ✅ Loading animado durante processamento
- ✅ QR Code com design melhorado
- ✅ Botão de copiar com feedback visual
- ✅ Scroll automático até o QR Code
- ✅ Informação de expiração (1 hora)
- ✅ Email do cliente exibido na confirmação

## 🧪 Teste Local (Antes do Deploy)

### 1. Abrir o Checkout
```cmd
REM Abrir no navegador
start checkout.html
```

### 2. Preencher o Formulário
- **Nome:** João Silva
- **Email:** teste@teste.com
- **CPF:** 123.456.789-00
- **WhatsApp:** (11) 99999-9999

### 3. Clicar em "Comprar Agora com Segurança"

### 4. Verificar o Comportamento

#### ✅ Deve Acontecer:
1. Loading aparece com mensagem "Gerando seu QR Code PIX..."
2. Após alguns segundos, QR Code aparece
3. Código PIX é exibido abaixo do QR Code
4. Botão "Copiar Código PIX" funciona
5. Email do cliente aparece na mensagem de confirmação
6. Página faz scroll automático até o QR Code

#### ❌ Se Der Erro:
- Verifique o Console do navegador (F12)
- Veja se a API está respondendo
- Confirme que as variáveis de ambiente estão configuradas

## 🚀 Teste em Produção (Após Deploy)

### 1. Acessar o Site
```
https://seu-projeto.vercel.app
```

### 2. Clicar em "Quero Emagrecer Agora"
Deve redirecionar para: `https://seu-projeto.vercel.app/checkout.html`

### 3. Preencher com Dados Reais
Use seus dados reais para testar o pagamento completo.

### 4. Fazer um Pagamento de Teste
- Gere o QR Code
- Pague R$ 29,87 via PIX
- Verifique se recebe o e-book no email

## 🔍 Verificar Logs

### Logs da Vercel
```cmd
REM Se tiver Vercel CLI instalado
vercel logs
```

Ou acesse: https://vercel.com/seu-projeto/logs

### Console do Navegador
1. Pressione F12
2. Vá na aba "Console"
3. Veja se há erros em vermelho

### Network Tab
1. Pressione F12
2. Vá na aba "Network"
3. Clique em "Comprar Agora"
4. Procure por `/api/payment-pix`
5. Veja a resposta da API

## 📊 Fluxo Completo

```
1. Landing Page (index.html)
   ↓ Clique em "Quero Emagrecer Agora"
   
2. Checkout (checkout.html)
   ↓ Preenche formulário
   ↓ Clique em "Comprar Agora com Segurança"
   
3. API (/api/payment-pix)
   ↓ Valida dados
   ↓ Envia para SigiloPay
   ↓ Retorna QR Code
   
4. Exibição do QR Code
   ↓ Cliente escaneia
   ↓ Paga R$ 29,87
   
5. Confirmação
   ↓ Cliente recebe e-book por email
```

## 🐛 Troubleshooting

### Erro: "Failed to fetch"
**Causa:** API não está respondendo

**Solução:**
1. Verifique se as variáveis de ambiente estão configuradas na Vercel
2. Veja os logs: `vercel logs`
3. Confirme que `SIGILOPAY_PUBLIC_KEY` e `SIGILOPAY_SECRET_KEY` estão corretas

### Erro: "QR Code não foi gerado"
**Causa:** SigiloPay não retornou o QR Code

**Solução:**
1. Verifique as credenciais do SigiloPay
2. Confirme que a conta está ativa
3. Veja os logs da API para detalhes do erro

### Erro: "CPF inválido"
**Causa:** CPF não tem 11 dígitos

**Solução:**
Digite um CPF com 11 números (pode ser fictício para teste)

### Erro: "Email inválido"
**Causa:** Formato de email incorreto

**Solução:**
Digite um email válido: `nome@dominio.com`

## ✅ Checklist de Teste

### Validações
- [ ] Nome com menos de 3 caracteres é rejeitado
- [ ] Email inválido é rejeitado
- [ ] CPF com menos de 11 dígitos é rejeitado
- [ ] Campos vazios são rejeitados

### Funcionalidades
- [ ] Loading aparece ao processar
- [ ] QR Code é gerado corretamente
- [ ] Código PIX pode ser copiado
- [ ] Botão de copiar muda para "✅ Copiado!"
- [ ] Email do cliente aparece na confirmação
- [ ] Scroll automático funciona

### Integração
- [ ] API responde corretamente
- [ ] SigiloPay gera o QR Code
- [ ] Valor correto (R$ 29,87) é enviado
- [ ] Dados do cliente são salvos

### Pagamento Real
- [ ] QR Code pode ser escaneado
- [ ] Pagamento é processado
- [ ] Cliente recebe confirmação
- [ ] E-book é enviado por email

## 📱 Teste em Dispositivos

### Desktop
- [ ] Chrome
- [ ] Firefox
- [ ] Edge
- [ ] Safari (Mac)

### Mobile
- [ ] Chrome (Android)
- [ ] Safari (iOS)
- [ ] Navegador padrão

### Responsividade
- [ ] Formulário legível em mobile
- [ ] QR Code visível em mobile
- [ ] Botões clicáveis em mobile
- [ ] Scroll funciona em mobile

## 🎯 Resultado Esperado

Ao final do teste, você deve:
1. ✅ Ver o QR Code gerado
2. ✅ Conseguir copiar o código PIX
3. ✅ Ver o email do cliente na confirmação
4. ✅ Poder escanear e pagar (se testar com dinheiro real)

## 📞 Suporte

Se algo não funcionar:
1. Veja os logs: `vercel logs`
2. Verifique o console do navegador (F12)
3. Confirme as variáveis de ambiente
4. Teste as credenciais do SigiloPay no painel deles

---

**Tudo pronto para testar!** 🚀
