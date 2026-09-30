# Pesquisa editorial para currículo, portfólio e carta

Pesquisa realizada em 29 de setembro de 2026. Este arquivo distingue orientações publicadas de decisões editoriais para o caso de Richard. Não é prova de formação, cargo, impacto ou participação em projetos.

## O que as fontes sustentam

1. **O currículo precisa destacar ativos relevantes, e a carta precisa conectar qualificações ao interesse pela organização.** Harvard diferencia o resumo breve de experiência do currículo da narrativa de interesse e adequação na carta. Isso favorece uma abertura forte e específica em cada documento, sem repetir toda a cronologia na carta. Fonte: [Harvard FAS, Create a Resume/CV or Cover Letter](https://careerservices.fas.harvard.edu/channels/create-a-resume-cv-or-cover-letter/).
2. **Projetos, realizações e competências devem aparecer de modo verificável.** O MIT trata currículo, carta e portfólio como peças que ajudam a chegar à entrevista e orienta a evidenciar habilidades, conquistas e projetos. Fonte: [MIT Career Advising, Resumes, cover letters, portfolios, and CVs](https://capd.mit.edu/channels/make-a-resume-cover-letter-cv/).
3. **Sistemas de recrutamento variam, e a estrutura simples reduz risco de extração errada.** O Indeed recomenda títulos de seção convencionais, termos pertinentes à vaga e cautela com tabelas, colunas, cabeçalhos e rodapés, cujo conteúdo pode se dispersar na importação. Isso não é uma regra universal de que PDFs ou layouts elaborados sejam rejeitados; é uma orientação prática para a versão enviada por ATS. Fontes: [Indeed, ATS-Friendly Resume, atualizado em junho de 2026](https://www.indeed.com/career-advice/resumes-cover-letters/ats-resume) e [Indeed para empregadores, Resume Parsing, atualizado em março de 2026](https://www.indeed.com/hire/c/info/resume-parsing).
4. **Ordem de leitura e estrutura semântica importam para acessibilidade.** O W3C exige que uma sequência significativa seja determinável programaticamente; a Adobe recomenda criar o PDF a partir de fonte estruturada, marcar tags, conferir idioma, links, ordem de leitura e executar verificação de acessibilidade. Layouts complexos exigem inspeção manual. Fontes: [W3C, WCAG 2.2: Meaningful Sequence](https://www.w3.org/WAI/WCAG22/Understanding/meaningful-sequence), [W3C, Headings](https://www.w3.org/WAI/tutorials/page-structure/headings/) e [Adobe, Creating accessible PDFs, atualização de fevereiro de 2026](https://helpx.adobe.com/acrobat/using/creating-accessible-pdfs.html).

## Proposta editorial para este perfil

**Conceito:** engenheiro que transforma problemas de negócio em sistemas operáveis, com trajetória em saúde e experiência recente em plataformas, agentes de IA, memória, observabilidade e infraestrutura. A força dessa narrativa depende de casos concretos com escopo e evidência. Usar “arquiteto de IA” apenas se as entregas comprovarem responsabilidade arquitetural; não derivar o título de uma lista de ferramentas.

**Pacote de leitura:**

- **Currículo autoral visual, em PDF:** 3 a 5 páginas em formato de apresentação. Uma tese por página, hierarquia tipográfica forte, poucos casos com diagramas pequenos e linhas de resultado. Abertura com proposição de valor, depois trajetória, 2 ou 3 estudos de caso e formação/contato. O “impacto tecnológico” deve vir dos sistemas e das decisões demonstradas, não de efeitos gráficos. Identificar claramente contribuição individual, estágio da entrega e o que não foi medido.
- **Currículo sóbrio, em PDF:** 1 a 2 páginas, uma coluna e títulos convencionais (Resumo, Experiência, Projetos, Formação, Competências). Cronologia reversa, frases curtas com ação + escopo + resultado verificável, links selecionáveis e palavras pertinentes às vagas pretendidas. Esta é a versão para upload em ATS; adaptar apenas conteúdo verdadeiro à descrição de cada vaga.
- **Duas cartas de apresentação, em PDF:** uma versão tecnológica com linguagem visual autoral e outra sóbria, ambas com uma página e prontas para personalizar por empresa e vaga. Abrir com uma cena/problema real e o motivo de interesse, desenvolver exemplos de decisão e entrega, conectar as competências ao desafio do destinatário e fechar com convite objetivo. Uma “carta completa” genérica pode existir, mas não deve inventar empresa, vaga ou motivação particular.

**Escolhas de design:** usar paleta contida, contraste robusto, tipografia legível, espaço em branco e diagramas com legendas textuais. A versão visual pode ter mais expressão; ambas devem manter conteúdo real em texto, ordem de leitura coerente, metadados, idioma correto, links acessíveis e tags PDF quando a ferramenta permitir. Ao exportar, conferir extração de texto, navegação por teclado e a árvore de tags; `pdftotext` sozinho não prova acessibilidade.

**Conteúdo que provoca curiosidade:** substituir listas extensas de tecnologias por decisões memoráveis: problema; restrição; papel de Richard; solução; evidência observável; aprendizado. Um caso MyCareforce pode mostrar escala operacional e limites de produção; Record4Me pode mostrar arquitetura de memória, proveniência e controle de acesso; a formação FIAP pode mostrar aplicação acadêmica. Cada caso requer confirmação de autoria, datas, status e permissão para divulgar detalhes.

## Auditoria dos currículos existentes

Fontes locais: [`README_PT.md`](../README_PT.md), [`README.md`](../README.md), [`RESUME_1PAGE_PT.md`](../RESUME_1PAGE_PT.md) e quatro PDFs na raiz do repositório. Estes documentos são relatos prévios, não comprovação externa.

| Item | Evidência observada | Tratamento recomendado |
|---|---|---|
| Atualidade | Os PDFs foram criados em 3 de abril de 2025. `README_PT.md` e `README.md` dizem “Sami, janeiro de 2022 — presente (3 anos e 4 meses)”. | Confirmar vínculo e datas atuais; remover duração fixa junto de “presente”. |
| Trabalho recente | Nenhuma das quatro fontes Markdown menciona MyCareforce, Record4Me ou FIAP. | Inserir apenas após mapear evidências e natureza do vínculo/projeto. |
| Métricas | `RESUME_1PAGE_PT.md` apresenta nove percentuais: 40%, 35%, 60%, 25%, 30%, 15%, 28%, 45%, 30%. | Não publicar como resultados demonstrados sem fonte, período, método e atribuição. Preferir resultado qualitativo preciso quando não houver medição. |
| Certificações | A versão de uma página lista AWS Solutions Architect Associate, MongoDB Certified Developer e CSM; o currículo longo não lista essas certificações. | Confirmar credenciais, emissor, situação e validade antes de publicar. |
| Formação anterior | A versão longa usa “Bacharelado em Tecnologia da Informação/Sistemas de Informação”; a curta usa “Bacharelado em Sistemas de Informação”. | Confirmar nome oficial no diploma ou histórico. |
| Identificação | O cabeçalho usa “Richard Ros”; o repositório e links usam “richarddaros”. | Confirmar o nome profissional preferido antes de finalizar. |
| Acessibilidade | `pdfinfo` dos PDFs PT de 1 e 3 páginas mostra `Tagged: no`; o PDF longo PT é gerado com `wkhtmltopdf`. | Exportar novos PDFs com fonte semântica e verificar tags/ordem de leitura; não alegar conformidade sem auditoria. |
| Densidade | O currículo longo relaciona muitas linguagens, plataformas e ferramentas sem vincular cada uma a um caso. | Selecionar competências com evidência recente e relevância para o cargo. |

## Trajetória e formação: limites desta leitura

- O **usuário relatou diretamente** que começou em 2026 uma faculdade de agentes autônomos na FIAP. Registrar como “em andamento desde 2026” apenas com o nome oficial do curso e o tipo de formação confirmados; evitar inferir graduação, pós-graduação ou certificado.
- Os currículos existentes registram passagens por Sami, Cogna Educação, dr.consulta, Great Place to Work Brasil, ISPM, Clickon e Lidermidia. Datas, cargos e realizações precisam de revisão com Richard e, quando possível, registros primários.
- A investigação deste arquivo não examina contribuições recentes no GitHub. Outros mapeamentos de projeto devem identificar repositório, PR/commit, autoria e estado de merge/deploy separadamente; não converter número de PRs em impacto empresarial.

## Critérios de aceitação editorial

1. Toda métrica tem fonte e contexto, ou é removida.
2. Cada projeto informa papel, contribuição, período, tecnologia realmente usada e nível de comprovação.
3. O resumo de abertura permanece inteligível sem conhecer siglas internas.
4. As duas versões do currículo e as duas cartas mantêm narrativa coerente sem copiar parágrafos entre si.
5. O PDF tem texto selecionável, links funcionais, ordem de leitura lógica, idioma e metadados; tags e contraste são inspecionados.
6. A versão sóbria mantém uma coluna e seções usuais para reduzir risco de parsing em ATS.
