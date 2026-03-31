# 🔒 Guia de Segurança

## ⚠️ IMPORTANTE: Proteção de Credenciais

Este projeto usa variáveis de ambiente para proteger informações sensíveis. **NUNCA** compartilhe suas credenciais publicamente!

## 📋 Checklist de Segurança

### ✅ O Que FAZER

1. **Usar arquivo .env local**
   ```bash
   # Copiar o exemplo
   cp .env.example .env
   
   # Editar com suas credenciais reais
   nano .env  # ou use seu editor favorito
   ```

2. **Configurar variáveis na Vercel**
   - Acesse: Settings → Environment Variables
   - Adicione cada variável manualmente
   - Marque para Production, Preview e Development

3. **Verificar .gitignore**
   ```bash
   # Confirmar que .env está ignorado
   cat .gitignore | grep .env
   ```

4. **Antes de commitar**
   ```bash
   # Verificar o que será commitado
   git status
   
   # Confirmar que .env NÃO aparece na lista
   # Se aparecer, adicione ao .gitignore imediatamente!
   ```

### ❌ O Que NÃO FAZER

1. **NUNCA commitar o arquivo .env**
   ```bash
   # ❌ ERRADO
   git add .env
   git commit -m "Adicionando configurações"
   ```

2. **NUNCA colocar credenciais no código**
   ```javascript
   // ❌ ERRADO
   const apiKey = 'minha_chave_secreta_123';
   
   // ✅ CORRETO
   const apiKey = process.env.API_KEY;
   ```

3. **NUNCA compartilhar credenciais**
   - Não envie por email
   - Não poste em fóruns
   - Não compartilhe em chat
   - Não coloque em documentação pública

4. **NUNCA usar credenciais de produção em desenvolvimento**
   - Use ambientes separados
   - Crie credenciais de teste quando possível

## 🔑 Variáveis de Ambiente

### Arquivo .env.example
Este arquivo é seguro para commitar. Ele mostra a estrutura sem expor valores reais:

```env
# Supabase Configuration
VITE_SUPABASE_URL=your_supabase_url_here
VITE_SUPABASE_ANON_KEY=your_supabase_anon_key_here
SUPABASE_SERVICE_ROLE_KEY=your_supabase_service_role_key_here

# SigiloPay Configuration
SIGILOPAY_PUBLIC_KEY=your_sigilopay_public_key_here
SIGILOPAY_SECRET_KEY=your_sigilopay_secret_key_here
```

### Arquivo .env (NÃO COMMITAR!)
Este arquivo contém suas credenciais reais e NUNCA deve ser commitado:

```env
# Supabase Configuration
VITE_SUPABASE_URL=https://seu-projeto.supabase.co
VITE_SUPABASE_ANON_KEY=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
SUPABASE_SERVICE_ROLE_KEY=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...

# SigiloPay Configuration
SIGILOPAY_PUBLIC_KEY=sua_chave_publica_real
SIGILOPAY_SECRET_KEY=sua_chave_secreta_real
```

## 🚨 Se Você Expôs Credenciais Acidentalmente

### 1. Remover do Git imediatamente
```bash
# Remover arquivo do histórico
git rm --cached .env

# Commitar a remoção
git commit -m "Remove arquivo .env do repositório"

# Forçar push
git push origin main --force
```

### 2. Revogar credenciais comprometidas

**Supabase:**
1. Acesse: https://app.supabase.com/project/seu-projeto/settings/api
2. Clique em "Reset" nas chaves comprometidas
3. Atualize suas variáveis de ambiente

**SigiloPay:**
1. Acesse: https://app.sigilopay.com.br
2. Vá em Configurações → API
3. Gere novas credenciais
4. Atualize suas variáveis de ambiente

### 3. Atualizar todas as instâncias
- Atualizar .env local
- Atualizar variáveis na Vercel
- Fazer novo deploy

## 🔍 Como Verificar se Está Seguro

### Verificar repositório local
```bash
# Procurar por possíveis credenciais expostas
git log --all --full-history --source -- .env

# Se retornar algo, você precisa limpar o histórico!
```

### Verificar repositório remoto (GitHub)
1. Acesse: https://github.com/seu-usuario/seu-repo
2. Use a busca: procure por termos como "supabase", "sigilopay", "secret"
3. Se encontrar credenciais, siga os passos de "Se Você Expôs Credenciais"

### Usar ferramentas de segurança
```bash
# Instalar git-secrets (previne commits de credenciais)
git secrets --install
git secrets --register-aws
```

## 📚 Boas Práticas

### 1. Rotação de Credenciais
- Troque suas credenciais periodicamente (a cada 3-6 meses)
- Use credenciais diferentes para dev/staging/production

### 2. Princípio do Menor Privilégio
- Use apenas as permissões necessárias
- Não use chaves de admin quando chaves de leitura são suficientes

### 3. Monitoramento
- Configure alertas para uso anormal de API
- Monitore logs de acesso
- Revise permissões regularmente

### 4. Backup Seguro
- Guarde credenciais em gerenciador de senhas (1Password, LastPass, etc.)
- Nunca em arquivos de texto simples
- Nunca em emails ou mensagens

## 🆘 Recursos Adicionais

- [OWASP Top 10](https://owasp.org/www-project-top-ten/)
- [GitHub Security Best Practices](https://docs.github.com/en/code-security)
- [Vercel Environment Variables](https://vercel.com/docs/concepts/projects/environment-variables)

## 📞 Em Caso de Dúvidas

Se você não tem certeza se algo é seguro:
1. **NÃO COMMITE** até ter certeza
2. Consulte a documentação
3. Peça ajuda em canais apropriados (sem compartilhar as credenciais!)

---

🔒 **Segurança em primeiro lugar! Proteja suas credenciais como se fossem as chaves da sua casa.**
