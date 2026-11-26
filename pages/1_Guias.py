from pathlib import Path
import unicodedata

import streamlit as st

from data.conteudos import CONTEUDOS
from data.ui import apply_styles, render_brand, render_disclaimer, render_page_heading


st.set_page_config(page_title="Guias | SOS Aprende", page_icon="📘", layout="wide")
apply_styles()
render_brand()

render_page_heading(
    "Aprender",
    "Guias de primeiros socorros",
    "Orientações introdutórias para reconhecer sinais e buscar ajuda. "
    "Em uma situação real, priorize a segurança do local e siga o atendente.",
)

assunto = st.selectbox("Escolha um assunto", list(CONTEUDOS))
conteudo = CONTEUDOS[assunto]

st.markdown(f'<div class="sos-section-label">Guia selecionado</div>', unsafe_allow_html=True)
st.subheader(assunto)

explicacao_coluna, sinais_coluna = st.columns([1, 1])
with explicacao_coluna:
    with st.container(border=True):
        st.markdown(
            '<div class="sos-section-label">Entenda</div>',
            unsafe_allow_html=True,
        )
        st.write(conteudo["explicacao"])
with sinais_coluna:
    with st.container(border=True):
        st.markdown(
            '<div class="sos-section-label">Reconheça os sinais</div>',
            unsafe_allow_html=True,
        )
        for sinal in conteudo["sinais"]:
            st.markdown(f"- {sinal}")

st.markdown('<div class="sos-section-label">Orientação inicial</div>', unsafe_allow_html=True)
st.subheader("Como agir com segurança")
for orientacao in conteudo["como_agir"]:
    st.markdown(
        f'<div class="sos-step">{orientacao}</div>',
        unsafe_allow_html=True,
    )

st.markdown('<div class="sos-section-label">Atenção</div>', unsafe_allow_html=True)
st.subheader("O que não fazer")
for alerta in conteudo["nao_fazer"]:
    st.markdown(f"- {alerta}")

image_dir = Path(__file__).resolve().parent.parent / "assets" / "imagens"
slug = unicodedata.normalize("NFKD", assunto.lower()).encode("ascii", "ignore").decode()
slug = slug.replace(" ", "_")
images = [image_dir / f"{slug}{extension}" for extension in (".png", ".jpg", ".jpeg", ".webp")]
image = next((candidate for candidate in images if candidate.is_file()), None)
if image:
    st.image(str(image), caption=f"Imagem educativa: {assunto}")

st.subheader("Quando procurar atendimento de emergência")
st.markdown(
    f'<div class="sos-alert"><strong>Procure ajuda imediatamente quando:</strong><br>'
    f'{conteudo["emergencia"]}</div>',
    unsafe_allow_html=True,
)
render_disclaimer()
