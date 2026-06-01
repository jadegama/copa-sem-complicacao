import streamlit as st
import pandas as pd

# ==============================
# CONFIGURAÇÃO DA PÁGINA
# ==============================

st.set_page_config(
    page_title="Copa sem Complicação",
    page_icon="⚽",
    layout="wide"
)

# ==============================
# CSS PERSONALIZADO
# ==============================

st.markdown(
    """
<style>

/* Fundo geral */
.stApp {
    background: #F8FAFC;
}

/* Espaçamento principal */
.block-container {
    padding-top: 2rem;
    padding-bottom: 3rem;
}

/* Capa */
.hero-card {
    background: linear-gradient(135deg, #022C22 0%, #064E3B 45%, #047857 100%);
    padding: 2.5rem;
    border-radius: 26px;
    color: white;
    box-shadow: 0px 16px 40px rgba(15, 23, 42, 0.22);
    margin-bottom: 2rem;
    border: 1px solid rgba(255,255,255,0.12);
}

/* Título da capa */
.hero-title {
    font-size: 3.35rem;
    font-weight: 900;
    letter-spacing: -1px;
    margin-bottom: 1.2rem;
    line-height: 1.1;
    text-shadow: 0px 4px 16px rgba(0, 0, 0, 0.35);
}

.hero-white {
    color: #FFFFFF !important;
}

.hero-highlight {
    color: #FBBF24 !important;
}

/* Texto da capa */
.hero-subtitle {
    color: #F8FAFC !important;
    font-size: 1.18rem;
    line-height: 1.7;
    max-width: 980px;
    text-shadow: 0px 2px 8px rgba(0, 0, 0, 0.22);
}

/* Cards da página inicial */
.info-card {
    background-color: white;
    padding: 1.35rem;
    border-radius: 20px;
    box-shadow: 0px 8px 22px rgba(15, 23, 42, 0.08);
    border-left: 6px solid #FBBF24;
    height: 100%;
}

.info-card h3 {
    color: #064E3B;
    margin-bottom: 0.7rem;
}

.info-card p {
    color: #475569;
    line-height: 1.5;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background-color: #064E3B;
}

section[data-testid="stSidebar"] * {
    color: white;
}

/* Inputs */
.stTextInput input {
    border-radius: 14px;
}

.stSelectbox div {
    border-radius: 14px;
}

/* Métricas */
[data-testid="stMetricValue"] {
    color: #047857;
    font-weight: 850;
}

[data-testid="stMetricLabel"] {
    color: #0F172A;
}

/* Botões */
.stButton button {
    border-radius: 14px;
    border: 1px solid #047857;
    color: #064E3B;
    font-weight: 700;
}

.stButton button:hover {
    border-color: #FBBF24;
    color: #047857;
}

/* Textos gerais */
h1, h2, h3 {
    color: #0F172A;
}

p, li {
    color: #334155;
}

/* Containers */
[data-testid="stVerticalBlockBorderWrapper"] {
    border-radius: 18px;
}

</style>
""",
    unsafe_allow_html=True
)

# ==============================
# CARREGAR DADOS
# ==============================

@st.cache_data
def carregar_duvidas():
    df = pd.read_csv("duvidas_copa_sem_complicacao.csv")
    df.columns = df.columns.str.strip()
    return df


@st.cache_data
def carregar_selecoes():
    df = pd.read_csv("selecoes_copa.csv")
    df.columns = df.columns.str.strip()
    return df


df_duvidas = carregar_duvidas()
df_selecoes = carregar_selecoes()

# ==============================
# SIDEBAR
# ==============================

st.sidebar.markdown("## ⚽ Copa sem Complicação")
st.sidebar.write("Um app educativo para entender a Copa de forma simples, visual e acessível.")

pagina = st.sidebar.radio(
    "Navegue pelo projeto:",
    [
        "🏠 Início",
        "🔎 Dúvidas do jogo",
        "🏆 Seleções",
        "⚖️ Comparar seleções",
        "📌 Sobre o projeto"
    ]
)

# ==============================
# PÁGINA INICIAL
# ==============================

if pagina == "🏠 Início":

    st.markdown(
        """
<div class="hero-card">
    <div class="hero-title">
        <span class="hero-white">⚽ Copa sem </span><span class="hero-highlight">Complicação</span>
    </div>
    <div class="hero-subtitle">
        Um guia simples para quem quer assistir à Copa entendendo o que está acontecendo —
        das regras às histórias das seleções, sem termos complicados.
    </div>
</div>
""",
        unsafe_allow_html=True
    )

    st.markdown("### Dados e tecnologia também podem simplificar experiências populares.")

    st.write(
        """
        O **Copa sem Complicação** foi pensado para quem quer acompanhar a Copa do Mundo,
        mas não entende muito de futebol. A proposta é traduzir o “futebolês” em explicações
        simples, humanas e fáceis de consultar.
        """
    )

    st.markdown("---")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown(
            """
<div class="info-card">
    <h3>🔎 Tire dúvidas</h3>
    <p>Entenda termos como VAR, impedimento, pênalti, saldo de gols, acréscimos e classificação.</p>
</div>
""",
            unsafe_allow_html=True
        )

    with col2:
        st.markdown(
            """
<div class="info-card">
    <h3>🏆 Conheça seleções</h3>
    <p>Veja títulos, participações, curiosidades e resumos históricos de seleções importantes.</p>
</div>
""",
            unsafe_allow_html=True
        )

    with col3:
        st.markdown(
            """
<div class="info-card">
    <h3>⚖️ Compare dados</h3>
    <p>Escolha duas seleções e veja informações lado a lado de forma clara e objetiva.</p>
</div>
""",
            unsafe_allow_html=True
        )

    st.markdown("### Visão geral do projeto")

    col4, col5, col6 = st.columns(3)

    with col4:
        st.metric("Dúvidas cadastradas", len(df_duvidas))

    with col5:
        st.metric("Seleções cadastradas", len(df_selecoes))

    with col6:
        st.metric("Categorias de dúvidas", df_duvidas["categoria"].nunique())

    st.markdown("---")

    col7, col8 = st.columns(2)

    with col7:
        with st.container(border=True):
            st.markdown("### Como usar")
            st.write(
                """
                1. Acesse **Dúvidas do jogo** para entender regras e termos do futebol.  
                2. Acesse **Seleções** para conhecer títulos e curiosidades.  
                3. Use **Comparar seleções** para visualizar duas seleções lado a lado.  
                4. Acesse **Sobre o projeto** para entender a proposta e as tecnologias usadas.
                """
            )

    with col8:
        with st.container(border=True):
            st.markdown("### Diferencial")
            st.write(
                """
                Mais do que reunir informações sobre futebol, o projeto organiza uma
                **base de conhecimento** para transformar dados e explicações em uma
                experiência simples para o usuário.
                """
            )

# ==============================
# PÁGINA DE DÚVIDAS
# ==============================

elif pagina == "🔎 Dúvidas do jogo":

    st.markdown(
        """
<div class="hero-card">
    <div class="hero-title">
        <span class="hero-white">🔎 Dúvidas do </span><span class="hero-highlight">jogo</span>
    </div>
    <div class="hero-subtitle">
        Pesquise uma palavra-chave ou filtre por categoria para encontrar explicações simples
        sobre regras, termos e situações comuns do futebol.
    </div>
</div>
""",
        unsafe_allow_html=True
    )

    col_busca, col_categoria = st.columns([2, 1])

    with col_busca:
        termo_busca = st.text_input(
            "Digite uma palavra-chave:",
            placeholder="Exemplo: impedimento, VAR, pênalti, classificação, cartão..."
        )

    with col_categoria:
        categorias = ["Todas"] + sorted(df_duvidas["categoria"].dropna().unique().tolist())

        categoria_escolhida = st.selectbox(
            "Filtrar por categoria:",
            categorias
        )

    df_filtrado = df_duvidas.copy()

    if categoria_escolhida != "Todas":
        df_filtrado = df_filtrado[df_filtrado["categoria"] == categoria_escolhida]

    if termo_busca:
        termo = termo_busca.lower()

        df_filtrado = df_filtrado[
            df_filtrado.apply(
                lambda linha: termo in " ".join(
                    linha.astype(str).str.lower().tolist()
                ),
                axis=1
            )
        ]

    st.markdown("### Resultado da busca")

    if df_filtrado.empty:
        st.warning(
            "Não encontrei nenhuma dúvida com esse termo. Tente pesquisar outra palavra, como 'gol', 'cartão', 'VAR' ou 'classificação'."
        )

    else:
        st.success(f"{len(df_filtrado)} dúvida(s) encontrada(s).")

        pergunta_escolhida = st.selectbox(
            "Escolha uma dúvida:",
            df_filtrado["pergunta"].tolist()
        )

        item = df_filtrado[df_filtrado["pergunta"] == pergunta_escolhida].iloc[0]

        pergunta = item["pergunta"]
        categoria = item["categoria"]
        nivel = item["nivel"]
        resposta = item["resposta"]
        exemplo = item["exemplo"]

        st.markdown("---")

        with st.container(border=True):
            st.markdown(f"## {pergunta}")

            col_tag1, col_tag2 = st.columns([1, 1])

            with col_tag1:
                st.markdown(f"**Categoria:** `{categoria}`")

            with col_tag2:
                st.markdown(f"**Nível:** `{nivel}`")

            st.markdown("### ✅ Resposta simples")
            st.info(resposta)

            st.markdown("### 💡 Exemplo prático")
            st.warning(exemplo)

    st.caption("Projeto educativo criado para explicar a Copa de forma simples, acessível e humana.")

# ==============================
# PÁGINA DE HISTÓRIA DAS SELEÇÕES
# ==============================

elif pagina == "🏆 Seleções":

    st.markdown(
        """
<div class="hero-card">
    <div class="hero-title">
        <span class="hero-white">🏆 </span><span class="hero-highlight">Seleções</span>
    </div>
    <div class="hero-subtitle">
        Consulte títulos, participações, curiosidades e resumos históricos das principais
        seleções em Copas do Mundo.
    </div>
</div>
""",
        unsafe_allow_html=True
    )

    col_busca, col_continente = st.columns([2, 1])

    with col_busca:
        termo_selecao = st.text_input(
            "Pesquise uma seleção:",
            placeholder="Exemplo: Brasil, Argentina, França, Marrocos..."
        )

    with col_continente:
        continentes = ["Todos"] + sorted(df_selecoes["continente"].dropna().unique().tolist())

        continente_escolhido = st.selectbox(
            "Filtrar por continente:",
            continentes
        )

    df_sel_filtrado = df_selecoes.copy()

    if continente_escolhido != "Todos":
        df_sel_filtrado = df_sel_filtrado[df_sel_filtrado["continente"] == continente_escolhido]

    if termo_selecao:
        termo = termo_selecao.lower()

        df_sel_filtrado = df_sel_filtrado[
            df_sel_filtrado.apply(
                lambda linha: termo in " ".join(
                    linha.astype(str).str.lower().tolist()
                ),
                axis=1
            )
        ]

    st.markdown("### Resultado da busca")

    if df_sel_filtrado.empty:
        st.warning(
            "Não encontrei nenhuma seleção com esse termo. Tente pesquisar por país ou continente."
        )

    else:
        st.success(f"{len(df_sel_filtrado)} seleção(ões) encontrada(s).")

        selecao_escolhida = st.selectbox(
            "Escolha uma seleção:",
            df_sel_filtrado["selecao"].tolist()
        )

        item = df_sel_filtrado[df_sel_filtrado["selecao"] == selecao_escolhida].iloc[0]

        selecao = item["selecao"]
        continente = item["continente"]
        titulos = item["titulos"]
        anos_titulos = item["anos_titulos"]
        participacoes = item["participacoes"]
        curiosidade = item["curiosidade"]
        resumo = item["resumo"]

        st.markdown("---")

        with st.container(border=True):
            st.markdown(f"## {selecao}")

            col1, col2, col3 = st.columns(3)

            with col1:
                st.metric("🏆 Títulos", titulos)

            with col2:
                st.metric("🌎 Continente", continente)

            with col3:
                st.metric("📌 Participações", participacoes)

            st.markdown("### 📅 Anos dos títulos")
            st.info(anos_titulos)

            st.markdown("### 💡 Curiosidade")
            st.warning(curiosidade)

            st.markdown("### 📖 Resumo simples")
            st.write(resumo)

    st.markdown("---")

    with st.container(border=True):
        st.markdown("### Ranking de seleções por número de títulos")

        ranking = df_selecoes.sort_values(
            by=["titulos", "selecao"],
            ascending=[False, True]
        )[["selecao", "continente", "titulos", "anos_titulos"]]

        ranking = ranking.rename(
            columns={
                "selecao": "Seleção",
                "continente": "Continente",
                "titulos": "Títulos",
                "anos_titulos": "Anos dos títulos"
            }
        )

        ranking = ranking.reset_index(drop=True)

        st.table(
            ranking.style.hide(axis="index")
        )

# ==============================
# PÁGINA COMPARAR SELEÇÕES
# ==============================

elif pagina == "⚖️ Comparar seleções":

    st.markdown(
        """
<div class="hero-card">
    <div class="hero-title">
        <span class="hero-white">⚖️ Comparar </span><span class="hero-highlight">seleções</span>
    </div>
    <div class="hero-subtitle">
        Escolha duas seleções para comparar títulos, participações, continente e resumo histórico
        de forma lado a lado.
    </div>
</div>
""",
        unsafe_allow_html=True
    )

    selecoes_lista = sorted(df_selecoes["selecao"].dropna().unique().tolist())

    col_select1, col_select2 = st.columns(2)

    with col_select1:
        selecao_1 = st.selectbox(
            "Escolha a primeira seleção:",
            selecoes_lista,
            index=0
        )

    with col_select2:
        indice_padrao = 1 if len(selecoes_lista) > 1 else 0

        selecao_2 = st.selectbox(
            "Escolha a segunda seleção:",
            selecoes_lista,
            index=indice_padrao
        )

    dados_1 = df_selecoes[df_selecoes["selecao"] == selecao_1].iloc[0]
    dados_2 = df_selecoes[df_selecoes["selecao"] == selecao_2].iloc[0]

    st.markdown("---")

    col_a, col_b = st.columns(2)

    with col_a:
        with st.container(border=True):
            st.markdown(f"## {dados_1['selecao']}")

            st.metric("🏆 Títulos", dados_1["titulos"])
            st.metric("📌 Participações", dados_1["participacoes"])

            st.markdown(f"**🌎 Continente:** `{dados_1['continente']}`")

            st.markdown("### 📅 Anos dos títulos")
            st.info(dados_1["anos_titulos"])

            st.markdown("### 💡 Curiosidade")
            st.warning(dados_1["curiosidade"])

            st.markdown("### 📖 Resumo")
            st.write(dados_1["resumo"])

    with col_b:
        with st.container(border=True):
            st.markdown(f"## {dados_2['selecao']}")

            st.metric("🏆 Títulos", dados_2["titulos"])
            st.metric("📌 Participações", dados_2["participacoes"])

            st.markdown(f"**🌎 Continente:** `{dados_2['continente']}`")

            st.markdown("### 📅 Anos dos títulos")
            st.info(dados_2["anos_titulos"])

            st.markdown("### 💡 Curiosidade")
            st.warning(dados_2["curiosidade"])

            st.markdown("### 📖 Resumo")
            st.write(dados_2["resumo"])

    st.markdown("---")

    with st.container(border=True):
        st.markdown("### Resumo da comparação")

        diferenca_titulos = int(dados_1["titulos"]) - int(dados_2["titulos"])
        diferenca_participacoes = int(dados_1["participacoes"]) - int(dados_2["participacoes"])

        if diferenca_titulos > 0:
            st.write(f"🏆 **{dados_1['selecao']}** tem {abs(diferenca_titulos)} título(s) a mais que **{dados_2['selecao']}**.")
        elif diferenca_titulos < 0:
            st.write(f"🏆 **{dados_2['selecao']}** tem {abs(diferenca_titulos)} título(s) a mais que **{dados_1['selecao']}**.")
        else:
            st.write("🏆 As duas seleções têm a mesma quantidade de títulos cadastrados.")

        if diferenca_participacoes > 0:
            st.write(f"📌 **{dados_1['selecao']}** tem {abs(diferenca_participacoes)} participação(ões) a mais em Copas.")
        elif diferenca_participacoes < 0:
            st.write(f"📌 **{dados_2['selecao']}** tem {abs(diferenca_participacoes)} participação(ões) a mais em Copas.")
        else:
            st.write("📌 As duas seleções têm a mesma quantidade de participações cadastradas.")

# ==============================
# PÁGINA SOBRE O PROJETO
# ==============================

elif pagina == "📌 Sobre o projeto":

    st.markdown(
        """
<div class="hero-card">
    <div class="hero-title">
        <span class="hero-white">📌 Sobre o </span><span class="hero-highlight">projeto</span>
    </div>
    <div class="hero-subtitle">
        Entenda o problema, a solução, a base de conhecimento, as tecnologias usadas
        e as competências demonstradas no Copa sem Complicação.
    </div>
</div>
""",
        unsafe_allow_html=True
    )

    col1, col2 = st.columns(2)

    with col1:
        with st.container(border=True):
            st.markdown("### Problema")
            st.write(
                """
                Durante a Copa do Mundo, muitas pessoas querem acompanhar os jogos,
                participar das conversas e entender o que está acontecendo, mas se perdem
                em regras, termos técnicos, formatos de classificação e contexto histórico.
                """
            )

    with col2:
        with st.container(border=True):
            st.markdown("### Solução")
            st.write(
                """
                O projeto cria uma experiência simples e acessível para consultar dúvidas,
                conhecer seleções e comparar informações históricas de forma organizada.
                """
            )

    st.markdown("---")

    col3, col4 = st.columns(2)

    with col3:
        with st.container(border=True):
            st.markdown("### Base de conhecimento")
            st.write(
                """
                Estruturei uma base em CSV para organizar perguntas, respostas,
                exemplos práticos, dados históricos das seleções, títulos, participações
                e curiosidades.
                """
            )

    with col4:
        with st.container(border=True):
            st.markdown("### Tecnologias usadas")
            st.write(
                """
                - Python  
                - Streamlit  
                - Pandas  
                - CSV como base de conhecimento  
                - HTML/CSS simples para personalização visual
                """
            )

    st.markdown("---")

    col5, col6 = st.columns(2)

    with col5:
        with st.container(border=True):
            st.markdown("### Competências demonstradas")
            st.write(
                """
                - Estruturação de dados  
                - Criação de interface interativa  
                - Busca e filtros  
                - Experiência do usuário  
                - Comunicação simples  
                - Organização de informação para leigos  
                - Transformação de conteúdo em produto digital
                """
            )

    with col6:
        with st.container(border=True):
            st.markdown("### Aprendizados")
            st.write(
                """
                Esse projeto mostra como dados e tecnologia podem simplificar
                experiências populares. A proposta não é apenas falar sobre futebol,
                mas transformar informação em uma experiência mais clara, acessível
                e humana.
                """
            )

    st.markdown("---")

    with st.container(border=True):
        st.markdown("### Próximos passos possíveis")
        st.write(
            """
            - Adicionar uma aba com história dos jogadores;  
            - Criar um quiz interativo sobre a Copa;  
            - Publicar o app online no Streamlit Community Cloud;  
            - Transformar o projeto em um post ou carrossel para LinkedIn;  
            - Evoluir a base de dados para uma planilha online ou banco de dados.
            """
        )

    st.info("Projeto desenvolvido por Jade Gama como estudo prático de dados, tecnologia e experiência do usuário.")
        