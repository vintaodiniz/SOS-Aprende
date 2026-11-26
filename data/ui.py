"""Utilitários compartilhados de apresentação."""

from pathlib import Path

import streamlit as st


ROOT_DIR = Path(__file__).resolve().parent.parent


def apply_styles() -> None:
    """Carrega a folha de estilos do projeto."""
    css_path = ROOT_DIR / "style" / "estilo.css"
    st.markdown(f"<style>{css_path.read_text(encoding='utf-8')}</style>", unsafe_allow_html=True)


def render_brand() -> None:
    """Exibe a identidade visual no menu lateral."""
    st.sidebar.markdown(
        '<div class="sos-brand">'
        '<div class="sos-brand-mark">✚</div>'
        '<div><div class="sos-brand-name">SOS Aprende</div>'
        '<div class="sos-brand-caption">Educação em primeiros socorros</div></div>'
        "</div>",
        unsafe_allow_html=True,
    )


def render_page_heading(eyebrow: str, title: str, description: str) -> None:
    """Exibe um cabeçalho padronizado para as páginas internas."""
    st.markdown(
        f'<div class="sos-page-heading"><div class="sos-eyebrow">{eyebrow}</div>'
        f"<h1>{title}</h1><p>{description}</p></div>",
        unsafe_allow_html=True,
    )


def render_disclaimer() -> None:
    """Exibe o aviso educativo e os contatos de emergência."""
    st.markdown(
        '<div class="sos-alert"><strong>Importante:</strong> este material é '
        "educativo e não substitui treinamento presencial nem atendimento "
        "médico. Em uma emergência, ligue para o SAMU (192) ou Bombeiros (193)."
        "</div>",
        unsafe_allow_html=True,
    )
