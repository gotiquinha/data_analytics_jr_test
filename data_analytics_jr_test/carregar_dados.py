import pandas as pd
import sqlite3
from pathlib import Path

def criar_conexao():
    """Cria uma conexão com o banco de dados SQLite."""
    db_path = Path(__file__).parent / "test_analytics.db"
    return sqlite3.connect(db_path)

def carregar_dados_escolas():
    """Carrega os dados das escolas do banco de dados."""
    try:
        conn = criar_conexao()
        query = """
        SELECT 
            e.cod_escola,
            e.nome_escola,
            e.dre,
            e.latitude,
            e.longitude,
            COUNT(DISTINCT p.cd_aluno) as total_alunos
        FROM escolas e
        LEFT JOIN perfil_alunos p ON e.cod_escola = p.cod_escola
        GROUP BY e.cod_escola
        """
        df = pd.read_sql_query(query, conn)
        conn.close()
        return df
    except Exception as e:
        print(f"Erro ao carregar dados: {e}")
        return None

def carregar_dados_series():
    """Carrega os dados de distribuição por série do banco de dados."""
    try:
        conn = criar_conexao()
        query = """
        SELECT 
            serie_ensino,
            COUNT(DISTINCT cd_aluno) as total_alunos
        FROM perfil_alunos
        GROUP BY serie_ensino
        ORDER BY total_alunos DESC
        LIMIT 10
        """
        df = pd.read_sql_query(query, conn)
        conn.close()
        return df
    except Exception as e:
        print(f"Erro ao carregar dados das séries: {e}")
        return None

if __name__ == "__main__":
    # Teste das funções
    df_escolas = carregar_dados_escolas()
    if df_escolas is not None:
        print("\nDados das escolas:")
        print(df_escolas.head())
    
    df_series = carregar_dados_series()
    if df_series is not None:
        print("\nDados das séries:")
        print(df_series.head()) 