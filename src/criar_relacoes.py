import pandas as pd
import sqlite3

def criar_relacoes():
    # Conexão com o banco de dados
    conn = sqlite3.connect('test_analytics.db')
    
    # Criando view para relacionar escolas e alunos
    query_view = """
    CREATE VIEW IF NOT EXISTS escolas_alunos AS
    SELECT 
        e.*,
        COUNT(DISTINCT a.cd_aluno) as total_alunos
    FROM escolas e
    LEFT JOIN alunos a ON e.cd_escola = a.cd_escola
    GROUP BY e.cd_escola;
    """
    
    try:
        conn.execute(query_view)
        conn.commit()
        print("View escolas_alunos criada com sucesso!")
        
        # Verificando os dados
        query_check = """
        SELECT 
            dre,
            COUNT(DISTINCT cd_escola) as total_escolas,
            SUM(total_alunos) as total_alunos
        FROM escolas_alunos
        GROUP BY dre
        ORDER BY total_alunos DESC;
        """
        
        result = pd.read_sql(query_check, conn)
        print("\nResumo por DRE:")
        print(result.to_string(index=False))
        
    except Exception as e:
        print(f"Erro ao criar view: {e}")
    
    finally:
        conn.close()

if __name__ == "__main__":
    criar_relacoes() 