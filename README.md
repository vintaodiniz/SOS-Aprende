# SOS Aprende

**Aprenda. Assista. Saiba como agir.**

## Integrantes

- **Victor Diniz** — Matrícula: 04152899
- **Thiago Azevedo** — Matrícula: 04171947
- **Alexandre Brahuna** — Matrícula: 04153437

## Apresentação

O **SOS Aprende** é um projeto educativo desenvolvido em Python com Streamlit
para apresentar informações introdutórias sobre primeiros socorros. A
aplicação reúne guias, vídeos demonstrativos, quizzes e contatos de emergência
em uma interface simples e interativa.

O projeto não utiliza banco de dados, sistema de login ou cadastro.

## Conteúdo e funcionalidades

- **Página inicial:** apresenta a proposta do projeto e os pilares aprender,
  assistir e praticar.
- **Guias:** aborda engasgos, queimaduras, convulsões, desmaios, sangramentos
  e parada cardíaca. Cada tema inclui uma explicação, sinais de identificação,
  orientações gerais, ações a evitar e indicação de quando procurar
  atendimento de emergência.
- **Vídeos demonstrativos:** permite filtrar vídeos por assunto e assisti-los
  na aplicação.
- **Simuladores e quizzes:** apresenta situações fictícias de múltipla
  escolha, feedback educativo e pontuação ao final.
- **Área de Emergência:** destaca os contatos do SAMU (192) e do Corpo de
  Bombeiros (193), com orientações gerais para a ligação.

## Tecnologias

- Python
- Streamlit
- HTML e CSS

## Como executar

É necessário ter o Python instalado. Abra um terminal na pasta
`SOS-Aprende`, onde estão os arquivos `requirements.txt` e `app.py`. No
Windows, você pode abrir essa pasta no Explorador de Arquivos, clicar na barra
de endereço, digitar `powershell` e pressionar **Enter**.

No terminal, instale o Streamlit:

```powershell
python -m pip install -r .\requirements.txt
```

Após a instalação, inicie a aplicação:

```powershell
python -m streamlit run .\app.py
```

O Streamlit exibirá um endereço local no terminal, geralmente
`http://localhost:8501`. Abra esse endereço no navegador para acessar o
projeto. Para encerrar a aplicação, volte ao terminal e pressione **Ctrl+C**.

## Organização do projeto

- `app.py`: página inicial.
- `pages/`: páginas de Guias, Vídeos, Simuladores e Emergência.
- `data/`: conteúdos educativos, vídeos, perguntas e recursos compartilhados.
- `style/estilo.css`: estilos visuais da aplicação.
- `assets/`: diretório para materiais complementares.
- `requirements.txt`: dependências necessárias para execução.

## Aviso educativo

O conteúdo do SOS Aprende tem finalidade educativa e introdutória. Não
substitui cursos presenciais de primeiros socorros, avaliação de profissionais
de saúde nem atendimento de emergência. Em uma situação real, acione o serviço
adequado e siga as instruções do atendente.
