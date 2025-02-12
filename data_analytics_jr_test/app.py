import streamlit as st
import pandas as pd
import plotly.express as px

# Configuração da página
st.set_page_config(
    page_title="Dashboard - Escolas Municipais de SP",
    page_icon="📚",
    layout="wide"
)

# Título
st.title("📚 Dashboard - Escolas Municipais de São Paulo")

# Carregando os dados
@st.cache_data
def carregar_dados():
    try:
        # Aqui você deve implementar a lógica para carregar seus dados
        # Por exemplo, do banco SQLite ou de arquivos CSV
        df = pd.DataFrame()  # Substitua isso pelos seus dados reais
        return df
    except Exception as e:
        st.error(f"Erro ao carregar os dados: {e}")
        return None

# Carregando os dados
df = carregar_dados()

if df is not None and not df.empty:
    # Métricas gerais
    col1, col2, col3 = st.columns(3)
    
    with col1:
        total_escolas = len(df)
        st.metric("Total de Escolas", f"{total_escolas:,}")
    
    with col2:
        total_alunos = df["total_alunos"].sum()
        st.metric("Total de Alunos", f"{total_alunos:,}")
    
    with col3:
        media_alunos = df["total_alunos"].mean()
        st.metric("Média de Alunos por Escola", f"{media_alunos:.0f}")

    # Mapa de densidade
    st.subheader("Densidade de Alunos por Região")
    
    fig = px.density_mapbox(
        df,
        lat="latitude",
        lon="longitude",
        z="total_alunos",
        radius=20,
        center={"lat": -23.5505, "lon": -46.6333},
        zoom=10,
        mapbox_style="carto-positron",
        title="Densidade de Alunos por Região"
    )
    
    st.plotly_chart(fig, use_container_width=True)

    # Distribuição por DRE
    st.subheader("Distribuição de Alunos por DRE")
    
    fig_dre = px.bar(
        df.groupby("dre")["total_alunos"].sum().reset_index(),
        x="dre",
        y="total_alunos",
        title="Total de Alunos por DRE"
    )
    
    st.plotly_chart(fig_dre, use_container_width=True)

else:
    st.warning("Não foi possível carregar os dados. Por favor, verifique a conexão com o banco de dados.") 