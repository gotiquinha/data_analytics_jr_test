import pandas as pd
import plotly.express as px
import sqlite3

def analisar_distribuicao_geografica():
    # Conexão com o banco de dados
    conn = sqlite3.connect('test_analytics.db')
    
    # Query para buscar dados geográficos
    query = """
    SELECT 
        e.cd_escola,
        e.nome,
        e.dre,
        e.bairro,
        e.latitude,
        e.longitude,
        COUNT(DISTINCT a.cd_aluno) as total_alunos
    FROM escolas_alunos e
    LEFT JOIN alunos a ON e.cd_escola = a.cd_escola
    GROUP BY e.cd_escola
    """
    
    # Carregando dados
    escolas = pd.read_sql(query, conn)
    conn.close()
    
    # Limpando dados
    escolas = escolas.dropna(subset=['latitude', 'longitude', 'total_alunos'])
    escolas['total_alunos'] = escolas['total_alunos'].fillna(0)
    
    # Análise por bairro
    bairros = escolas.groupby('bairro').agg({
        'cd_escola': 'count',
        'total_alunos': 'sum'
    }).reset_index()
    
    bairros.columns = ['bairro', 'total_escolas', 'total_alunos']
    bairros = bairros.sort_values('total_alunos', ascending=False)
    
    print("\nEstatísticas por Bairro:")
    print(bairros.head(10).to_string(index=False))
    
    # Salvando dataset processado
    escolas.to_csv('data/dados/escolas_geo.csv', index=False)
    
    # Criando mapa de calor
    fig = px.scatter_mapbox(
        escolas,
        lat='latitude',
        lon='longitude',
        size='total_alunos',
        hover_name='nome',
        hover_data=['dre', 'total_alunos'],
        title="Distribuição Geográfica das Escolas",
        mapbox_style="carto-positron"
    )
    
    # Salvando visualização
    fig.write_html('data/graficos/mapa_escolas.html')

if __name__ == "__main__":
    analisar_distribuicao_geografica() 