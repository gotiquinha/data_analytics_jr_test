import streamlit as st
import pandas as pd
import plotly.express as px
import sqlite3

# Configuração da página
st.set_page_config(
    page_title="Análise de Escolas Municipais SP",
    page_icon="📚",
    layout="wide"
)

# Título
st.title("📚 Análise das Escolas Municipais de São Paulo")

# Conexão com o banco de dados
@st.cache_data
def carregar_dados():
    conn = sqlite3.connect('test_analytics.db')
    escolas = pd.read_sql("""
        SELECT e.*, COUNT(a.cd_aluno) as total_alunos
        FROM escolas_alunos e
        LEFT JOIN alunos a ON e.cd_escola = a.cd_escola
        GROUP BY e.cd_escola
    """, conn)
    alunos_serie = pd.read_sql("""
        SELECT serie_ensino, COUNT(*) as total
        FROM alunos
        GROUP BY serie_ensino
        ORDER BY total DESC
    """, conn)
    alunos_dre = pd.read_sql("""
        SELECT e.dre, COUNT(DISTINCT a.cd_aluno) as total_alunos
        FROM escolas_alunos e
        LEFT JOIN alunos a ON e.cd_escola = a.cd_escola
        GROUP BY e.dre
        ORDER BY total_alunos DESC
    """, conn)
    conn.close()
    return escolas, alunos_serie, alunos_dre

# Carregando dados
escolas, alunos_serie, alunos_dre = carregar_dados()

# Métricas principais
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Total de Escolas", f"{len(escolas):,}")
with col2:
    st.metric("Total de Alunos", f"{escolas['total_alunos'].sum():,}")
with col3:
    media_alunos = escolas['total_alunos'].mean()
    st.metric("Média de Alunos por Escola", f"{media_alunos:.0f}")

# Distribuição de alunos por série
st.subheader("Distribuição de Alunos por Série")
fig_series = px.bar(
    alunos_serie.head(10),
    x='serie_ensino',
    y='total',
    title="Top 10 Séries com Mais Alunos"
)
st.plotly_chart(fig_series)

# Distribuição por DRE
st.subheader("Distribuição de Alunos por DRE")
fig_dre = px.bar(
    alunos_dre,
    x='dre',
    y='total_alunos',
    title="Alunos por Diretoria Regional de Educação"
)
st.plotly_chart(fig_dre)

# Mapa das escolas
st.subheader("Distribuição Geográfica das Escolas")
escolas_map = escolas.dropna(subset=['latitude', 'longitude', 'total_alunos'])
fig_map = px.scatter_mapbox(
    escolas_map,
    lat='latitude',
    lon='longitude',
    size='total_alunos',
    hover_name='nome',
    hover_data=['dre', 'total_alunos'],
    title="Localização das Escolas",
    mapbox_style="carto-positron"
)
st.plotly_chart(fig_map)

# Conclusões
st.subheader("Principais Conclusões")
st.write("""
- A rede municipal de São Paulo possui uma grande concentração de alunos no ensino fundamental
- Existe uma distribuição desigual de alunos entre as DREs
- As escolas estão bem distribuídas geograficamente, mas com maior concentração em áreas periféricas
- A média de alunos por escola varia significativamente entre as regiões
""") 