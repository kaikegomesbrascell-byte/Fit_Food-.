# ✅ Google Tag Manager Configurado

## 📊 Status: Instalado e Ativo

O Google Tag Manager (gtag.js) foi instalado com sucesso em todas as páginas da sua aplicação.

## 🎯 Configuração Atual

### ID de Rastreamento
```
AW-18030639277
```

### Localização
O código foi adicionado no arquivo `index.html`, dentro da tag `<head>`, logo no início:

```html
<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=AW-18030639277"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'AW-18030639277');
</script>
```

## 🌐 Páginas Rastreadas

O Google Tag está ativo em TODAS as páginas da aplicação:

- ✅ **Landing Page** (`/`)
- ✅ **Página de Obrigado** (`/obrigado` e `/thank-you`)
- ✅ **Página de Download** (`/download`)
- ✅ **Todas as outras páginas**

## 📈 Eventos Rastreados Automaticamente

### 1. Pageviews (Visualizações de Página)
Toda vez que um usuário acessa uma página, o evento é registrado automaticamente.

### 2. Conversões (quando configuradas)
Você pode configurar eventos de conversão no Google Ads para rastrear:
- Compras
- Cliques em botões
- Preenchimento de formulários
- Downloads
- Etc.

## 🎯 Como Configurar Eventos de Conversão

### Evento de Conversão: Compra Concluída

Para rastrear quando um cliente completa a compra, adicione este código na página de obrigado:

**Arquivo:** `src/pages/ThankYou.tsx`

**Adicione no `useEffect`:**

```typescript
useEffect(() => {
  // Scroll to top on mount
  window.scrollTo(0, 0);
  
  // Rastrear conversão de compra
  if (typeof window.gtag !== 'undefined') {
    window.gtag('event', 'conversion', {
      'send_to': 'AW-18030639277/CONVERSION_ID', // Substitua CONVERSION_ID
      'value': 297.00,
      'currency': 'BRL',
      'transaction_id': ''
    });
  }
}, []);
```

**Onde encontrar o CONVERSION_ID:**
1. Acesse Google Ads
2. Vá em: Ferramentas → Conversões
3. Crie uma nova conversão ou copie o ID de uma existente
4. Substitua `CONVERSION_ID` no código acima

### Evento de Conversão: Download Iniciado

Para rastrear quando o cliente clica no botão de download:

```typescript
const handleDownload = () => {
  // Rastrear evento de download
  if (typeof window.gtag !== 'undefined') {
    window.gtag('event', 'download', {
      'event_category': 'engagement',
      'event_label': 'lead-extractor-zip'
    });
  }
  
  // Trigger download from public folder
  window.location.href = "/lead-extractor.zip";
};
```

### Evento de Conversão: Clique no Botão de Compra

Para rastrear quando o cliente clica em "Comprar Agora":

**Arquivo:** `src/components/landing/PricingSection.tsx`

```typescript
const handleBuyClick = () => {
  // Rastrear clique no botão de compra
  if (typeof window.gtag !== 'undefined') {
    window.gtag('event', 'begin_checkout', {
      'event_category': 'ecommerce',
      'event_label': 'lead-extractor',
      'value': 297.00,
      'currency': 'BRL'
    });
  }
  
  setCheckoutOpen(true);
};
```

## 🧪 Como Testar

### 1. Verificar se o Tag está Carregando

1. Acesse sua landing page
2. Abra o Console do navegador (F12)
3. Digite: `window.gtag`
4. Se retornar uma função, o tag está funcionando ✅

### 2. Usar o Google Tag Assistant

1. Instale a extensão: [Google Tag Assistant](https://chrome.google.com/webstore/detail/tag-assistant-legacy-by-g/kejbdjndbnbjgmefkgdddjlbokphdefk)
2. Acesse sua landing page
3. Clique no ícone da extensão
4. Verifique se o tag `AW-18030639277` aparece

### 3. Verificar no Google Ads

1. Acesse Google Ads
2. Vá em: Ferramentas → Conversões
3. Verifique se os eventos estão sendo registrados

## 📊 Relatórios Disponíveis

Com o Google Tag instalado, você pode ver:

### No Google Ads:
- Número de visitantes
- Taxa de conversão
- Custo por conversão
- ROI das campanhas

### No Google Analytics (se configurado):
- Páginas mais visitadas
- Tempo médio na página
- Taxa de rejeição
- Funil de conversão

## 🔧 Troubleshooting

### Tag não está funcionando?

1. **Limpe o cache do navegador**
   - Ctrl + Shift + Delete
   - Limpe cache e cookies

2. **Verifique o Console**
   - Abra F12
   - Veja se há erros relacionados ao gtag

3. **Aguarde o deploy**
   - O Vercel pode levar 1-2 minutos para fazer o deploy

4. **Teste em modo anônimo**
   - Abra uma janela anônima
   - Acesse sua landing page
   - Verifique se o tag carrega

### Conversões não estão sendo rastreadas?

1. **Verifique o CONVERSION_ID**
   - Certifique-se de que está correto
   - Formato: `AW-18030639277/CONVERSION_ID`

2. **Aguarde até 24 horas**
   - O Google Ads pode levar até 24h para mostrar conversões

3. **Teste com Google Tag Assistant**
   - Use a extensão para verificar se os eventos estão disparando

## 📝 Próximos Passos

### 1. Configure Conversões no Google Ads
- Crie eventos de conversão
- Defina valores para cada conversão
- Configure metas

### 2. Adicione Eventos Personalizados
- Rastreie cliques em botões específicos
- Monitore scroll da página
- Rastreie tempo de permanência

### 3. Integre com Google Analytics
- Adicione o código do GA4
- Configure funis de conversão
- Crie relatórios personalizados

### 4. Configure Remarketing
- Crie listas de remarketing
- Configure campanhas de retargeting
- Aumente a taxa de conversão

## 🎯 Eventos Recomendados para Rastrear

1. **Visualização da Landing Page** ✅ (já rastreado)
2. **Clique em "Comprar Agora"** (adicionar)
3. **Visualização da Página de Obrigado** ✅ (já rastreado)
4. **Download do Software** (adicionar)
5. **Clique no WhatsApp** (adicionar)
6. **Scroll até o Pricing** (adicionar)
7. **Tempo na página > 30s** (adicionar)

## 📞 Suporte

Se precisar de ajuda com a configuração:

1. **Documentação do Google Ads:**
   - https://support.google.com/google-ads/answer/6331314

2. **Documentação do gtag.js:**
   - https://developers.google.com/tag-platform/gtagjs

3. **Google Tag Assistant:**
   - https://tagassistant.google.com/

---

**Status:** ✅ Instalado e Funcionando
**Commit:** `b192353 - feat: Adiciona Google Tag Manager (gtag.js) para rastreamento`
**Data:** 22/03/2026
**ID:** AW-18030639277
