# Instruções para Geração de Currículos em PDF

Este repositório contém arquivos para gerar versões profissionais de currículos em PDF a partir de arquivos Markdown. Abaixo estão as instruções para instalar as dependências necessárias e gerar os PDFs.

## Requisitos

Para gerar os PDFs, você precisará instalar as seguintes ferramentas:

- **Pandoc**: Conversor universal de documentos
- **wkhtmltopdf**: Ferramenta para converter HTML em PDF
- **LaTeX** (opcional, para alguns formatos avançados)

## Instalação das Dependências

### No Ubuntu/Debian

```bash
# Atualizar repositórios e instalar Pandoc
sudo apt-get update
sudo apt-get install -y pandoc

# Instalar wkhtmltopdf
sudo apt-get install -y wkhtmltopdf

# Instalar LaTeX (opcional, para alguns formatos)
sudo apt-get install -y texlive-xetex
```

### No macOS (usando Homebrew)

```bash
# Instalar Homebrew (se ainda não estiver instalado)
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Instalar Pandoc
brew install pandoc

# Instalar wkhtmltopdf
brew install wkhtmltopdf
```

### No Windows

1. **Pandoc**: Baixe e instale a partir de [https://pandoc.org/installing.html](https://pandoc.org/installing.html)
2. **wkhtmltopdf**: Baixe e instale a partir de [https://wkhtmltopdf.org/downloads.html](https://wkhtmltopdf.org/downloads.html)

## Estrutura do Projeto

- `README.md` - Currículo em inglês (formato Markdown)
- `README_PT.md` - Currículo em português (formato Markdown)
- `resume.css` - Estilos CSS para o PDF
- `resume-template.html` - Template HTML para conversão
- `curriculum_en_pro.pdf` - Versão em inglês do currículo em PDF
- `curriculum_pt_pro.pdf` - Versão em português do currículo em PDF

## Comandos para Gerar os PDFs

### Versão em Português

```bash
pandoc README_PT.md -o curriculum_pt_pro.pdf \
  --pdf-engine=wkhtmltopdf \
  --pdf-engine-opt=--margin-top --pdf-engine-opt=5 \
  --pdf-engine-opt=--margin-bottom --pdf-engine-opt=5 \
  --pdf-engine-opt=--margin-left --pdf-engine-opt=10 \
  --pdf-engine-opt=--margin-right --pdf-engine-opt=10 \
  --template=resume-template.html \
  --css=resume.css \
  --metadata title="Currículo - Richard Ros"
```

### Versão em Inglês

```bash
pandoc README.md -o curriculum_en_pro.pdf \
  --pdf-engine=wkhtmltopdf \
  --pdf-engine-opt=--margin-top --pdf-engine-opt=5 \
  --pdf-engine-opt=--margin-bottom --pdf-engine-opt=5 \
  --pdf-engine-opt=--margin-left --pdf-engine-opt=10 \
  --pdf-engine-opt=--margin-right --pdf-engine-opt=10 \
  --template=resume-template.html \
  --css=resume.css \
  --metadata title="Resume - Richard Ros"
```

## Personalização

### Ajustar Margens

Você pode ajustar as margens de duas maneiras:

1. **No comando Pandoc**:
   - Altere os valores após `--pdf-engine-opt=` para ajustar as margens em milímetros
   - Exemplo: `--pdf-engine-opt=--margin-left --pdf-engine-opt=15` para uma margem esquerda de 15mm

2. **No arquivo CSS**:
   - Edite o arquivo `resume.css` e ajuste os valores de padding e margin
   - Para margens de impressão, ajuste a regra `@page { margin: ... }`

### Modificar Estilos

Para alterar a aparência do PDF:

1. Edite o arquivo `resume.css` para ajustar cores, fontes, espaçamentos, etc.
2. Regenere os PDFs usando os comandos acima

## Solução de Problemas

### Emojis não aparecem no PDF

Os emojis podem não ser renderizados corretamente em alguns sistemas. Se isso acontecer, você pode:
- Remover os emojis do arquivo Markdown
- Substituí-los por ícones FontAwesome (requer modificação do template HTML)

### Erros de Margem

Se o conteúdo estiver sendo cortado nas bordas:
- Aumente os valores das margens nos comandos ou no CSS
- Reduza o tamanho da fonte no CSS

### Fontes não carregam

Se as fontes personalizadas não estiverem sendo aplicadas:
- Verifique se a conexão com a internet está funcionando (para fontes do Google)
- Considere incluir as fontes localmente no projeto
