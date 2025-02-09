# Análise de Dados - Escolas Municipais de São Paulo

Este projeto contém a análise dos dados das escolas municipais de São Paulo, desenvolvida como parte do teste para a posição de Analista de Dados Jr.

## Estrutura do Projeto

```
.
├── data/               # Dados brutos e processados
│   ├── Data/          # Dados originais em CSV
│   ├── graficos/      # Gráficos gerados
│   └── dados/         # Datasets processados
├── docs/              # Documentação
│   └── README_ANALISE.md  # Análise detalhada
├── src/               # Códigos fonte
│   ├── carregar_dados.py    # ETL dos dados
│   ├── criar_relacoes.py    # Criação de relações
│   ├── analise_exploratoria.py  # Análises básicas
│   ├── analise_geografica.py    # Análises geográficas
│   └── app.py        # Aplicativo Streamlit
└── requirements.txt   # Dependências do projeto
```

## Instalação

1. Clone este repositório
2. Instale as dependências:
```bash
pip install -r requirements.txt
```

## Executando o Projeto

1. Carregue os dados para o SQLite:
```bash
python src/carregar_dados.py
```

2. Crie as relações entre as tabelas:
```bash
python src/criar_relacoes.py
```

3. Execute as análises:
```bash
python src/analise_exploratoria.py
python src/analise_geografica.py
```

4. Visualize os resultados no Streamlit:
```bash
streamlit run src/app.py
```

## Análises Realizadas

1. Carregamento e organização dos dados em SQLite
2. Criação de relações entre escolas e alunos
3. Análise exploratória dos dados
4. Análise geográfica das escolas
5. Visualização interativa com Streamlit

Para mais detalhes sobre as análises e conclusões, consulte [docs/README_ANALISE.md](docs/README_ANALISE.md).

## Tecnologias Utilizadas

- Python 3.12
- SQLite
- Pandas
- Plotly
- Streamlit

