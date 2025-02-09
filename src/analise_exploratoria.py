import pandas as pd
import plotly.express as px
import sqlite3

def analisar_dados():
    # Conexão com o banco de dados
    conn = sqlite3.connect('test_analytics.db')
    
    # Análise de alunos por série
    query_series = """
    SELECT serie_ensino, COUNT(*) as total
    FROM alunos
    GROUP BY serie_ensino
    ORDER BY total DESC
    """
    alunos_serie = pd.read_sql(query_series, conn)
    
    print("\nDistribuição de Alunos por Série:")
    print(alunos_serie.to_string(index=False))
    
    # Análise de alunos por idade
    query_idade = """
    SELECT idade, COUNT(*) as total
    FROM alunos
    GROUP BY idade
    ORDER BY idade
    """
    alunos_idade = pd.read_sql(query_idade, conn)
    
    print("\nDistribuição de Alunos por Idade:")
    print(alunos_idade.to_string(index=False))
    
    # Análise de escolas por DRE
    query_dre = """
    SELECT 
        e.dre,
        COUNT(DISTINCT e.cd_escola) as total_escolas,
        COUNT(DISTINCT a.cd_aluno) as total_alunos
    FROM escolas_alunos e
    LEFT JOIN alunos a ON e.cd_escola = a.cd_escola
    GROUP BY e.dre
    ORDER BY total_alunos DESC
    """
    escolas_dre = pd.read_sql(query_dre, conn)
    
    print("\nDistribuição de Escolas e Alunos por DRE:")
    print(escolas_dre.to_string(index=False))
    
    conn.close()
    
    # Gerando gráficos
    # 1. Distribuição por série
    fig_series = px.bar(
        alunos_serie.head(10),
        x='serie_ensino',
        y='total',
        title="Top 10 Séries com Mais Alunos"
    )
    fig_series.write_html('data/graficos/distribuicao_series.html')
    
    # 2. Distribuição por idade
    fig_idade = px.line(
        alunos_idade,
        x='idade',
        y='total',
        title="Distribuição de Alunos por Idade"
    )
    fig_idade.write_html('data/graficos/distribuicao_idade.html')
    
    # 3. Distribuição por DRE
    fig_dre = px.bar(
        escolas_dre,
        x='dre',
        y=['total_escolas', 'total_alunos'],
        title="Distribuição de Escolas e Alunos por DRE",
        barmode='group'
    )
    fig_dre.write_html('data/graficos/distribuicao_dre.html')

if __name__ == "__main__":
    analisar_dados() 