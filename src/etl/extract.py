import pandas as pd

def extract_data():
    print("Extraindo dados...")
    df = pd.read_csv('data/processed/saas_companies_clean.csv')
    print(f"Dados extraídos: {df.shape[0]} linhas.")
    return df
