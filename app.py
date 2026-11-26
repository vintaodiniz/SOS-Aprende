import streamlit as st

from data.ui import apply_styles, render_brand, render_disclaimer


st.set_page_config(
    page_title="SOS Aprende",
    page_icon="🚑",
    layout="wide",
    initial_sidebar_state="expanded",
)
apply_styles()
render_brand()

st.markdown(
    '<section class="sos-hero"><div class="sos-hero-copy">'
    '<div class="sos-eyebrow">Educação em primeiros socorros</div>'
    "<h1>SOS Aprende</h1>"
    '<p class="sos-tagline">Aprenda. Assista. Saiba como agir.</p>'
    "<p>Informação clara para reconhecer situações de emergência, aprender "
    "cuidados iniciais e saber quando pedir ajuda profissional.</p>"
    '</div><div class="sos-hero-side"><div class="sos-hero-icon">🚑</div></div>'
    "</section>",
    unsafe_allow_html=True,
)

st.markdown('<div class="sos-section-label">O seu caminho de aprendizagem</div>', unsafe_allow_html=True)
st.subheader("Conhecimento que pode fazer a diferença")
colunas = st.columns(3)
pilares = [
    ("📘", "1. Aprender", "Consulte guias introdutórios sobre seis situações comuns."),
    ("▶", "2. Assistir", "Explore vídeos demonstrativos organizados por assunto."),
    ("✦", "3. Praticar", "Revise o que aprendeu com situações fictícias e quizzes."),
]
for coluna, (icone, titulo, descricao) in zip(colunas, pilares):
    with coluna:
        st.markdown(
            f'<div class="sos-card"><span class="sos-card-icon">{icone}</span>'
            f"<h3>{titulo}</h3><p>{descricao}</p></div>",
            unsafe_allow_html=True,
        )

st.markdown(
    '<div class="sos-section-label">Explore a plataforma</div>',
    unsafe_allow_html=True,
)
st.subheader("Por onde você quer começar?")
atalhos = st.columns(2)
paginas = [
    ("📘", "Guias", "Conheça os seis temas.", "pages/1_Guias.py"),
    ("🎥", "Vídeos", "Aprenda com demonstrações.", "pages/2_Videos.py"),
    ("🧠", "Simuladores", "Teste seus conhecimentos.", "pages/3_Simuladores.py"),
    ("🚨", "Emergência", "Veja os contatos essenciais.", "pages/4_Emergencia.py"),
]
for indice, (icone, titulo, descricao, pagina) in enumerate(paginas):
    coluna = atalhos[indice % len(atalhos)]
    with coluna:
        with st.container(border=True):
            st.markdown(
                f'<span class="sos-card-icon">{icone}</span>'
                f"<h3>{titulo}</h3><p>{descricao}</p>",
                unsafe_allow_html=True,
            )
            st.page_link(pagina, label=f"Abrir {titulo} →")

st.markdown('<div class="sos-section-label">Uma lembrança importante</div>', unsafe_allow_html=True)
render_disclaimer()
