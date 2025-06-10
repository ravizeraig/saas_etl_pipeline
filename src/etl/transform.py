from src.utils.cleaning import convert_money, convert_employees

def transform_data(df):
    print("Transformando dados...")

    # Aplicando as funções de limpeza
    df['Total Funding'] = df['Total Funding'].apply(convert_money)
    df['ARR'] = df['ARR'].apply(convert_money)
    df['Valuation'] = df['Valuation'].apply(convert_money)
    df['Employees'] = df['Employees'].apply(convert_employees)

    print("Transformação concluída.")
    return df
