# 🥗 Landing Page - 100 Receitas Fit

Landing page moderna para venda do e-book "100 Receitas Fit de Apenas 3 Ingredientes".

## 🚀 Deploy na Vercel

### Configuração Rápida

1. Copie `.env.example` para `.env` e preencha com suas credenciais
2. Conecte seu repositório na Vercel
3. Configure as variáveis de ambiente (veja abaixo)
4. Deploy automático!

### Variáveis de Ambiente Necessárias

⚠️ **IMPORTANTE:** Nunca exponha suas credenciais! Use sempre variáveis de ambiente.

Copie o arquivo `.env.example` para `.env` e preencha com suas credenciais reais:

```bash
cp .env.example .env
```

Depois configure as mesmas variáveis na Vercel:

```env
# Supabase
VITE_SUPABASE_URL=your_supabase_url_here
VITE_SUPABASE_ANON_KEY=your_supabase_anon_key_here
SUPABASE_SERVICE_ROLE_KEY=your_supabase_service_role_key_here

# SigiloPay
SIGILOPAY_PUBLIC_KEY=your_sigilopay_public_key_here
SIGILOPAY_SECRET_KEY=your_sigilopay_secret_key_here
```

**Nota:** Copie o arquivo `.env.example` para `.env` e preencha com suas credenciais reais.

Marque todas as variáveis para: **Production**, **Preview** e **Development**

## 💳 Integração de Pagamento - SigiloPay

### Criar Pagamento PIX

```javascript
POST https://app.sigilopay.com.br/api/v1/gateway/pix/receive

Headers:
{
  "Content-Type": "application/json",
  "x-public-key": "kaikegomesbrascell_dj5xs7rlxoaoew4z",
  "x-secret-key": "nvt3mku331xhv1d8oxmqfnp20tjecpacan3v5gk0n276u5kkhexqieuz8y3cmc9f"
}

Body:
{
  "identifier": "receitas-fit-123456",
  "amount": 47,
  "client": {
    "name": "Nome do Cliente",
    "email": "email@exemplo.com",
    "document": "12345678900"
  },
  "expiresIn": 3600
}
```

### Resposta

```json
{
  "pix": {
    "code": "00020126580014br.gov.bcb.pix...",
    "base64": "iVBORw0KGgoAAAANSUhEUgAAA..."
  },
  "transactionId": "cmn2310ly12ul1smm14put5uf",
  "status": "PENDING"
}
```

Use o QR Code: `data:image/png;base64,${pix.base64}`

## 📁 Estrutura do Projeto

```
/
├── index.html                          # Landing page principal
├── The_camera_slowly_202603311118.mp4  # Vídeo de demonstração
├── 100-Receitas-Fit-de-Apenas-3-Ingredientes - Copia.pdf  # E-book
├── vercel.json                         # Configuração Vercel
├── api/
│   ├── payment-pix.js                  # API serverless para PIX
│   └── package.json                    # Dependências da API
└── README.md                           # Este arquivo
```

## 🎯 Funcionalidades

- ✅ Design moderno e responsivo
- ✅ Vídeo de demonstração integrado
- ✅ Carrossel de benefícios automático
- ✅ Seção de preços com CTA
- ✅ Integração com SigiloPay (PIX)
- ✅ Deploy automático na Vercel

## 📚 Documentação Completa

- [INICIO_RAPIDO.md](./INICIO_RAPIDO.md) - Setup em 5 minutos
- [SEGURANCA.md](./SEGURANCA.md) - **LEIA PRIMEIRO!** Proteção de credenciais
- [COMO_FAZER_DEPLOY.md](./COMO_FAZER_DEPLOY.md) - Guia passo a passo
- [Setup Vercel](./VERCEL_SETUP.md) - Guia completo de deploy
- [API SigiloPay](./SIGILOPAY_API_DOCS.md) - Documentação da API de pagamento
- [Estrutura do Projeto](./ESTRUTURA_FINAL.md) - Arquivos e pastas
- [Resumo do Projeto](./PROJETO_RECEITAS_FIT.md) - Visão geral completa

## 🔒 Segurança

⚠️ **ATENÇÃO:** Este projeto usa variáveis de ambiente para proteger credenciais sensíveis.

- ✅ Arquivo `.env.example` - Seguro para commitar (template)
- ❌ Arquivo `.env` - NUNCA commitar (contém credenciais reais)
- ✅ Credenciais na Vercel - Configuradas via dashboard

**Leia o [Guia de Segurança](./SEGURANCA.md) antes de fazer deploy!**

## 🔒 Segurança

- Todas as chamadas à API SigiloPay são feitas via serverless functions
- Credenciais protegidas por variáveis de ambiente
- CORS configurado corretamente
- Pagamentos processados de forma segura

## 📞 Suporte

Para dúvidas sobre:
- **Deploy**: Verifique os logs na Vercel
- **Pagamentos**: Consulte o painel SigiloPay
- **Código**: Abra uma issue no repositório

---

Desenvolvido com ❤️ para ajudar pessoas a terem uma vida mais saudável
