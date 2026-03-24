# Instruções de Build - Google Maps Lead Extractor

Este documento fornece instruções detalhadas para gerar o executável standalone do Lead Extractor usando PyInstaller.

## Pré-requisitos

### 1. Python 3.9 ou superior
Certifique-se de ter Python 3.9+ instalado:
```bash
python --version
```

### 2. Instalar Dependências
Instale todas as dependências do projeto:
```bash
pip install -r requirements.txt
```

### 3. Instalar PyInstaller
```bash
pip install pyinstaller
```

### 4. Instalar Navegadores do Playwright
O Playwright requer a instalação dos navegadores:
```bash
playwright install chromium
```

## Gerando o Executável

### Opção 1: Usando o arquivo .spec (Recomendado)

O arquivo `lead_extractor.spec` já está configurado com todas as dependências necessárias.

```bash
pyinstaller lead_extractor.spec
```

### Opção 2: Comando direto (Alternativa)

Se preferir não usar o arquivo .spec:

```bash
pyinstaller --name=LeadExtractor ^
    --onefile ^
    --windowed ^
    --add-data "license.key;." ^
    --hidden-import=playwright ^
    --hidden-import=customtkinter ^
    --hidden-import=pandas ^
    --hidden-import=openpyxl ^
    --hidden-import=psutil ^
    --hidden-import=asyncio ^
    --hidden-import=threading ^
    --collect-all playwright ^
    --collect-all customtkinter ^
    main.py
```

**Nota:** No Linux/Mac, use `:` ao invés de `;` no `--add-data`

## Estrutura de Saída

Após a execução do PyInstaller, você encontrará:

```
projeto/
├── build/              # Arquivos temporários de build (pode ser deletado)
├── dist/               # Executável final
│   └── LeadExtractor.exe
├── lead_extractor.spec # Arquivo de configuração
└── ...
```

O executável final estará em: `dist/LeadExtractor.exe`

## Configurações do Arquivo .spec

### Modo One-File vs One-Folder

**Modo Atual: One-File** (configuração padrão)
- Gera um único arquivo .exe
- Mais fácil de distribuir
- Tamanho maior (~150-200MB)
- Inicialização ligeiramente mais lenta

**Para mudar para One-Folder:**
1. Abra `lead_extractor.spec`
2. No bloco `EXE`, remova as linhas:
   ```python
   a.binaries,
   a.zipfiles,
   a.datas,
   ```
3. Adicione após o bloco `EXE`:
   ```python
   coll = COLLECT(
       exe,
       a.binaries,
       a.zipfiles,
       a.datas,
       strip=False,
       upx=True,
       upx_exclude=[],
       name='LeadExtractor',
   )
   ```

### Inclusão de Dependências

O arquivo .spec já inclui:

✅ **Playwright** - Automação de navegador
- Todos os submódulos do Playwright
- Arquivos de dados necessários
- Drivers do Chromium

✅ **CustomTkinter** - Interface gráfica
- Todos os submódulos do CustomTkinter
- Temas e recursos visuais

✅ **Pandas e OpenPyXL** - Exportação de dados
- Submódulos necessários para Excel/CSV

✅ **Bibliotecas Padrão**
- asyncio, threading, tkinter, psutil, etc.

### Adicionar Ícone da Aplicação

Se você tiver um arquivo de ícone (.ico):

1. Coloque o arquivo `icon.ico` na raiz do projeto
2. No arquivo `lead_extractor.spec`, altere a linha:
   ```python
   icon=None,
   ```
   Para:
   ```python
   icon='icon.ico',
   ```

## Otimizações de Tamanho

### Compressão UPX

O arquivo .spec já está configurado para usar UPX (compressão):
```python
upx=True,
```

Para instalar UPX:
- **Windows:** Baixe de https://upx.github.io/
- **Linux:** `sudo apt-get install upx`
- **Mac:** `brew install upx`

### Exclusões

O arquivo .spec já exclui bibliotecas não utilizadas:
```python
excludes=[
    'matplotlib',
    'numpy.testing',
    'pytest',
    'setuptools',
]
```

## Testando o Executável

### 1. Teste em Ambiente Limpo

Teste o executável em uma máquina **sem Python instalado** para garantir que todas as dependências estão incluídas.

**Ambiente de teste ideal:**
- Máquina virtual Windows limpa
- Computador de usuário final sem ferramentas de desenvolvimento
- Windows 10/11 recém-instalado

### 2. Verificações Essenciais

Execute todos os testes abaixo antes de distribuir:

**Inicialização:**
- [ ] O executável inicia sem erros
- [ ] Tempo de inicialização < 10 segundos
- [ ] Nenhuma janela de console aparece (modo windowed)
- [ ] A interface gráfica é exibida corretamente

**Funcionalidades Core:**
- [ ] A validação de licença funciona (válida e inválida)
- [ ] Campos de input aceitam texto corretamente
- [ ] Slider de limite funciona (50, 100, 500)
- [ ] Botão "Iniciar Extração" responde
- [ ] O navegador Chromium é iniciado corretamente (em background)

**Extração de Dados:**
- [ ] Busca no Google Maps funciona
- [ ] Dados são extraídos corretamente
- [ ] Tabela é atualizada em tempo real
- [ ] Barra de progresso funciona
- [ ] Botão "Parar" interrompe a extração
- [ ] Extração completa sem crashes

**Exportação:**
- [ ] Exportação Excel (.xlsx) funciona
- [ ] Exportação CSV funciona
- [ ] Arquivos são salvos corretamente
- [ ] Formatação Excel está correta (negrito, colunas ajustadas)
- [ ] Dados exportados estão completos e corretos

**Performance:**
- [ ] Uso de memória < 500MB durante operação
- [ ] Interface permanece responsiva
- [ ] Extração de 50 leads < 5 minutos
- [ ] Sem memory leaks após múltiplas extrações

**Tratamento de Erros:**
- [ ] Erro de licença exibe mensagem clara
- [ ] Erro de conexão é tratado graciosamente
- [ ] Logs são salvos em `lead_extractor.log`
- [ ] Erros não causam crash do aplicativo

### 3. Requisitos de Sistema

#### Para Usuários Finais (Executável)

**Sistema Operacional:**
- Windows 10 (64-bit) - Build 1809 ou superior
- Windows 11 (64-bit) - Todas as versões
- **Não suportado:** Windows 7, 8, 8.1, ou versões 32-bit

**Hardware Mínimo:**
- **Processador:** Intel Core i3 (3ª geração) ou AMD equivalente
- **Memória RAM:** 4GB
- **Espaço em Disco:** 500MB livres para instalação
- **Espaço Temporário:** 200MB adicionais para operação
- **Placa de Vídeo:** Qualquer (não requer GPU dedicada)
- **Resolução de Tela:** Mínimo 1280x720 pixels

**Hardware Recomendado:**
- **Processador:** Intel Core i5 (6ª geração ou superior) ou AMD Ryzen 3
- **Memória RAM:** 8GB ou mais
- **Espaço em Disco:** 1GB livre
- **Resolução de Tela:** 1920x1080 pixels (Full HD)
- **SSD:** Recomendado para melhor performance

**Conectividade:**
- **Internet:** Banda larga estável (mínimo 5 Mbps)
- **Firewall:** Permitir conexões HTTPS para google.com
- **Proxy:** Suporte a proxy HTTP/HTTPS (se necessário)

**Software:**
- **Nenhuma instalação adicional necessária**
- Não requer Python, Node.js, ou outras ferramentas
- Não requer instalação de navegadores
- Funciona "out of the box"

#### Para Desenvolvedores (Build)

**Sistema Operacional:**
- Windows 10/11 (para build Windows)
- Linux (para build Linux)
- macOS (para build macOS)
- **Nota:** Build deve ser feito na plataforma alvo

**Software Necessário:**
- Python 3.9, 3.10, 3.11 ou 3.12
- pip (gerenciador de pacotes Python)
- PyInstaller 5.0 ou superior
- Git (opcional, para controle de versão)

**Hardware Recomendado para Build:**
- **Processador:** Intel Core i5 ou superior
- **Memória RAM:** 8GB mínimo (16GB recomendado)
- **Espaço em Disco:** 2GB livres
- **SSD:** Altamente recomendado (build 3-5x mais rápido)

### 4. Compatibilidade e Limitações

**Sistemas Suportados:**
- ✅ Windows 10 (64-bit) - Build 1809+
- ✅ Windows 11 (64-bit) - Todas as versões
- ❌ Windows 7/8/8.1 (não suportado)
- ❌ Windows 32-bit (não suportado)
- ❌ Linux (requer build separado)
- ❌ macOS (requer build separado)

**Antivírus e Segurança:**
- ⚠️ Alguns antivírus podem marcar como falso positivo
- ⚠️ Windows Defender pode exigir confirmação na primeira execução
- ✅ Considere assinatura digital para distribuição comercial

**Limitações Conhecidas:**
- Primeira execução pode ser 2-3x mais lenta (extração de arquivos)
- Executável one-file cria pasta temporária em %TEMP%
- Requer permissões de escrita para criar logs e exportar dados
- Não funciona em ambientes sem acesso à internet

## Solução de Problemas

### Erro: "Failed to execute script"

**Causa:** Dependência faltando ou caminho incorreto

**Solução:**
1. Verifique se todas as dependências estão em `requirements.txt`
2. Execute com `--debug=all` para ver logs detalhados:
   ```bash
   pyinstaller --debug=all lead_extractor.spec
   ```

### Erro: "Playwright not found"

**Causa:** Navegadores do Playwright não incluídos

**Solução:**
1. Certifique-se de que `collect_data_files('playwright')` está no .spec
2. Verifique se os navegadores foram instalados:
   ```bash
   playwright install chromium
   ```

### Erro: "CustomTkinter theme not found"

**Causa:** Arquivos de tema do CustomTkinter não incluídos

**Solução:**
1. Certifique-se de que `collect_data_files('customtkinter')` está no .spec
2. Verifique se a linha `include_py_files=True` está presente

### Executável muito grande (>300MB)

**Soluções:**
1. Use compressão UPX (já habilitada)
2. Adicione mais bibliotecas à lista `excludes`
3. Considere usar modo one-folder ao invés de one-file

### Erro ao abrir arquivo Excel exportado

**Causa:** OpenPyXL não incluído corretamente

**Solução:**
1. Verifique se `openpyxl_hiddenimports` está em `all_hiddenimports`
2. Adicione explicitamente:
   ```python
   hiddenimports=['openpyxl.cell._writer'],
   ```

## Distribuição

### Arquivo Único (One-File)

Distribua apenas o arquivo `dist/LeadExtractor.exe` junto com:
- `license.key` (arquivo de licença)
- `README.md` (instruções de uso)

### Pasta (One-Folder)

Distribua toda a pasta `dist/LeadExtractor/` contendo:
- `LeadExtractor.exe`
- Todas as DLLs e dependências
- `license.key`
- `README.md`

### Criando Instalador (Opcional)

Para criar um instalador profissional, use ferramentas como:
- **Inno Setup** (Windows) - https://jrsoftware.org/isinfo.php
- **NSIS** (Windows) - https://nsis.sourceforge.io/
- **WiX Toolset** (Windows) - https://wixtoolset.org/

## Checklist de Build Final

Antes de distribuir o executável:

### Testes Funcionais
- [ ] Testado em ambiente limpo (sem Python)
- [ ] Todas as funcionalidades verificadas
- [ ] Extração de 50, 100 e 500 leads testada
- [ ] Exportação Excel e CSV testada
- [ ] Validação de licença (válida e inválida) testada
- [ ] Botão "Parar" funciona corretamente
- [ ] Tratamento de erros funciona

### Testes de Compatibilidade
- [ ] Testado em Windows 10 (64-bit)
- [ ] Testado em Windows 11 (64-bit)
- [ ] Testado com diferentes resoluções de tela
- [ ] Testado com antivírus ativo
- [ ] Testado em máquina com poucos recursos (4GB RAM)

### Performance
- [ ] Tamanho do executável aceitável (<200MB)
- [ ] Verificado uso de memória (<500MB)
- [ ] Tempo de inicialização aceitável (<10 segundos)
- [ ] Extração de 50 leads < 5 minutos
- [ ] Sem memory leaks após múltiplas extrações

### Documentação
- [ ] README.md atualizado com instruções
- [ ] BUILD_INSTRUCTIONS.md completo
- [ ] MANUAL_USUARIO.md para usuários finais
- [ ] Arquivo de licença de exemplo incluído
- [ ] Changelog documentado (se aplicável)

### Arquivos de Distribuição
- [ ] Executável gerado e testado
- [ ] license.key de exemplo criado
- [ ] Documentação em PDF (opcional)
- [ ] Arquivo de instalação (opcional)

### Segurança e Legal
- [ ] Código revisado para vulnerabilidades
- [ ] Sem credenciais ou dados sensíveis no código
- [ ] Licença de software definida
- [ ] Termos de uso documentados (se aplicável)

---

## Distribuição e Empacotamento

### Opção 1: Distribuição Simples (Arquivos Soltos)

**Estrutura de distribuição:**
```
LeadExtractor_v1.0/
├── LeadExtractor.exe          # Executável principal
├── license.key                # Arquivo de licença (exemplo ou real)
├── MANUAL_USUARIO.pdf         # Manual em PDF (opcional)
└── LEIA-ME.txt               # Instruções rápidas
```

**Arquivo LEIA-ME.txt:**
```
Google Maps Lead Extractor v1.0
================================

INSTALAÇÃO:
1. Extraia todos os arquivos para uma pasta
2. Certifique-se de que license.key está na mesma pasta
3. Execute LeadExtractor.exe

REQUISITOS:
- Windows 10/11 (64-bit)
- 4GB RAM mínimo
- Conexão com internet

SUPORTE:
- Consulte MANUAL_USUARIO.pdf para instruções completas
- Entre em contato: [seu email/site]

IMPORTANTE:
- Mantenha license.key na mesma pasta do executável
- Não compartilhe seu arquivo de licença
```

**Compactar para distribuição:**
```bash
# Criar arquivo ZIP
powershell Compress-Archive -Path LeadExtractor_v1.0 -DestinationPath LeadExtractor_v1.0.zip

# Ou usar 7-Zip para melhor compressão
7z a -tzip LeadExtractor_v1.0.zip LeadExtractor_v1.0\
```

### Opção 2: Instalador Profissional (Inno Setup)

**Instalar Inno Setup:**
1. Baixe de: https://jrsoftware.org/isinfo.php
2. Instale no Windows

**Criar script de instalação (installer.iss):**
```iss
[Setup]
AppName=Google Maps Lead Extractor
AppVersion=1.0.0
DefaultDirName={autopf}\LeadExtractor
DefaultGroupName=Lead Extractor
OutputDir=installer_output
OutputBaseFilename=LeadExtractor_Setup_v1.0
Compression=lzma2
SolidCompression=yes
ArchitecturesAllowed=x64
ArchitecturesInstallIn64BitMode=x64

[Files]
Source: "dist\LeadExtractor.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "license.key"; DestDir: "{app}"; Flags: ignoreversion
Source: "MANUAL_USUARIO.pdf"; DestDir: "{app}"; Flags: ignoreversion

[Icons]
Name: "{group}\Lead Extractor"; Filename: "{app}\LeadExtractor.exe"
Name: "{group}\Manual do Usuário"; Filename: "{app}\MANUAL_USUARIO.pdf"
Name: "{autodesktop}\Lead Extractor"; Filename: "{app}\LeadExtractor.exe"

[Run]
Filename: "{app}\LeadExtractor.exe"; Description: "Executar Lead Extractor"; Flags: nowait postinstall skipifsilent
```

**Compilar instalador:**
```bash
# Via linha de comando
"C:\Program Files (x86)\Inno Setup 6\ISCC.exe" installer.iss

# Ou abra installer.iss no Inno Setup e clique em "Compile"
```

### Opção 3: Instalador MSI (WiX Toolset)

Para ambientes corporativos que exigem MSI:

**Instalar WiX Toolset:**
```bash
# Via Chocolatey
choco install wixtoolset

# Ou baixe de: https://wixtoolset.org/
```

**Criar arquivo Product.wxs:**
```xml
<?xml version="1.0" encoding="UTF-8"?>
<Wix xmlns="http://schemas.microsoft.com/wix/2006/wi">
  <Product Id="*" Name="Lead Extractor" Language="1033" Version="1.0.0" 
           Manufacturer="Sua Empresa" UpgradeCode="PUT-GUID-HERE">
    <Package InstallerVersion="200" Compressed="yes" InstallScope="perMachine" />
    
    <MediaTemplate EmbedCab="yes" />
    
    <Directory Id="TARGETDIR" Name="SourceDir">
      <Directory Id="ProgramFiles64Folder">
        <Directory Id="INSTALLFOLDER" Name="LeadExtractor" />
      </Directory>
    </Directory>
    
    <ComponentGroup Id="ProductComponents" Directory="INSTALLFOLDER">
      <Component Id="MainExecutable">
        <File Source="dist\LeadExtractor.exe" />
      </Component>
      <Component Id="LicenseFile">
        <File Source="license.key" />
      </Component>
    </ComponentGroup>
    
    <Feature Id="ProductFeature" Title="Lead Extractor" Level="1">
      <ComponentGroupRef Id="ProductComponents" />
    </Feature>
  </Product>
</Wix>
```

**Compilar MSI:**
```bash
candle Product.wxs
light -out LeadExtractor.msi Product.wixobj
```

### Opção 4: Distribuição via Cloud

**Upload para cloud storage:**
```bash
# Google Drive, Dropbox, OneDrive, etc.
# Gere link de compartilhamento
# Forneça link aos clientes
```

**Vantagens:**
- ✅ Fácil distribuição
- ✅ Controle de versões
- ✅ Estatísticas de download
- ✅ Atualizações centralizadas

**Desvantagens:**
- ❌ Requer conta cloud
- ❌ Limites de armazenamento/banda
- ❌ Dependência de serviço terceiro

### Assinatura Digital (Recomendado para Produção)

**Por que assinar digitalmente:**
- ✅ Evita avisos de "Publisher Unknown"
- ✅ Reduz falsos positivos de antivírus
- ✅ Aumenta confiança dos usuários
- ✅ Necessário para distribuição corporativa

**Como obter certificado:**
1. Compre certificado de Code Signing
   - DigiCert, Sectigo, GlobalSign, etc.
   - Custo: $100-$500/ano
2. Instale o certificado no Windows
3. Assine o executável:

```bash
# Usando signtool (Windows SDK)
signtool sign /f "seu_certificado.pfx" /p "senha" /t http://timestamp.digicert.com LeadExtractor.exe

# Verificar assinatura
signtool verify /pa LeadExtractor.exe
```

### Versionamento

**Esquema de versão recomendado:**
```
MAJOR.MINOR.PATCH
1.0.0 - Primeira versão
1.0.1 - Correção de bugs
1.1.0 - Novas funcionalidades
2.0.0 - Mudanças incompatíveis
```

**Atualizar versão no código:**
```python
# Em main.py ou config.py
__version__ = "1.0.0"
__build_date__ = "2024-01-15"
```

**Atualizar versão no .spec:**
```python
# Em lead_extractor.spec
version='1.0.0',
```

### Changelog

**Manter arquivo CHANGELOG.md:**
```markdown
# Changelog

## [1.0.0] - 2024-01-15
### Adicionado
- Extração automatizada de leads do Google Maps
- Interface gráfica moderna com CustomTkinter
- Sistema de licenciamento
- Exportação Excel e CSV
- Proteção anti-bot

### Corrigido
- N/A (primeira versão)

### Conhecido
- Primeira execução pode ser lenta
- Alguns antivírus podem dar falso positivo
```

---

## Distribuição para Clientes

### Pacote Completo para Cliente

**Incluir:**
1. ✅ `LeadExtractor.exe` (executável)
2. ✅ `license.key` (licença do cliente)
3. ✅ `MANUAL_USUARIO.pdf` (manual em PDF)
4. ✅ `LEIA-ME.txt` (instruções rápidas)
5. ✅ `SUPORTE.txt` (informações de contato)

**Não incluir:**
- ❌ Código-fonte (.py)
- ❌ Arquivos de build (.spec, build/, dist/)
- ❌ Arquivos de desenvolvimento (.git, .venv)
- ❌ Logs ou dados de teste

### Email de Entrega ao Cliente

**Modelo de email:**
```
Assunto: Lead Extractor - Sua Licença e Download

Olá [Nome do Cliente],

Segue em anexo o Google Maps Lead Extractor v1.0.

ARQUIVOS INCLUÍDOS:
- LeadExtractor.exe (executável principal)
- license.key (sua licença válida até [data])
- MANUAL_USUARIO.pdf (instruções completas)

INSTALAÇÃO:
1. Extraia todos os arquivos para uma pasta
2. Execute LeadExtractor.exe
3. Consulte o manual para instruções detalhadas

REQUISITOS:
- Windows 10/11 (64-bit)
- 4GB RAM mínimo
- Conexão com internet

SUPORTE:
- Email: [seu email]
- WhatsApp: [seu número]
- Horário: Segunda a Sexta, 9h-18h

IMPORTANTE:
- Mantenha seu arquivo license.key seguro
- Não compartilhe sua licença
- Sua licença expira em: [data]

Qualquer dúvida, estou à disposição!

Atenciosamente,
[Seu Nome]
```

### Renovação de Licença

**Processo de renovação:**
1. Cliente solicita renovação
2. Gere novo `license.key` com nova data
3. Envie apenas o novo `license.key`
4. Cliente substitui o arquivo antigo
5. Não precisa baixar executável novamente

**Arquivo license.key renovado:**
```json
{
    "api_key": "GMLE-XXXX-XXXX-XXXX-XXXX",
    "expiration_date": "2025-12-31",
    "customer_name": "Nome do Cliente",
    "license_type": "commercial",
    "renewal_count": 1
}
```

## Suporte

Para problemas durante o build:
1. Verifique os logs em `build/LeadExtractor/warn-LeadExtractor.txt`
2. Execute com `--debug=all` para logs detalhados
3. Consulte a documentação do PyInstaller: https://pyinstaller.org/

## Notas Importantes

⚠️ **Antivírus:** Alguns antivírus podem marcar executáveis PyInstaller como suspeitos. Isso é um falso positivo comum. Considere assinar digitalmente o executável para produção.

⚠️ **Playwright:** O executável incluirá o navegador Chromium completo, o que aumenta significativamente o tamanho final.

⚠️ **Primeira Execução:** A primeira execução pode ser mais lenta devido à extração de arquivos temporários (modo one-file).

✅ **Compatibilidade:** O executável gerado no Windows só funcionará no Windows. Para Linux/Mac, é necessário gerar o executável na respectiva plataforma.
