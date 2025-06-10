from src.etl.extract import extract_data
from src.etl.load import load_data
from src.etl.transform import transform_data
from src.db.db_loader import DBLoader
from src.utils.logger import get_logger
from src.db.db_connection import get_connection



def main():
    print("Iniciando aplicação BigDataTst...")

    df_raw = extract_data()
    df_clean = transform_data(df_raw)
    load_data(df_clean)


    print("Pipeline finalizado com sucesso.")

if __name__ == "__main__":
    main()

