# src/db_connection.py
import os
import logging
import psycopg2
from psycopg2 import OperationalError
from dotenv import load_dotenv
import sqlite3

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

# Configuração do logger (apenas para garantir que está funcionando aqui também)
logger = logging.getLogger(__name__)
if not logger.handlers:
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


def get_connection():
    db_type = os.getenv("DB_TYPE")

    if db_type == "postgresql":
        try:
            logger.info("Tentando conectar ao banco POSTGRESQL...")
            conn = psycopg2.connect(
                dbname=os.getenv("DB_NAME"),
                user=os.getenv("DB_USER"),
                password=os.getenv("DB_PASSWORD"),
                host=os.getenv("DB_HOST"),
                port=os.getenv("DB_PORT")
            )
            logger.info("Conexão com PostgreSQL estabelecida com sucesso.")
            return conn
        except OperationalError as e:
            logger.error(f"Erro de conexão com PostgreSQL: {e}")
            # Loga todos os detalhes da conexão que foram tentados (exceto a senha)
            logger.error(f"Detalhes da conexão tentada: "
                         f"DB_NAME={os.getenv('DB_NAME')}, "
                         f"DB_USER={os.getenv('DB_USER')}, "
                         f"DB_HOST={os.getenv('DB_HOST')}, "
                         f"DB_PORT={os.getenv('DB_PORT')}")
            # Re-lança a exceção para que o programa principal saiba que a conexão falhou
            raise
        except Exception as e:
            logger.error(f"Ocorreu um erro inesperado ao conectar com PostgreSQL: {e}")
            raise
    elif db_type == "sqlite":
        try:
            sqlite_db_path = os.getenv("SQLITE_DB_PATH")
            logger.info(f"Tentando conectar ao banco SQLite em: {sqlite_db_path}")
            conn = sqlite3.connect(sqlite_db_path) # Assumindo que sqlite3 está importado
            logger.info("Conexão com SQLite estabelecida com sucesso.")
            return conn
        except Exception as e:
            logger.error(f"Erro ao conectar com SQLite: {e}")
            logger.error(f"Caminho do DB SQLite tentado: {os.getenv('SQLITE_DB_PATH')}")
            raise
    else:
        logger.error(f"Tipo de banco de dados não suportado: {db_type}")
        raise ValueError(f"Tipo de banco de dados não suportado: {db_type}")
