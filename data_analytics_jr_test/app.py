import streamlit as st
import pandas as pd
import plotly.express as px
from carregar_dados import carregar_dados_escolas, carregar_dados_series

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
        df_escolas = carregar_dados_escolas()
        df_series = carregar_dados_series()
        if df_escolas is None or df_series is None:
            raise Exception("Não foi possível carregar os dados do banco")
        return df_escolas, df_series
    except Exception as e:
        st.error(f"Erro ao carregar os dados: {e}")
        return None, None

# Carregando os dados
df, df_series = carregar_dados()

if df is not None and not df.empty:
    # Visão Geral
    st.header("👁️ Visão Geral")
    
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

    # Distribuição por Série
    st.header("📊 Distribuição por Série")
    st.caption("As 10 séries com mais alunos")
    
    if df_series is not None and not df_series.empty:
        fig_series = px.bar(
            df_series,
            x="serie_ensino",
            y="total_alunos",
            title="Top 10 Séries por Número de Alunos"
        )
        
        fig_series.update_layout(
            xaxis_title="Série",
            yaxis_title="Total de Alunos",
            showlegend=False
        )
        
        st.plotly_chart(fig_series, use_container_width=True)
    
    # Distribuição Geográfica
    st.header("🗺️ Distribuição Geográfica")
    st.caption("Localização das escolas no mapa de São Paulo")
    
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
    st.header("🏫 Distribuição por DRE")
    st.caption("Número de escolas e alunos por Diretoria Regional de Educação")
    
    fig_dre = px.bar(
        df.groupby("dre")["total_alunos"].sum().sort_values(ascending=False).reset_index(),
        x="dre",
        y="total_alunos",
        title="Escolas e Alunos por DRE"
    )
    
    fig_dre.update_layout(
        xaxis_title="DRE",
        yaxis_title="Quantidade",
        showlegend=True
    )
    
    st.plotly_chart(fig_dre, use_container_width=True)
    
    # Principais Conclusões
    st.header("📝 Principais Conclusões")
    
    st.markdown("""
    1. **Concentração em Educação Infantil**: A maior parte dos alunos está em séries iniciais, com destaque para Atividades Complementares e Educação Infantil.
    
    2. **Distribuição Regional**: Há uma concentração maior de escolas e alunos nas regiões periféricas da cidade, especialmente nas DREs Campo Limpo, Pirituba/Jaraguá e São Miguel.
    
    3. **Tamanho das Escolas**: Existe uma variação significativa no tamanho das escolas entre diferentes regiões, o que pode indicar diferentes necessidades de infraestrutura.
    
    4. **Distribuição Geográfica**: O mapa mostra uma distribuição ampla de escolas pela cidade, mas com clusters claros em certas regiões, especialmente nas periferias.
    """)

else:
    st.warning("Não foi possível carregar os dados. Por favor, verifique a conexão com o banco de dados.") 