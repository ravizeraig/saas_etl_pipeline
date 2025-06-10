# src/db_connection.py
import os
import psycopg2
import pymysql
import sqlite3
from dotenv import load_dotenv
import logging

load_dotenv()

# Setup do logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")


# src/db_connection.py (Trecho relevante)

def get_connection():  # db_type removido dos parametros
    db_type = os.getenv("DB_TYPE")  # <--- Lendo do .env

    if not db_type:
        logging.error("Variável de ambiente 'DB_TYPE' não definida. Por favor, defina no seu .env.")
        raise ValueError("DB_TYPE não configurado no .env")

    logging.info(f"Conectando ao banco {db_type.upper()}...")  # <--- Log dinâmico com f-string

    try:
        if db_type == 'postgresql':
            conn = psycopg2.connect(
                dbname=os.getenv("DB_NAME"),
                user=os.getenv("DB_USER"),
                password=os.getenv("DB_PASSWORD"),
                host=os.getenv("DB_HOST"),
                port=os.getenv("DB_PORT")
            )

        elif db_type == 'mysql':
            conn = pymysql.connect(
                host=os.getenv("DB_HOST"),
                user=os.getenv("DB_USER"),
                password=os.getenv("DB_PASSWORD"),
                database=os.getenv("DB_NAME"),
                port=int(os.getenv("DB_PORT"))
            )

        elif db_type == 'sqlite':
            sqlite_path = os.getenv("SQLITE_DB_PATH")
            if not sqlite_path:
                logging.error(f"Variável de ambiente 'SQLITE_DB_PATH' não definida para DB_TYPE={db_type}.")
                raise ValueError("SQLITE_DB_PATH não configurado no .env para DB_TYPE=sqlite")
            conn = sqlite3.connect(sqlite_path)

        else:
            raise ValueError(f"Tipo de banco não suportado no DB_TYPE do .env: {db_type}")

        logging.info("Conexão estabelecida com sucesso.")
        return conn

    except Exception as e:
        logging.error(f"Erro ao conectar com o banco de dados ({db_type}): {e}")  # Log de erro também mais dinâmico
        raise
