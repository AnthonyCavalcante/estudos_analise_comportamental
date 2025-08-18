# Em: src/data_processing.py
import pandas as pd
import dataframe_image as dfi
from typing import List, Any, Tuple  # Importa tipos para type hinting


def load_data_csv(local_path: str) -> pd.DataFrame:
    """Carrega dados de um arquivo CSV para um DataFrame.

    Args:
        local_path (str): Caminho onde o arquivo CSV está armazenado.

    Returns:
        pd.DataFrame: DataFrame pandas com os dados carregados.
    """
    print(f'Dados carregados de: {local_path}')
    return pd.read_csv(local_path)


def save_data_csv(df: pd.DataFrame, local_path: str):
    """Salva um DataFrame em um arquivo CSV, sem o índice.

    Args:
        df (pd.DataFrame): DataFrame a ser salvo.
        local_path (str): Caminho completo onde o arquivo será salvo.
    """
    df.to_csv(local_path, index=False)
    print(f'Arquivo salvo com sucesso em: {local_path}!')


def trate_nan(df: pd.DataFrame, fill_value: Any = 0) -> pd.DataFrame:
    """Substitui valores NaN em todas as colunas aplicáveis por um valor padrão.

    Args:
        df (pd.DataFrame): DataFrame a ser tratado.
        fill_value (Any, optional): Valor para substituir os NaNs. Default é 0.

    Returns:
        pd.DataFrame: DataFrame com os valores nulos tratados.
    """
    df_copy = df.copy()
    columns_nan = df_copy.columns[df_copy.isna().any()].to_list()

    for col in columns_nan:
        df_copy[col] = df_copy[col].fillna(fill_value)

    return df_copy


def create_date_cols(df: pd.DataFrame, cols: List[str]) -> pd.DataFrame:
    """Converte colunas para datetime e extrai a data e o dia da semana.

    Args:
        df (pd.DataFrame): DataFrame que receberá as novas colunas.
        cols (List[str]): Lista de nomes das colunas a serem transformadas.

    Returns:
        pd.DataFrame: DataFrame com as novas colunas de data.
    """
    df_copy = df.copy()
    for col in cols:
        df_copy[col] = pd.to_datetime(df_copy[col])
        df_copy[col + '_date'] = df_copy[col].dt.date
        df_copy[col + '_weekday'] = df_copy[col].dt.day_name()
    return df_copy

def group_transform(df: pd.DataFrame,new_column: str , col_group: str, 
                    column_transform: str, tuple: tuple) -> pd.DataFrame:

    df_trate = df.copy()
    df_trate[new_column] = df_trate.groupby(col_group)[column_transform].transform(tuple[0],tuple[1])
    return df_trate

