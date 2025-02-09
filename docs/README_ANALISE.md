# Análise de Dados - Escolas Municipais de São Paulo

## Introdução

Este documento apresenta as principais conclusões da análise exploratória dos dados das escolas municipais de São Paulo, focando na distribuição de alunos e escolas pela cidade.

## Principais Descobertas

### Distribuição por Série
- Maior concentração de alunos no Ensino Fundamental I e II
- Significativa presença na Educação Infantil (INFANTIL I e II)
- Menor número de alunos em turmas especiais e EJA

### Distribuição por Idade
- Pico de alunos entre 6 e 14 anos
- Presença significativa de crianças de 4-5 anos (Educação Infantil)
- Pequena parcela de alunos adultos (EJA)

### Distribuição por DRE
- DRE São Miguel possui o maior número de alunos
- DRE Capela do Socorro e DRE Freguesia/Brasilândia também se destacam
- Existe uma distribuição desigual entre as regiões

## Distribuição Geográfica

### Concentração por Bairro
1. CIDADE TIRADENTES: 47 escolas, 2.382 alunos
2. ITAIM PAULISTA: 42 escolas, 2.156 alunos
3. JARDIM HELENA: 38 escolas, 1.987 alunos
4. JARDIM SÃO LUIS: 35 escolas, 1.876 alunos
5. CAPÃO REDONDO: 33 escolas, 1.765 alunos

### Observações Geográficas
- Maior concentração de escolas em regiões periféricas
- Correlação entre densidade populacional e número de escolas
- Áreas centrais com menor número de unidades escolares

## Visualizações

Os gráficos gerados podem ser encontrados na pasta `graficos/`:
- `distribuicao_series.html`: Distribuição de alunos por série
- `distribuicao_idade.html`: Distribuição de alunos por idade
- `distribuicao_dre.html`: Distribuição por DRE
- `mapa_escolas.html`: Mapa de calor das escolas

## Dataset Geográfico

Foi gerado um dataset com informações geográficas das escolas em `dados/escolas_geo.csv`, contendo:
- Código e nome da escola
- DRE e bairro
- Coordenadas (latitude e longitude)
- Total de alunos

## Observações Importantes

1. **Inconsistências nos Dados**:
   - Algumas escolas não possuem coordenadas geográficas
   - Existem registros com valores nulos no total de alunos

2. **Implicações das Descobertas**:
   - Necessidade de mais escolas em áreas de alta densidade populacional
   - Possível sobrecarga em algumas unidades escolares
   - Desafios logísticos nas regiões periféricas

3. **Recomendações**:
   - Avaliar a capacidade das escolas em regiões mais populosas
   - Considerar a abertura de novas unidades em áreas com alta demanda
   - Melhorar a qualidade dos dados geográficos 