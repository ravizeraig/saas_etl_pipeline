import os
import logging
from sqlalchemy import create_engine
# from src.db.db_connection import get_connection # Provavelmente você já tem isso ou algo similar

logger = logging.getLogger(__name__)

class DBLoader:
    def __init__(self):
        # NÃO chame get_connection() aqui e tente acessar .engine
        # A conexão do SQLite é diferente e não precisa de um engine complexo assim
        # Vamos pegar as variáveis de ambiente diretamente para criar o engine SQLAlchemy
        self.db_type = os.getenv("DB_TYPE")
        self.engine = self._create_engine() # Chame _create_engine aqui

    def _create_engine(self):
        if self.db_type == "postgresql":
            # Lógica para PostgreSQL (se você precisar dela para outros ambientes)
            db_name = os.getenv("DB_NAME")
            db_user = os.getenv("DB_USER")
            db_password = os.getenv("DB_PASSWORD")
            db_host = os.getenv("DB_HOST")
            db_port = os.getenv("DB_PORT")
            db_url = f"postgresql+psycopg2://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"
            logger.info(f"Criando engine SQLAlchemy para PostgreSQL: {db_host}:{db_port}/{db_name}")
            return create_engine(db_url)
        elif self.db_type == "sqlite":
            sqlite_db_path = os.getenv("SQLITE_DB_PATH")
            # URL para SQLite: 'sqlite:///caminho/para/o/arquivo.db'
            db_url = f"sqlite:///{sqlite_db_path}"
            logger.info(f"Criando engine SQLAlchemy para SQLite: {sqlite_db_path}")
            return create_engine(db_url)
        else:
            logger.error(f"Tipo de banco de dados não suportado para SQLAlchemy Engine: {self.db_type}")
            raise ValueError(f"Tipo de banco de dados não suportado: {self.db_type}")

    def load_data(self, df, table_name="processed_data"):
        """
        Carrega um DataFrame pandas para o banco de dados.
        """
        try:
            # Use o engine que foi criado no __init__
            df.to_sql(table_name, self.engine, if_exists='replace', index=False)
            logger.info(f"Dados carregados com sucesso na tabela '{table_name}'.")
        except Exception as e:
            logger.error(f"Erro ao carregar dados para o banco de dados: {e}")
            raise

# Remover esta linha se ela estava fora da classe DBLoader
# db_loader = DBLoader()