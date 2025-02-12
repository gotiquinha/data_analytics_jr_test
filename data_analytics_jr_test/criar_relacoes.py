import sqlite3
import pandas as pd
from pathlib import Path
import csv

def detectar_delimitador(arquivo):
    """Detecta o delimitador usado no arquivo CSV."""
    with open(arquivo, 'r', encoding='latin1') as csvfile:
        # Lê as primeiras linhas do arquivo
        header = csvfile.readline()
        
        # Testa diferentes delimitadores comuns
        delimitadores = [',', ';', '\t', '|']
        for delimitador in delimitadores:
            if delimitador in header:
                return delimitador
    return ','  # delimitador padrão

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
        # Detectando o delimitador
        delimitador = detectar_delimitador(arquivo_csv)
        print(f"Delimitador detectado para escolas: '{delimitador}'")
        
        # Lendo o arquivo CSV com encoding latin1
        df = pd.read_csv(arquivo_csv, encoding='latin1', sep=delimitador)
        print("Colunas disponíveis:", df.columns.tolist())
        
        # Renomeando e selecionando as colunas necessárias
        df_escolas = df[[
            'CODESC',
            'NOMES',
            'DRE',
            'LATITUDE',
            'LONGITUDE'
        ]].copy()
        
        # Renomeando as colunas para o padrão do banco
        df_escolas.columns = [
            'cod_escola',
            'nome_escola',
            'dre',
            'latitude',
            'longitude'
        ]
        
        # Convertendo latitude e longitude para float
        df_escolas['latitude'] = pd.to_numeric(df_escolas['latitude'], errors='coerce')
        df_escolas['longitude'] = pd.to_numeric(df_escolas['longitude'], errors='coerce')
        
        # Conectando ao banco
        db_path = Path(__file__).parent / "test_analytics.db"
        conn = sqlite3.connect(db_path)
        
        # Importando dados
        df_escolas.to_sql("escolas", conn, if_exists="replace", index=False)
        
        conn.close()
        print("Dados das escolas importados com sucesso!")
        print(f"Total de escolas importadas: {len(df_escolas)}")
    except Exception as e:
        print(f"Erro ao importar dados das escolas: {e}")

def importar_dados_alunos(arquivo_csv):
    """Importa os dados dos alunos do arquivo CSV para o banco de dados."""
    try:
        # Detectando o delimitador
        delimitador = detectar_delimitador(arquivo_csv)
        print(f"Delimitador detectado para alunos: '{delimitador}'")
        
        # Lendo o arquivo CSV com encoding latin1
        df = pd.read_csv(arquivo_csv, encoding='latin1', sep=delimitador)
        print("Colunas disponíveis:", df.columns.tolist())
        
        # Criando um identificador único para aluno
        df['cd_aluno'] = df.groupby(['CODESC', 'DESCSERIE', 'IDADE', 'SEXO', 'NEE']).ngroup().astype(str)
        
        # Renomeando e selecionando as colunas necessárias
        df_alunos = df[[
            'cd_aluno',
            'CODESC',
            'DESCSERIE'
        ]].copy()
        
        # Renomeando as colunas para o padrão do banco
        df_alunos.columns = [
            'cd_aluno',
            'cod_escola',
            'serie_ensino'
        ]
        
        # Conectando ao banco
        db_path = Path(__file__).parent / "test_analytics.db"
        conn = sqlite3.connect(db_path)
        
        # Importando dados
        df_alunos.to_sql("perfil_alunos", conn, if_exists="replace", index=False)
        
        conn.close()
        print("Dados dos alunos importados com sucesso!")
        print(f"Total de alunos importados: {len(df_alunos)}")
    except Exception as e:
        print(f"Erro ao importar dados dos alunos: {e}")

if __name__ == "__main__":
    # Criando o banco e as tabelas
    criar_banco()
    
    # Caminhos para os arquivos CSV
    data_dir = Path(__file__).parent.parent / "data/Data/Data"
    arquivo_escolas = data_dir / "Escolas/escolas122023.csv"
    arquivo_alunos = data_dir / "Perfil dos educandos/idadeserieneeracadez23.csv"
    
    print(f"Importando dados de:")
    print(f"Escolas: {arquivo_escolas}")
    print(f"Alunos: {arquivo_alunos}")
    
    # Importando os dados
    importar_dados_escolas(arquivo_escolas)
    importar_dados_alunos(arquivo_alunos) 