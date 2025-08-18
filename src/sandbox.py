import pandas as pd
from data_processing import load_data_csv, save_data_csv, trate_nan, create_date_cols 

pd.set_option('display.width', None)
DATA_PATH = '/workspaces/Data/raw/desafio_semana4.csv'
DATA_SAVE = '/workspaces/Data/processed/desafio_semanal_4_dados_processados.csv'
DATE_COLS = ['LastPurchaseDate']
LOCAL_PATH = '/workspaces/outputs/figures/final_question01.png'


def main():
    """Função principal que orquestra a análise."""

if __name__ == '__main__':
    main()
