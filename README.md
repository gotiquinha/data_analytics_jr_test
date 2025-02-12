# 📚 Dashboard - Escolas Municipais de São Paulo

Dashboard interativo para análise das escolas municipais de São Paulo, desenvolvido com Streamlit e Plotly.

## 🎯 Funcionalidades

- Visualização de métricas gerais
- Gráficos de distribuição de alunos
- Mapa de densidade de alunos por região
- Análise temporal dos dados

## 🚀 Como executar localmente

1. Clone o repositório:
```bash
git clone https://github.com/gotiquinha/use.uniformes.git
cd use-uniformes
```

2. Crie um ambiente virtual e ative-o:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate  # Windows
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

4. Execute a aplicação:
```bash
streamlit run data_analytics_jr_test/app.py
```

## 📊 Fonte dos dados

Os dados utilizados neste projeto são provenientes da Secretaria Municipal de Educação de São Paulo.

## 📁 Estrutura do projeto

```
.
├── data_analytics_jr_test/
│   ├── app.py              # Aplicativo Streamlit
│   ├── criar_relacoes.py   # Script para criar relações no banco
│   └── carregar_dados.py   # Script para carregar dados iniciais
├── requirements.txt        # Dependências do projeto
└── README.md              # Este arquivo
```

## 📝 Licença

Este projeto está sob a licença MIT.

## 🤝 Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir uma issue ou enviar um pull request. 