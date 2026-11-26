import streamlit as st

from data.ui import apply_styles, render_brand, render_disclaimer, render_page_heading


st.set_page_config(page_title="Emergência | SOS Aprende", page_icon="🚨", layout="wide")
apply_styles()
render_brand()

render_page_heading(
    "Ajuda imediata",
    "Área de Emergência",
    "Se alguém estiver em perigo imediato, peça ajuda sem demora. "
    "Informe sua localização e siga as instruções do atendente.",
)

coluna_samu, coluna_bombeiros = st.columns(2)
with coluna_samu:
    st.markdown(
        '<div class="sos-contact"><div class="sos-contact-icon">🚑</div><h2>SAMU</h2>'
        '<div class="sos-contact-number">192</div>'
        "<p>Urgências clínicas, acidentes, mal súbito e situações que "
        "necessitam de atendimento médico de emergência.</p></div>",
        unsafe_allow_html=True,
    )
with coluna_bombeiros:
    st.markdown(
        '<div class="sos-contact"><div class="sos-contact-icon">🚒</div><h2>Corpo de Bombeiros</h2>'
        '<div class="sos-contact-number">193</div>'
        "<p>Incêndios, salvamentos, resgates e acidentes com necessidade "
        "de intervenção dos bombeiros.</p></div>",
        unsafe_allow_html=True,
    )

st.header("Durante a ligação")
for orientacao in [
    "Diga primeiro o endereço completo, município e um ponto de referência; confirme se é possível retornar a ligação.",
    "Descreva o que aconteceu, quantas pessoas precisam de ajuda e o estado atual delas, especialmente consciência e respiração.",
    "Informe riscos no local, como fogo, trânsito, eletricidade, violência ou produtos químicos.",
    "Responda às perguntas com calma, não desligue antes da orientação e siga as instruções do atendente.",
    "Se possível, peça a alguém para aguardar a equipe em um local visível e facilitar o acesso.",
]:
    st.markdown(f'<div class="sos-step">{orientacao}</div>', unsafe_allow_html=True)

st.markdown(
    '<div class="sos-alert"><strong>Prioridade:</strong> não se coloque em risco '
    "e não mova alguém com suspeita de trauma, salvo se houver perigo imediato "
    "no local. Siga a orientação recebida pelo telefone.</div>",
    unsafe_allow_html=True,
)
render_disclaimer()
