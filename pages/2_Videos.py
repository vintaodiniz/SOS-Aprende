import streamlit as st

from data.videos import VIDEOS
from data.ui import apply_styles, render_brand, render_disclaimer, render_page_heading


st.set_page_config(page_title="Vídeos | SOS Aprende", page_icon="🎥", layout="wide")
apply_styles()
render_brand()

render_page_heading(
    "Assistir",
    "Vídeos demonstrativos",
    "Os vídeos são incorporados a partir de links externos. Confira a fonte "
    "e prefira materiais de instituições reconhecidas.",
)

assuntos = ["Todos"] + list(dict.fromkeys(video["assunto"] for video in VIDEOS))
filtro = st.selectbox("Filtrar por assunto", assuntos)
videos_exibidos = [
    video for video in VIDEOS if filtro == "Todos" or video["assunto"] == filtro
]

for video in videos_exibidos:
    with st.container(border=True):
        st.markdown(f'<div class="sos-section-label">{video["assunto"]}</div>', unsafe_allow_html=True)
        st.subheader(video["titulo"])
        st.write(video["descricao"])
        if "SUBSTITUIR_" in video["url"]:
            st.info(
                "Link pendente: substitua o endereço placeholder em "
                "`data/videos.py` por uma URL válida de vídeo educativo."
            )
        else:
            st.video(video["url"])
    st.divider()

render_disclaimer()
