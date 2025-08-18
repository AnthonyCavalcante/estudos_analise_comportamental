import pandas as pd
from data_processing import load_data_csv, group_transform
from data_transforming import export_table_img
def main():
    """Função principal que orquestra a análise."""
    LOAD_PATH = '/workspaces/Data/processed/dados_processados.csv'
    IMG_SAVE_PATH = '/workspaces/outputs/figures/table_question3.png'
    TXT_INSERT_PATH = 'outputs/reports/report_question02.txt'

    df = load_data_csv(LOAD_PATH)
    df_quartil = group_transform(df, 'PR_first_quartil', 'Tier', 'PointsRedeemed',('quantile',0.25))
    set_tier = ['Silver', 'Gold']
    df_low_tier = df_quartil[(df_quartil['Tier'].isin(set_tier) & 
                              (df_quartil['PointsRedeemed'] < df_quartil['PR_first_quartil']))]

    with open(TXT_INSERT_PATH, 'a', encoding='utf-8') as f:
        print('\n\n Dados gerados para questão 03', file=f)
        print(f"\n Os Ids abaixo do 1º Quartil de seus Tier são:\n{df_low_tier['CustomerID'].unique()} ", file=f)
    
        for col in df_quartil[['AvgTransactionValue','NumTransactionsLast90Days']].columns:
            print(f"\nA média de {col} dos IDs encontrado é {df_low_tier[col].mean().round(2)}", file=f)
            print(f"A média geral de {col} do tier Silver é de {df_quartil[df_quartil['Tier'] =='Silver'][col].mean().round(2)}", file=f)
            print(f"A média geral de {col} do tier gold é de {df_quartil[df_quartil['Tier'] =='Gold'][col].mean().round(2)}", file=f)

    export_table_img(df_low_tier,IMG_SAVE_PATH, 'Tabela Questão 3: Usuários abaixo do 1º Quartil por Tier')
    print('dados registrados no txt')


if __name__ == '__main__':
    main()