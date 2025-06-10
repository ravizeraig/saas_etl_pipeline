# SaaS Data Pipeline

Este projeto é um pipeline de ETL (Extract, Transform, Load) para ingestão e análise de dados de empresas SaaS.

## 📌 Objetivo

Construir um pipeline de dados completo com:

- Extração de dados de um dataset de empresas SaaS
- Transformação e limpeza dos dados
- Carga dos dados em um banco de dados PostgreSQL
- Preparação para análises futuras

## 🛠️ Tecnologias utilizadas

- **Python 3.10**
- **Pandas**
- **SQLAlchemy**
- **PostgreSQL**
- **psycopg2**
- **python-dotenv**
- **Logging customizado**

## 🗂️ Estrutura do projeto
Claro, Mi! Agora com o .env.example incluído na estrutura, vou te gerar a versão final para o seu README.md.

Aqui está a estrutura de diretórios e arquivos atualizada, pronta para ser copiada:

Markdown

## 🗂️ Estrutura do Projeto

saas_etl_pipeline/  

├── src/
│   ├── etl/
│   │   ├── init.py      # Sinaliza que 'etl' é um pacote Python
│   │   ├── extract.py       # Lógica para extração de dados
│   │   ├── transform.py     # Lógica para transformação de dados
│   │   └── load.py          # Lógica para carga de dados
│   ├── db/
│   │   ├── init.py      # Sinaliza que 'db' é um pacote Python
│   │   ├── db_connection.py # Funções para conexão ao banco de dados
│   │   └── db_loader.py     # Lógica para carregar DataFrames no banco
│   ├── utils/
│   │   ├── init.py      # Sinaliza que 'utils' é um pacote Python
│   │   ├── logger.py        # Configuração e obtenção de loggers
│   │   └── cleaning.py      # Funções utilitárias de limpeza de dados
│   └── main.py              # Ponto de entrada principal do pipeline

├── data/
│   ├── raw/                 # Dados brutos de origem (ex: top_100_saas_companies_2025.csv)
│   └── processed/           # Dados limpos e transformados (ex: saas_companies_clean.csv)

├── notebooks/               # Notebooks Jupyter para exploração e análise
│   └── analise.ipynb

├── .env                     # Variáveis de ambiente (ex: credenciais de DB, NÃO versionado no Git)
├── .env.example             # Exemplo das variáveis de ambiente necessárias (versionado no Git)
├── .gitignore               # Arquivo para o Git ignorar arquivos e pastas específicos
├── requirements.txt         # Lista de dependências Python do projeto
└── README.md                # Documentação principal do projeto
