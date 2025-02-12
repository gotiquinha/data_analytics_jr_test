import sqlite3
import pandas as pd
from pathlib import Path

def criar_banco():
    """Cria o banco de dados e as tabelas necessárias."""
    db_path = Path(__file__).parent / "test_analytics.db"
    conn = sqlite3.connect(db_path)
    
    # Criando tabela de escolas
    conn.execute("""
    CREATE TABLE IF NOT EXISTS escolas (
        cod_escola TEXT PRIMARY KEY,
        nome_escola TEXT,
        dre TEXT,
        latitude REAL,
        longitude REAL
    )
    """)
    
    # Criando tabela de perfil dos alunos
    conn.execute("""
    CREATE TABLE IF NOT EXISTS perfil_alunos (
        cd_aluno TEXT,
        cod_escola TEXT,
        serie_ensino TEXT,
        FOREIGN KEY (cod_escola) REFERENCES escolas(cod_escola)
    )
    """)
    
    conn.commit()
    conn.close()

def importar_dados_escolas(arquivo_csv):
    """Importa os dados das escolas do arquivo CSV para o banco de dados."""
    try:
        # Lendo o arquivo CSV
        df = pd.read_csv(arquivo_csv)
        
        # Conectando ao banco
        db_path = Path(__file__).parent / "test_analytics.db"
        conn = sqlite3.connect(db_path)
        
        # Importando dados
        df.to_sql("escolas", conn, if_exists="replace", index=False)
        
        conn.close()
        print("Dados das escolas importados com sucesso!")
    except Exception as e:
        print(f"Erro ao importar dados das escolas: {e}")

def importar_dados_alunos(arquivo_csv):
    """Importa os dados dos alunos do arquivo CSV para o banco de dados."""
    try:
        # Lendo o arquivo CSV
        df = pd.read_csv(arquivo_csv)
        
        # Conectando ao banco
        db_path = Path(__file__).parent / "test_analytics.db"
        conn = sqlite3.connect(db_path)
        
        # Importando dados
        df.to_sql("perfil_alunos", conn, if_exists="replace", index=False)
        
        conn.close()
        print("Dados dos alunos importados com sucesso!")
    except Exception as e:
        print(f"Erro ao importar dados dos alunos: {e}")

if __name__ == "__main__":
    # Criando o banco e as tabelas
    criar_banco()
    
    # Aqui você deve especificar os caminhos dos seus arquivos CSV
    arquivo_escolas = "caminho/para/seu/arquivo/escolas.csv"
    arquivo_alunos = "caminho/para/seu/arquivo/alunos.csv"
    
    # Importando os dados
    importar_dados_escolas(arquivo_escolas)
    importar_dados_alunos(arquivo_alunos) 