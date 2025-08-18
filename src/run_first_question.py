import pandas as pd
from data_processing import load_data_csv
from data_transforming import export_table_img

LOCAL_PATH = '/workspaces/outputs/figures/question02_table.png'

def main():
    """Função principal que orquestra a análise."""
    df = load_data_csv('/workspaces/Data/processed/desafio_semanal_4_dados_processados.csv')
    
    df_tier_group = df.groupby('Tier').agg({'CustomerID':'count',
                                            'TotalPointsEarned':'mean',
                                            'PointsRedeemed':'mean',
                                            'NumTransactionsLast90Days':'mean'})
    export_table_img(df_tier_group, LOCAL_PATH, 'Relação Qtd. Usuários por Tier')

if __name__ == '__main__':
    main()