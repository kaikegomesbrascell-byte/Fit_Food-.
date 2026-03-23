# 📱 Como Configurar o Número do WhatsApp

## Página de Obrigado

Para configurar o número do WhatsApp na página de obrigado, edite o arquivo:

**Arquivo:** `src/pages/ThankYou.tsx`

**Linha 14:**
```typescript
const phoneNumber = "5511999999999"; // ALTERE AQUI
```

### Formato do Número

O número deve estar no formato internacional sem espaços, hífens ou parênteses:

- **Código do país:** 55 (Brasil)
- **DDD:** 11, 21, 47, etc.
- **Número:** 9 dígitos (celular) ou 8 dígitos (fixo)

### Exemplos

```typescript
// São Paulo (11)
const phoneNumber = "5511987654321";

// Rio de Janeiro (21)
const phoneNumber = "5521987654321";

// Curitiba (41)
const phoneNumber = "5541987654321";

// WhatsApp Business
const phoneNumber = "5511912345678";
```

### Mensagem Padrão

A mensagem que o cliente verá ao clicar no botão é:

```
"Olá! Acabei de adquirir o LeadExtract e preciso de ajuda com a instalação."
```

Para alterar a mensagem, edite a **linha 15** do arquivo `ThankYou.tsx`:

```typescript
const message = encodeURIComponent("Sua mensagem personalizada aqui");
```

## Testando

1. Acesse: `http://localhost:5173/obrigado`
2. Clique no botão "Falar com Suporte no WhatsApp"
3. Verifique se abre o WhatsApp com o número correto

## URLs da Página

A página de obrigado está disponível em 2 URLs:

- `/obrigado` (português)
- `/thank-you` (inglês)

Ambas exibem a mesma página.

## Deploy

Após configurar o número, faça o deploy:

```bash
cd landing-page
git add .
git commit -m "chore: Configura número do WhatsApp na página de obrigado"
git push origin main
```

O Vercel fará o deploy automático.
