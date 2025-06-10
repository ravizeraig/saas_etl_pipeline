import pandas as pd
from sqlalchemy import create_engine
from src.db.db_connection import get_connection
from src.utils.logger import get_logger

class DBLoader:
    def __init__(self):
        self.logger = get_logger(__name__)
        self.connection = get_connection()
        self.engine = self._create_engine()

    def _create_engine(self):
        """Cria engine SQLAlchemy para uso com pandas.to_sql"""
        try:
            db_url = self.connection.engine.url
            return create_engine(db_url)
        except AttributeError:
            # Se sua get_connection() retorna raw connection (psycopg2)
            import os
            db_name = os.getenv("DB_NAME")
            db_user = os.getenv("DB_USER")
            db_password = os.getenv("DB_PASSWORD")
            db_host = os.getenv("DB_HOST")
            db_port = os.getenv("DB_PORT")

            db_url = f'postgresql+psycopg2://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}'
            return create_engine(db_url)

    def load_dataframe(self, df: pd.DataFrame, table_name: str):
        """Carrega um DataFrame para a tabela no banco de dados"""
        try:
            self.logger.info(f"Iniciando inserção de {len(df)} registros na tabela '{table_name}'...")
            df.to_sql(table_name, self.engine, if_exists='replace', index=False)
            self.logger.info(f"Inserção na tabela '{table_name}' concluída com sucesso.")
        except Exception as e:
            self.logger.error(f"Erro ao inserir dados na tabela '{table_name}': {e}")
            raise
        finally:
            self.connection.close()
            self.logger.info("Conexão com o banco de dados fechada.")
