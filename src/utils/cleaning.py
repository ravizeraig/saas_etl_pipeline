import pandas as pd
import numpy as np


def convert_money(value):
    """
    Converte string de dinheiro como '$1.5B', '$200M', '$3T' para número em dólares.
    """
    if pd.isnull(value):
        return np.nan

    multipliers = {'K': 1e3, 'M': 1e6, 'B': 1e9, 'T': 1e12}

    try:
        value = value.replace('$', '').replace(',', '').strip()
        if value[-1] in multipliers:
            multiplier = multipliers[value[-1]]
            return float(value[:-1]) * multiplier
        else:
            return float(value)
    except:
        return np.nan


def convert_employees(value):
    """
    Converte string de número de funcionários como '221,000' para inteiro.
    """
    if pd.isnull(value):
        return np.nan

    try:
        return int(value.replace(',', '').strip())
    except:
        return np.nan
