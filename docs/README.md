# Portfólio profissional de Richard Ros

## Leitura recomendada

1. [Biografia profissional e trajetória](biografia-profissional.md) — narrativa completa, projetos, estudos e fontes.
2. [Atuação na MyCareforce](atuacao-mycareforce.md) — síntese pública do último ano e limites das alegações.
3. [Record4Me e projetos pessoais](atuacao-record4me-e-projetos.md) — projetos, estudos aplicados e estágio das entregas.
4. [Pesquisa sobre currículos e carta](pesquisa-curriculo.md) — recomendações, links e auditoria dos currículos antigos.
5. [Conteúdo editorial dos PDFs](conteudo-editorial.json) — seleção em linguagem de apresentação.

Os quatro arquivos finais estão em [`../output/pdf/`](../output/pdf/): `curriculo-apresentacao.pdf` (cinco páginas em formato de apresentação), `curriculo-executivo.pdf` (duas páginas A4), `carta-apresentacao-tecnologica.pdf` (uma página A4) e `carta-apresentacao.pdf` (uma página A4, versão sóbria). O retrato tratado, fornecido pelo titular, está em [`../output/assets/retrato-profissional.png`](../output/assets/retrato-profissional.png).

## Escopo público

Este repositório é público. Os resumos acima não incluem links, hashes, caminhos ou detalhes operacionais de repositórios privados. O levantamento técnico completo fica em notas locais do titular, fora do Git. Os PDFs e a fotografia foram preparados para este portfólio profissional.

## Regeração

O gerador está em [`../scripts/build_pdfs.py`](../scripts/build_pdfs.py), usa WeasyPrint 66 e fontes Noto Sans instaladas neste ambiente. Após editar `conteudo-editorial.json`, execute:

```bash
uv run --with 'weasyprint==66.0' python scripts/build_pdfs.py
```

O script gera PDF/UA-1 com texto selecionável. A marcação técnica e a extração de texto foram conferidas; isso não substitui uma auditoria completa de acessibilidade com leitor de tela.
