#!/usr/bin/env python3
"""Build the four Portuguese career PDFs from one editorial data file."""

from __future__ import annotations

import json
from html import escape
from pathlib import Path

from weasyprint import HTML


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "docs" / "conteudo-editorial.json"
OUTPUT = ROOT / "output" / "pdf"
PHOTO = ROOT / "output" / "assets" / "retrato-profissional.png"


def e(value: str) -> str:
    return escape(value, quote=True)


def a(label: str, url: str) -> str:
    return f'<a href="{e(url)}">{e(label)}</a>'


def portrait(css_class: str, name: str) -> str:
    return (
        f'<img class="{e(css_class)}" src="{e(PHOTO.as_uri())}" '
        f'alt="Retrato profissional de {e(name)}">'
    )


def document(title: str, css: str, body: str) -> str:
    return (
        '<!doctype html><html lang="pt-BR"><head><meta charset="utf-8">'
        f"<title>{e(title)}</title><style>{css}</style></head><body>{body}</body></html>"
    )


COMMON = """
@font-face { font-family: Noto; src: url(file:///usr/share/fonts/truetype/noto/NotoSans-Regular.ttf); font-weight: 400; }
@font-face { font-family: Noto; src: url(file:///usr/share/fonts/truetype/noto/NotoSans-Bold.ttf); font-weight: 700; }
@font-face { font-family: Noto; src: url(file:///usr/share/fonts/truetype/noto/NotoSans-Italic.ttf); font-style: italic; }
:root { --navy:#101b2b; --ink:#192434; --muted:#536173; --teal:#187e85; --aqua:#6fe6da; --cream:#f7f5f0; --line:#d8dfdf; }
* { box-sizing:border-box; }
body { margin:0; font-family:Noto, sans-serif; color:var(--ink); }
a { color:inherit; text-decoration:none; border-bottom:1px solid currentColor; }
"""


DECK_CSS = COMMON + """
@page { size: 320mm 180mm; margin:0; }
.slide { width:320mm; height:180mm; padding:17mm 19mm; page-break-after:always; position:relative; overflow:hidden; }
.slide:last-child { page-break-after:auto; }
.dark { background:var(--navy); color:#f8faf9; }
.light { background:var(--cream); color:var(--navy); }
.eyebrow { font-size:10pt; letter-spacing:0.19em; text-transform:uppercase; font-weight:700; color:var(--teal); margin:0 0 7mm; }
.dark .eyebrow { color:var(--aqua); }
h1 { font-size:36pt; line-height:1.1; letter-spacing:-0.045em; margin:0 0 8mm; max-width:245mm; }
h2 { font-size:27pt; line-height:1.15; letter-spacing:-0.035em; margin:0 0 5mm; max-width:250mm; }
h3 { font-size:13pt; margin:0 0 3mm; }
p { margin:0; }
.lead { font-size:17pt; line-height:1.45; max-width:218mm; }
.slide-number { position:absolute; right:19mm; bottom:12mm; font-size:9pt; letter-spacing:0.12em; opacity:.65; }
.rail { position:absolute; top:17mm; bottom:17mm; right:19mm; width:2px; background:var(--aqua); opacity:.6; }
.hero-rule { height:2mm; width:43mm; background:var(--aqua); margin:11mm 0; }
.hero-footer { position:absolute; left:19mm; bottom:17mm; font-size:10pt; opacity:.8; }
.hero .lead { max-width:175mm; }
.hero h1 { max-width:178mm; }
.hero-photo { position:absolute; right:27mm; top:24mm; width:82mm; height:118mm; object-fit:cover; object-position:center 18%; border:1.5mm solid #69b9bc; border-radius:5mm; box-shadow:0 9mm 19mm rgba(0,0,0,.25); }
.hero-photo-caption { position:absolute; right:27mm; top:146mm; width:82mm; color:#bbd6d9; font-size:8.5pt; letter-spacing:.12em; text-align:right; }
.case-index { position:absolute; right:20mm; top:16mm; font-size:53pt; font-weight:700; opacity:.09; line-height:1; }
.case-grid { display:grid; grid-template-columns:1fr 1fr; gap:14mm; margin-top:5mm; }
.case-grid p, .case-wide p { font-size:12pt; line-height:1.55; }
.label { text-transform:uppercase; font-size:9pt; letter-spacing:.12em; font-weight:700; color:var(--teal); margin-bottom:3mm; }
.dark .label { color:var(--aqua); }
.case-wide { margin-top:6mm; border-top:1px solid var(--line); padding-top:5mm; }
.dark .case-wide { border-color:#445163; }
.flow { position:absolute; left:19mm; right:32mm; bottom:29mm; display:flex; gap:3mm; }
.flow-step { flex:1; border-top:1px solid #8db9bb; padding-top:2mm; font-size:8.5pt; letter-spacing:.02em; }
.flow-step strong { color:var(--teal); font-size:8pt; margin-right:2.5mm; }
.dark .flow-step { border-color:#5e9298; }
.dark .flow-step strong { color:var(--aqua); }
.chips { position:absolute; left:19mm; bottom:14mm; right:32mm; }
.chip { display:inline-block; background:#e4eeee; border-radius:20mm; padding:2mm 4mm; margin:0 2mm 2mm 0; font-size:9pt; }
.dark .chip { background:#213c46; }
.timeline { display:grid; grid-template-columns:repeat(4,1fr); gap:7mm; margin-top:12mm; }
.timeline article { border-top:2px solid var(--teal); padding-top:5mm; }
.timeline h3 { font-size:11pt; }
.timeline p { font-size:9.5pt; line-height:1.45; }
.contact { margin-top:11mm; display:flex; gap:9mm; font-size:11pt; }
.fine { font-size:9pt; line-height:1.5; color:var(--muted); }
.dark .fine { color:#bac7cc; }
"""


CV_CSS = COMMON + """
@page { size:A4; margin:16mm 18mm 16mm 18mm; }
body { font-size:9.3pt; line-height:1.45; }
header { border-bottom:2px solid var(--teal); padding-bottom:5mm; margin-bottom:5mm; min-height:39mm; padding-right:37mm; position:relative; }
.cv-photo { position:absolute; right:0; top:0; width:31mm; height:38mm; object-fit:cover; object-position:center 16%; border-radius:2mm; }
h1 { font-size:23pt; letter-spacing:-.04em; margin:0; color:var(--navy); }
.role-title { font-size:10.5pt; font-weight:700; color:var(--teal); margin-top:1mm; }
.contact-line { font-size:8.5pt; margin-top:3mm; }
h2 { font-size:10.5pt; text-transform:uppercase; letter-spacing:.1em; color:var(--teal); margin:6mm 0 2mm; padding-bottom:1mm; border-bottom:1px solid var(--line); }
h3 { font-size:10pt; margin:3.5mm 0 0; color:var(--navy); }
.meta { color:var(--muted); font-size:8.5pt; margin:.5mm 0 1.5mm; }
p { margin:0 0 2.5mm; }
ul { margin:1mm 0 3mm 5mm; padding:0; }
li { margin-bottom:1.3mm; padding-left:1mm; }
.entry { break-inside:avoid; }
.page-two { break-before:page; }
.skills { font-size:9pt; }
.closing { margin-top:4mm; font-size:8pt; color:var(--muted); }
"""


LETTER_CSS = COMMON + """
@page { size:A4; margin:17mm 22mm 17mm 22mm; }
body { font-size:10.1pt; line-height:1.51; }
.topline { color:var(--teal); text-transform:uppercase; letter-spacing:.15em; font-size:9pt; font-weight:700; }
h1 { font-size:22pt; letter-spacing:-.04em; line-height:1.17; color:var(--navy); margin:4mm 0 3mm; }
.author { font-size:9.5pt; color:var(--muted); border-bottom:2px solid var(--teal); padding-bottom:5mm; margin-bottom:7mm; }
p { margin:0 0 3.5mm; }
.signature { margin-top:5mm; font-weight:700; color:var(--navy); }
.foot { border-top:1px solid var(--line); padding-top:3mm; margin-top:5mm; font-size:8.3pt; color:var(--muted); }
.letter-head { position:relative; padding-right:37mm; }
.letter-photo { position:absolute; top:0; right:0; width:29mm; height:35mm; object-fit:cover; object-position:center 15%; border-radius:2mm; }
"""


TECH_LETTER_CSS = COMMON + """
@page { size:A4; margin:0; }
body { font-size:9.6pt; line-height:1.5; }
.tech-letter { width:210mm; height:297mm; position:relative; overflow:hidden; background:#f8f8f5; }
.tech-main { margin-left:58mm; padding:19mm 16mm 16mm 16mm; }
.tech-kicker { margin:0 0 8mm; color:var(--teal); text-transform:uppercase; font-size:8.5pt; font-weight:700; letter-spacing:.16em; }
.tech-main h1 { max-width:115mm; font-size:25pt; letter-spacing:-.045em; line-height:1.13; color:var(--navy); margin:0 0 6mm; }
.tech-intro { color:#36515c; font-size:11pt; line-height:1.45; font-weight:700; margin:0 0 7mm; }
.tech-rule { width:26mm; height:1.3mm; background:var(--teal); margin:0 0 8mm; }
.tech-main p { margin:0 0 4.3mm; }
.tech-main .salutation { font-weight:700; margin-bottom:3mm; }
.tech-main .signature { margin-top:6mm; font-weight:700; font-size:11pt; color:var(--navy); }
.tech-side { position:absolute; left:0; top:0; bottom:0; width:58mm; background:var(--navy); color:#e7f0ef; padding:17mm 8mm 14mm; }
.tech-photo { display:block; width:42mm; height:55mm; object-fit:cover; object-position:center 14%; border:1mm solid #72d7ce; border-radius:2mm; margin:0 0 9mm; }
.tech-side h2 { font-size:17pt; line-height:1.15; margin:0 0 2mm; letter-spacing:-.03em; }
.tech-side .side-title { font-size:8.5pt; color:#a8d9d9; line-height:1.45; margin:0 0 10mm; }
.tech-side .side-rule { width:14mm; height:1mm; background:#72d7ce; margin:0 0 6mm; }
.tech-side .side-label { text-transform:uppercase; letter-spacing:.15em; font-size:7.5pt; color:#72d7ce; font-weight:700; margin:0 0 5mm; }
.tech-side .side-item { border-top:1px solid #41606b; padding:3mm 0 4mm; font-size:8.5pt; line-height:1.4; }
.tech-side .side-item strong { display:block; color:#fff; font-size:9pt; }
.tech-side .side-contact { position:absolute; bottom:14mm; left:8mm; right:8mm; font-size:7.8pt; line-height:1.65; overflow-wrap:anywhere; }
.tech-side a { color:#d8efec; }
"""


def deck(data: dict) -> str:
    cases = data["cases"]
    pages = [
        f'<section class="slide dark hero"><div class="rail"></div><p class="eyebrow">Portfólio profissional · 2026</p>'
        f'<h1>{e(data["name"])}</h1><div class="hero-rule"></div>'
        f'<p class="lead">{e(data["thesis"])}</p>'
        f'{portrait("hero-photo", data["name"])}'
        '<span class="hero-photo-caption">ENGENHARIA · PRODUTO · AGENTES</span>'
        f'<p class="hero-footer">{e(data["title"])} &nbsp;·&nbsp; {e(data["contact"]["location"])}</p>'
        '<span class="slide-number">01 / 05</span></section>'
    ]
    for index, case in enumerate(cases, start=2):
        theme = "light" if index % 2 == 0 else "dark"
        chips = "".join(f'<span class="chip">{e(item)}</span>' for item in case["tags"])
        flow = "".join(
            f'<span class="flow-step"><strong>{step_index:02d}</strong>{e(step)}</span>'
            for step_index, step in enumerate(case["flow"], start=1)
        )
        pages.append(
            f'<section class="slide {theme}"><span class="case-index" aria-hidden="true">{index-1:02d}</span>'
            f'<p class="eyebrow">{e(case["category"])} · caso {index-1:02d}</p>'
            f'<h2>{e(case["headline"])}</h2><p class="lead">{e(case["summary"])}</p>'
            '<div class="case-grid">'
            f'<div><p class="label">Desafio</p><p>{e(case["challenge"])}</p></div>'
            f'<div><p class="label">Minha contribuição</p><p>{e(case["contribution"])}</p></div>'
            '</div><div class="case-wide"><p class="label">O que a evidência mostra</p>'
            f'<p>{e(case["evidence"])}</p></div><div class="flow">{flow}</div>'
            f'<div class="chips">{chips}</div>'
            f'<span class="slide-number">0{index} / 05</span></section>'
        )
    timeline = "".join(
        f'<article><h3>{e(item["name"])}</h3><p>{e(item["summary"])}</p></article>'
        for item in data["timeline"]
    )
    c = data["contact"]
    pages.append(
        '<section class="slide light"><p class="eyebrow">Percurso & próximo capítulo</p>'
        f'<h2>{e(data["closing_title"])}</h2><p class="lead">{e(data["closing"])}</p>'
        f'<div class="timeline">{timeline}</div>'
        '<div class="contact">'
        f'{a(c["email"], "mailto:" + c["email"])}'
        f'{a("LinkedIn", c["linkedin"])}{a("GitHub", c["github"])}'
        '</div>'
        '<p class="fine" style="margin-top:7mm">Seleciono problemas em que produto, arquitetura e operação precisam conversar.</p>'
        '<span class="slide-number">05 / 05</span></section>'
    )
    return document(f'Portfólio de {data["name"]}', DECK_CSS, "".join(pages))


def experience_entry(entry: dict) -> str:
    bullets = "".join(f"<li>{e(bullet)}</li>" for bullet in entry["bullets"])
    return (
        '<section class="entry">'
        f'<h3>{e(entry["organization"])} · {e(entry["role"])}</h3>'
        f'<p class="meta">{e(entry["period"])}</p><ul>{bullets}</ul></section>'
    )


def cv(data: dict) -> str:
    c = data["contact"]
    recent = "".join(experience_entry(item) for item in data["recent_experience"])
    prior = "".join(experience_entry(item) for item in data["prior_experience"])
    projects = "".join(experience_entry(item) for item in data["selected_projects"])
    education = "".join(
        f'<p><strong>{e(item["program"])}</strong> · {e(item["institution"])} · {e(item["period"])}</p>'
        for item in data["education"]
    )
    skills = "".join(
        f'<p class="skills"><strong>{e(group["name"])}:</strong> {e(group["items"])}</p>'
        for group in data["skills"]
    )
    body = (
        f'<header>{portrait("cv-photo", data["name"])}<h1>{e(data["name"])}</h1><p class="role-title">{e(data["title"])}</p>'
        f'<p class="contact-line">{e(c["location"])} · {a(c["email"], "mailto:" + c["email"])} · '
        f'{a("LinkedIn", c["linkedin"])} · {a("GitHub", c["github"])}</p></header>'
        f'<h2>Resumo</h2><p>{e(data["resume_summary"])}</p>'
        f'<h2>Experiência recente</h2>{recent}'
        f'<h2>Projetos selecionados</h2>{projects}'
        f'<section class="page-two"><h2>Trajetória anterior</h2>{prior}'
        f'<h2>Formação</h2>{education}'
        f'<h2>Competências</h2>{skills}'
        '<p class="closing">Portfólio e código selecionado no GitHub.</p></section>'
    )
    return document(f'Currículo de {data["name"]}', CV_CSS, body)


def letter(data: dict) -> str:
    paragraphs = "".join(f"<p>{e(paragraph)}</p>" for paragraph in data["letter"]["paragraphs"])
    c = data["contact"]
    body = (
        f'<div class="letter-head">{portrait("letter-photo", data["name"])}<p class="topline">Carta de apresentação</p>'
        f'<h1>{e(data["letter"]["title"])}</h1>'
        f'<p class="author">{e(data["name"])} · {e(data["title"])}</p></div>'
        f'{paragraphs}<p class="signature">{e(data["name"])}</p>'
        f'<p class="foot">{e(c["location"])} · {a(c["email"], "mailto:" + c["email"])} · '
        f'{a("LinkedIn", c["linkedin"])} · {a("GitHub", c["github"])}</p>'
    )
    return document(f'Carta de apresentação de {data["name"]}', LETTER_CSS, body)


def tech_letter(data: dict) -> str:
    c = data["contact"]
    content = data["letter_tech"]
    paragraphs = "".join(f"<p>{e(paragraph)}</p>" for paragraph in content["paragraphs"])
    body = (
        '<section class="tech-letter"><main class="tech-main">'
        '<p class="tech-kicker">Carta de apresentação · 2026</p>'
        f'<h1>{e(content["title"])}</h1>'
        f'<p class="tech-intro">{e(content["intro"])}</p>'
        '<div class="tech-rule" aria-hidden="true"></div>'
        '<p class="salutation">Olá,</p>'
        f'{paragraphs}<p class="signature">{e(data["name"])}</p></main>'
        '<aside class="tech-side">'
        f'{portrait("tech-photo", data["name"])}'
        f'<h2>{e(data["name"])}</h2><p class="side-title">{e(data["title"])}</p>'
        '<div class="side-rule" aria-hidden="true"></div>'
        '<p class="side-label">Linhas de trabalho</p>'
        '<p class="side-item"><strong>Saúde</strong>Produto e operação</p>'
        '<p class="side-item"><strong>IA aplicada</strong>Memória e avaliação</p>'
        '<p class="side-item"><strong>Agentes</strong>Rastreabilidade e limites</p>'
        '<div class="side-contact">'
        f'{a(c["email"], "mailto:" + c["email"])}<br>'
        f'{a("LinkedIn", c["linkedin"])}<br>{a("GitHub", c["github"])}'
        '</div></aside></section>'
    )
    return document(f'Carta tecnológica de {data["name"]}', TECH_LETTER_CSS, body)


def main() -> None:
    data = json.loads(DATA.read_text(encoding="utf-8"))
    if not PHOTO.is_file():
        raise FileNotFoundError(f"Retrato não encontrado: {PHOTO}")
    OUTPUT.mkdir(parents=True, exist_ok=True)
    for filename, html in (
        ("curriculo-apresentacao.pdf", deck(data)),
        ("curriculo-executivo.pdf", cv(data)),
        ("carta-apresentacao.pdf", letter(data)),
        ("carta-apresentacao-tecnologica.pdf", tech_letter(data)),
    ):
        HTML(string=html, base_url=str(ROOT)).write_pdf(
            OUTPUT / filename, pdf_variant="pdf/ua-1"
        )
        print(OUTPUT / filename)


if __name__ == "__main__":
    main()
