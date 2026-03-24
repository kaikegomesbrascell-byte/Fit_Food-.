# ✅ Evento de Conversão de Compra Configurado

## 🎯 Status: Instalado e Ativo

O evento de conversão de compra foi configurado com sucesso na página de obrigado.

## 📊 Configuração do Evento

### Detalhes do Evento
```javascript
gtag('event', 'conversion', {
  'send_to': 'AW-18030639277/mg8YCPyF4Y0cEK3x1pVD',
  'value': 297.0,
  'currency': 'BRL',
  'transaction_id': ''
});
```

### Informações
- **Tipo:** Conversão de Compra
- **ID:** `AW-18030639277/mg8YCPyF4Y0cEK3x1pVD`
- **Valor:** R$ 297,00
- **Moeda:** BRL (Real Brasileiro)
- **Transaction ID:** Vazio (pode ser preenchido dinamicamente)

## 📍 Localização

### Arquivo
`landing-page/src/pages/ThankYou.tsx`

### Páginas Ativas
- ✅ `/obrigado` (português)
- ✅ `/thank-you` (inglês)

### Quando Dispara
O evento dispara automaticamente quando a página de obrigado carrega, usando o `useEffect` do React.

## 🎯 O Que é Rastreado

### Evento de Conversão
Toda vez que um cliente:
1. Completa o pagamento
2. É redirecionado para `/obrigado`
3. A página carrega

O Google Ads registra:
- ✅ Uma conversão de compra
- ✅ Valor de R$ 297,00
- ✅ Moeda BRL
- ✅ Data e hora da conversão

## 📈 Benefícios

### 1. Rastreamento de ROI
- Veja quanto você gasta em anúncios vs quanto ganha em vendas
- Calcule o ROI real das suas campanhas

### 2. Otimização de Campanhas
- Google Ads otimiza automaticamente para conversões
- Mostra anúncios para pessoas mais propensas a comprar

### 3. Relatórios Detalhados
- Veja quantas conversões por dia/semana/mês
- Compare diferentes campanhas
- Identifique os melhores anúncios

### 4. Remarketing Inteligente
- Crie listas de pessoas que compraram
- Exclua compradores de campanhas de aquisição
- Faça upsell para clientes existentes

## 🧪 Como Testar

### Teste Manual

1. **Acesse a página de obrigado:**
   ```
   https://seu-dominio.vercel.app/obrigado
   ```

2. **Abra o Console do navegador:**
   - Pressione F12
   - Vá na aba "Console"

3. **Verifique se o evento disparou:**
   - Você deve ver algo como: `gtag('event', 'conversion', ...)`
   - Ou use o Google Tag Assistant

4. **Aguarde 24-48 horas:**
   - As conversões podem levar até 48h para aparecer no Google Ads

### Teste com Google Tag Assistant

1. **Instale a extensão:**
   - [Google Tag Assistant](https://chrome.google.com/webstore/detail/tag-assistant-legacy-by-g/kejbdjndbnbjgmefkgdddjlbokphdefk)

2. **Acesse a página de obrigado**

3. **Clique no ícone da extensão**

4. **Verifique:**
   - Tag base: `AW-18030639277` ✅
   - Evento de conversão: `mg8YCPyF4Y0cEK3x1pVD` ✅

## 📊 Verificar no Google Ads

### 1. Acesse o Google Ads
```
https://ads.google.com
```

### 2. Vá em Conversões
```
Ferramentas → Medição → Conversões
```

### 3. Encontre sua conversão
- Nome: "Compra" ou similar
- ID: `mg8YCPyF4Y0cEK3x1pVD`

### 4. Verifique os dados
- Conversões recentes
- Valor total
- Taxa de conversão

## 🔧 Personalização Avançada

### Adicionar Transaction ID Único

Para rastrear cada compra individualmente, adicione um ID único:

```typescript
useEffect(() => {
  window.scrollTo(0, 0);
  
  // Gerar ID único para a transação
  const transactionId = `TXN-${Date.now()}-${Math.random().toString(36).substr(2, 9)}`;
  
  if (typeof window.gtag !== 'undefined') {
    window.gtag('event', 'conversion', {
      'send_to': 'AW-18030639277/mg8YCPyF4Y0cEK3x1pVD',
      'value': 297.0,
      'currency': 'BRL',
      'transaction_id': transactionId
    });
  }
}, []);
```

### Adicionar Informação de Novo Cliente

Se você souber se é um cliente novo ou recorrente:

```typescript
const isNewCustomer = true; // ou false

window.gtag('event', 'conversion', {
  'send_to': 'AW-18030639277/mg8YCPyF4Y0cEK3x1pVD',
  'value': 297.0,
  'currency': 'BRL',
  'transaction_id': '',
  'new_customer': isNewCustomer
});
```

### Valor Dinâmico

Se o valor da compra variar:

```typescript
const purchaseValue = 297.0; // Pode vir de uma API ou parâmetro

window.gtag('event', 'conversion', {
  'send_to': 'AW-18030639277/mg8YCPyF4Y0cEK3x1pVD',
  'value': purchaseValue,
  'currency': 'BRL',
  'transaction_id': ''
});
```

## 📈 Métricas Importantes

### No Google Ads, você verá:

1. **Conversões**
   - Número total de compras

2. **Valor de Conversão**
   - Soma de todas as compras (R$ 297 × número de conversões)

3. **Taxa de Conversão**
   - % de visitantes que compraram

4. **Custo por Conversão**
   - Quanto você gasta em anúncios para cada venda

5. **ROAS (Return on Ad Spend)**
   - Quanto você ganha para cada R$ 1 gasto em anúncios

## 🎯 Otimização de Campanhas

Com o evento de conversão configurado, você pode:

### 1. Estratégia de Lance Automática
- Use "Maximizar conversões"
- Ou "CPA desejado"
- Google otimiza automaticamente

### 2. Públicos Semelhantes
- Crie públicos baseados em compradores
- Encontre pessoas similares

### 3. Exclusão de Compradores
- Exclua quem já comprou
- Economize orçamento

### 4. Campanhas de Remarketing
- Mostre anúncios diferentes para compradores
- Faça upsell ou cross-sell

## 🔍 Troubleshooting

### Conversões não aparecem no Google Ads?

1. **Aguarde 24-48 horas**
   - Conversões podem demorar para aparecer

2. **Verifique o ID**
   - Certifique-se: `AW-18030639277/mg8YCPyF4Y0cEK3x1pVD`

3. **Teste com Tag Assistant**
   - Verifique se o evento está disparando

4. **Limpe o cache**
   - Ctrl + Shift + Delete
   - Teste em modo anônimo

### Conversões duplicadas?

1. **Adicione Transaction ID único**
   - Google Ads remove duplicatas automaticamente

2. **Verifique se o evento dispara apenas uma vez**
   - Use `useEffect` com array de dependências vazio `[]`

### Valor errado?

1. **Verifique o código**
   - Valor deve ser: `297.0` (sem vírgula)
   - Moeda deve ser: `'BRL'`

2. **Atualize o código**
   - Edite `src/pages/ThankYou.tsx`
   - Faça commit e push

## 📞 Suporte

### Documentação Oficial
- [Google Ads - Conversões](https://support.google.com/google-ads/answer/6331314)
- [gtag.js - Eventos](https://developers.google.com/tag-platform/gtagjs/reference/events)

### Verificar Status
- [Google Tag Assistant](https://tagassistant.google.com/)
- [Google Ads - Conversões](https://ads.google.com/aw/conversions)

---

**Status:** ✅ Configurado e Ativo
**Commit:** `aa3821b - feat: Adiciona evento de conversão de compra na página de obrigado`
**Data:** 22/03/2026
**Evento:** Compra (Conversion)
**ID:** AW-18030639277/mg8YCPyF4Y0cEK3x1pVD
**Valor:** R$ 297,00
