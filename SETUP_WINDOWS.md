# 🪟 Setup no Windows - Guia Rápido

## ✅ Seu .env Já Está Configurado!

Ótima notícia! O arquivo `.env` já existe com suas credenciais. Não precisa fazer nada!

## 📋 Verificar Configuração

### 1. Ver o conteúdo do .env
```cmd
type .env
```

### 2. Verificar se está no .gitignore
```cmd
findstr ".env" .gitignore
```

Deve mostrar: `.env`

## 🚀 Próximos Passos

### 1. Commitar o Código (SEM o .env)
```cmd
git add .
git commit -m "Landing Page Receitas Fit - Versão Final"
git push origin main
```

**Importante:** O arquivo `.env` NÃO será incluído no commit (protegido pelo .gitignore)

### 2. Configurar Variáveis na Vercel

Acesse: https://vercel.com/seu-projeto/settings/environment-variables

Adicione estas variáveis (copie os valores do seu `.env`):

| Variável | Onde Encontrar |
|----------|----------------|
| `VITE_SUPABASE_URL` | Abra o `.env` e copie o valor |
| `VITE_SUPABASE_ANON_KEY` | Abra o `.env` e copie o valor |
| `SUPABASE_SERVICE_ROLE_KEY` | Abra o `.env` e copie o valor |
| `SIGILOPAY_PUBLIC_KEY` | Painel SigiloPay |
| `SIGILOPAY_SECRET_KEY` | Painel SigiloPay |

**Marque para:** Production, Preview e Development

### 3. Fazer Deploy
```cmd
git push origin main
```

A Vercel fará o deploy automaticamente!

## 🔍 Comandos Úteis no Windows

### Ver arquivo
```cmd
type arquivo.txt
```

### Copiar arquivo
```cmd
copy origem.txt destino.txt
```

### Procurar texto em arquivo
```cmd
findstr "texto" arquivo.txt
```

### Ver status do Git
```cmd
git status
```

### Ver diferenças
```cmd
git diff
```

## ⚠️ Importante: Proteção do .env

### ✅ O Que Está Protegido
- `.env` está no `.gitignore`
- Não será commitado
- Suas credenciais estão seguras

### 🔍 Verificar Proteção
```cmd
git status
```

Se `.env` aparecer na lista, **NÃO COMMITE!** Adicione ao .gitignore:
```cmd
echo .env >> .gitignore
```

## 📱 Testar Localmente

### Opção 1: Abrir direto no navegador
```cmd
start index.html
```

### Opção 2: Usar servidor local
```cmd
npx serve .
```

Depois acesse: http://localhost:3000

## 🐛 Troubleshooting

### Erro: 'git' não é reconhecido
**Solução:** Instale o Git: https://git-scm.com/download/win

### Erro: 'npx' não é reconhecido
**Solução:** Instale o Node.js: https://nodejs.org/

### Erro: Não consigo ver o .env
**Solução:** Mostrar arquivos ocultos:
1. Abra o Explorador de Arquivos
2. Clique em "Exibir"
3. Marque "Itens ocultos"

## ✅ Checklist Rápido

- [x] Arquivo `.env` existe com credenciais
- [x] `.env` está no `.gitignore`
- [ ] Código commitado no Git
- [ ] Variáveis configuradas na Vercel
- [ ] Deploy realizado
- [ ] Site testado e funcionando

## 🎯 Resumo

Seu `.env` já está configurado! Agora é só:

1. **Commitar** o código (sem o .env)
2. **Configurar** variáveis na Vercel
3. **Deploy** automático!

---

**Dúvidas?** Consulte:
- [README.md](./README.md)
- [COMO_FAZER_DEPLOY.md](./COMO_FAZER_DEPLOY.md)
- [SEGURANCA.md](./SEGURANCA.md)
