from src.db.db_loader import DBLoader
from src.utils.logger import get_logger

def load_data(df):
    logger = get_logger(__name__)
    logger.info("Iniciando carga de dados via ETL...")

    db_loader = DBLoader()
    db_loader.load_dataframe(df, table_name='saas_companies_clean')

    logger.info("Carga de dados via ETL concluída.")
