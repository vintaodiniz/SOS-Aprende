import streamlit as st

from data.perguntas import PERGUNTAS
from data.ui import apply_styles, render_brand, render_disclaimer, render_page_heading


st.set_page_config(page_title="Simuladores | SOS Aprende", page_icon="🧠", layout="wide")
apply_styles()
render_brand()


def reiniciar_quiz() -> None:
    st.session_state.quiz_indice = 0
    st.session_state.quiz_respostas = {}
    st.session_state.quiz_finalizado = False


if "quiz_indice" not in st.session_state:
    reiniciar_quiz()

render_page_heading(
    "Praticar",
    "Simuladores e quizzes",
    "Leia cada situação fictícia e escolha a alternativa mais segura. "
    "O quiz é educativo e não substitui treinamento prático.",
)

if st.session_state.quiz_finalizado:
    acertos = sum(
        resposta == pergunta["resposta_correta"]
        for resposta, pergunta in zip(
            st.session_state.quiz_respostas.values(), PERGUNTAS
        )
    )
    st.success(f"Quiz concluído! Sua pontuação: {acertos} de {len(PERGUNTAS)}.")
    if st.button("Reiniciar quiz", type="primary"):
        reiniciar_quiz()
        st.rerun()
else:
    indice = st.session_state.quiz_indice
    pergunta = PERGUNTAS[indice]
    st.progress(
        (indice + 1) / len(PERGUNTAS),
        text=f"Pergunta {indice + 1} de {len(PERGUNTAS)}",
    )
    st.markdown(
        f'<div class="sos-section-label">{pergunta["tema"]}</div>',
        unsafe_allow_html=True,
    )
    st.subheader(pergunta["situacao"])

    resposta_existente = st.session_state.quiz_respostas.get(indice)
    with st.container(border=True):
        with st.form(key=f"quiz_form_{indice}"):
            resposta = st.radio(
                "Escolha a alternativa mais segura",
                pergunta["alternativas"],
                index=resposta_existente,
                key=f"quiz_radio_{indice}",
            )
            enviado = st.form_submit_button("Verificar resposta", type="primary")

    if enviado and resposta is not None:
        indice_resposta = pergunta["alternativas"].index(resposta)
        st.session_state.quiz_respostas[indice] = indice_resposta
        resposta_existente = indice_resposta
    elif enviado:
        st.warning("Selecione uma alternativa antes de verificar a resposta.")

    if resposta_existente is not None:
        if resposta_existente == pergunta["resposta_correta"]:
            st.markdown(
                f'<div class="sos-success"><strong>Correto.</strong> '
                f'{pergunta["explicacao"]}</div>',
                unsafe_allow_html=True,
            )
        else:
            st.markdown(
                f'<div class="sos-alert"><strong>Não é a alternativa mais segura.</strong> '
                f'{pergunta["explicacao"]}</div>',
                unsafe_allow_html=True,
            )
        rotulo = "Ver resultado" if indice == len(PERGUNTAS) - 1 else "Próxima pergunta"
        if st.button(rotulo, type="primary", key=f"quiz_next_{indice}"):
            if indice == len(PERGUNTAS) - 1:
                st.session_state.quiz_finalizado = True
            else:
                st.session_state.quiz_indice += 1
            st.rerun()

render_disclaimer()
