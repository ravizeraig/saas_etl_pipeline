import os
import logging
import psycopg2
from psycopg2 import OperationalError
from dotenv import load_dotenv
import sqlite3 # Importar o módulo sqlite3

load_dotenv()

logger = logging.getLogger(__name__)
if not logger.handlers:
    # Configuração básica de logging se ainda não houver handlers
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
            logger.error(f"Detalhes da conexão tentada: "
                         f"DB_NAME={os.getenv('DB_NAME')}, "
                         f"DB_USER={os.getenv('DB_USER')}, "
                         f"DB_HOST={os.getenv('DB_HOST')}, "
                         f"DB_PORT={os.getenv('DB_PORT')}")
            raise
        except Exception as e:
            logger.error(f"Ocorreu um erro inesperado ao conectar com PostgreSQL: {e}")
            raise
    elif db_type == "sqlite":
        try:
            sqlite_db_path = os.getenv("SQLITE_DB_PATH")
            # Crie o diretório 'data' se ele não existir
            os.makedirs(os.path.dirname(sqlite_db_path), exist_ok=True)
            logger.info(f"Tentando conectar ao banco SQLite em: {sqlite_db_path}")
            conn = sqlite3.connect(sqlite_db_path)
            logger.info("Conexão com SQLite estabelecida com sucesso.")
            return conn
        except Exception as e:
            logger.error(f"Erro ao conectar com SQLite: {e}")
            logger.error(f"Caminho do DB SQLite tentado: {os.getenv('SQLITE_DB_PATH')}")
            raise
    else:
        logger.error(f"Tipo de banco de dados não suportado: {db_type}")
        raise ValueError(f"Tipo de banco de dados não suportado: {db_type}")