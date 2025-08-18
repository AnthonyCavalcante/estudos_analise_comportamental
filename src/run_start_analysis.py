import pandas as pd
from data_processing import load_data_csv, save_data_csv, trate_nan, create_date_cols

DATA_PATH = '/workspaces/Data/raw/desafio_semana4.csv'
DATA_SAVE = '/workspaces/Data/processed/desafio_semanal_4_dados_processados.csv'
DATE_COLS = ['LastPurchaseDate']

def main():
    """Função principal que orquestra a análise."""
    df = load_data_csv(DATA_PATH)
    print('dados carregados!! ')

    df = trate_nan(df, 0)
    print('Valores nulos corrigidos!')

    df = create_date_cols(df, DATE_COLS )
    print('novas colunas de data criadas!!!')

    save_data_csv(
        df, DATA_SAVE )


if __name__ == '__main__':
    main()
