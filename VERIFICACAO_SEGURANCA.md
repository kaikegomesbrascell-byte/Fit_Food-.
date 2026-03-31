# ✅ Checklist de Verificação de Segurança

Use este checklist antes de fazer commit e deploy para garantir que nenhuma credencial seja exposta.

## 📋 Antes de Commitar

### 1. Verificar arquivo .env
```bash
# ❌ Se este comando mostrar o arquivo, NÃO COMMITE!
git status | grep ".env"

# ✅ Deve mostrar apenas .env.example
git status | grep ".env.example"
```

**Ação:** Se `.env` aparecer, adicione ao .gitignore imediatamente!

### 2. Verificar código-fonte
```bash
# Procurar por possíveis credenciais hardcoded
grep -r "supabase.co" --exclude-dir=node_modules --exclude-dir=.git .
grep -r "sigilopay" --exclude-dir=node_modules --exclude-dir=.git .
grep -r "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9" --exclude-dir=node_modules --exclude-dir=.git .
```

**Ação:** Se encontrar credenciais reais, substitua por `process.env.VARIAVEL`

### 3. Verificar arquivos staged
```bash
# Ver o que será commitado
git diff --cached

# Procurar por padrões suspeitos
git diff --cached | grep -i "secret\|key\|password\|token"
```

**Ação:** Se encontrar credenciais, remova do stage e corrija!

### 4. Verificar .gitignore
```bash
# Confirmar que .env está ignorado
cat .gitignore | grep "^\.env$"
```

**Ação:** Se não estiver, adicione `.env` ao .gitignore!

## 📋 Antes de Fazer Deploy

### 1. Verificar variáveis de ambiente na Vercel
- [ ] `VITE_SUPABASE_URL` configurada
- [ ] `VITE_SUPABASE_ANON_KEY` configurada
- [ ] `SUPABASE_SERVICE_ROLE_KEY` configurada
- [ ] `SIGILOPAY_PUBLIC_KEY` configurada
- [ ] `SIGILOPAY_SECRET_KEY` configurada
- [ ] Todas marcadas para Production, Preview, Development

### 2. Verificar código da API
```bash
# Verificar se a API usa variáveis de ambiente
cat api/payment-pix.js | grep "process.env"
```

**Esperado:** Deve mostrar todas as variáveis sendo lidas de `process.env`

### 3. Verificar documentação
```bash
# Procurar por credenciais expostas na documentação
grep -r "kaikegomesbrascell" *.md
grep -r "blodznzrdzjsvaqabsvj" *.md
grep -r "nvt3mku331xhv1d8oxmqfnp20tjecpacan3v5gk0n276u5kkhexqieuz8y3cmc9f" *.md
```

**Ação:** Se encontrar, substitua por placeholders genéricos!

## 📋 Após Deploy

### 1. Testar com credenciais de produção
- [ ] Landing page carrega
- [ ] Vídeo funciona
- [ ] Checkout abre
- [ ] QR Code PIX é gerado
- [ ] Código PIX pode ser copiado

### 2. Verificar logs
```bash
# Ver logs da Vercel
vercel logs --follow
```

**Ação:** Confirme que não há erros de variáveis de ambiente faltando

### 3. Testar pagamento real (opcional)
- [ ] Fazer um pagamento de teste
- [ ] Verificar se o webhook funciona (se configurado)
- [ ] Confirmar que o cliente recebe o e-book

## 🚨 Checklist de Emergência

Se você acidentalmente expôs credenciais:

### Ação Imediata
- [ ] Remover arquivo do Git: `git rm --cached .env`
- [ ] Commitar remoção: `git commit -m "Remove .env"`
- [ ] Force push: `git push --force`

### Revogar Credenciais
- [ ] Supabase: Resetar chaves em Settings → API
- [ ] SigiloPay: Gerar novas credenciais no painel

### Atualizar Tudo
- [ ] Atualizar `.env` local
- [ ] Atualizar variáveis na Vercel
- [ ] Fazer novo deploy
- [ ] Testar tudo novamente

## 📊 Score de Segurança

Conte quantos itens você marcou:

- **20/20** ✅ Excelente! Seu projeto está seguro
- **15-19** ⚠️ Bom, mas revise os itens não marcados
- **10-14** 🔶 Atenção! Corrija os problemas antes de continuar
- **< 10** 🚨 PARE! Não faça deploy até corrigir tudo

## 🔍 Ferramentas Úteis

### git-secrets (Previne commits de credenciais)
```bash
# Instalar
brew install git-secrets  # macOS
# ou
apt-get install git-secrets  # Linux

# Configurar
git secrets --install
git secrets --register-aws
```

### truffleHog (Encontra credenciais no histórico)
```bash
# Instalar
pip install truffleHog

# Escanear repositório
trufflehog --regex --entropy=False .
```

### gitleaks (Detecta segredos)
```bash
# Instalar
brew install gitleaks  # macOS

# Escanear
gitleaks detect --source . --verbose
```

## 📚 Recursos

- [OWASP Cheat Sheet](https://cheatsheetseries.owasp.org/)
- [GitHub Security](https://docs.github.com/en/code-security)
- [Vercel Security](https://vercel.com/docs/security)

## ✅ Certificação

Ao marcar todos os itens acima, você certifica que:

- ✅ Nenhuma credencial está exposta no código
- ✅ Todas as credenciais usam variáveis de ambiente
- ✅ O arquivo `.env` está no `.gitignore`
- ✅ A documentação não contém credenciais reais
- ✅ As variáveis estão configuradas na Vercel
- ✅ O projeto foi testado e está funcionando

---

🔒 **Segurança não é opcional. É essencial!**

Data da última verificação: ___/___/______
Verificado por: _______________________
