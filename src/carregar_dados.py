import pandas as pd
import sqlite3
from sqlalchemy import create_engine
import os

# Criando conexão com o banco SQLite
# O banco será criado no arquivo 'test_analytics.db'
engine = create_engine('sqlite:///test_analytics.db')

def carregar_dados():
    """
    Função para carregar os dados dos arquivos CSV para o SQLite.
    Esta é uma função simples que:
    1. Lê os arquivos CSV da pasta Data
    2. Carrega eles para um banco SQLite
    """
    
    # Pasta onde estão os arquivos CSV
    pasta_dados = 'Data'
    
    try:
        # Para cada arquivo CSV na pasta
        for arquivo in os.listdir(pasta_dados):
            if arquivo.endswith('.csv'):
                # Nome da tabela será o nome do arquivo sem a extensão
                nome_tabela = arquivo.replace('.csv', '')
                
                print(f'Carregando {arquivo}...')
                
                # Lê o arquivo CSV
                df = pd.read_csv(f'{pasta_dados}/{arquivo}')
                
                # Carrega para o SQLite
                df.to_sql(nome_tabela, engine, if_exists='replace', index=False)
                
                print(f'Tabela {nome_tabela} criada com sucesso!')
                
    except Exception as e:
        print(f'Erro ao carregar os dados: {str(e)}')

if __name__ == '__main__':
    print('Iniciando carregamento dos dados...')
    carregar_dados()
    print('Processo finalizado!') 