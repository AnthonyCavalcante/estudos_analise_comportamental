import pandas as pd
from data_processing import load_data_csv
def main():
    """Função principal que orquestra a análise."""
    LOCAL_PATH = '/workspaces/Data/processed/desafio_semanal_4_dados_processados.csv'
    LOCAL_SAVE = '/workspaces/outputs/reports/report_question02.txt'

    
    df = load_data_csv(LOCAL_PATH)
    df_churn = df[df['ChurnedLoyaltyProgram'] == True].groupby('Tier').agg({'CustomerID':'count',
                                                                            'TotalPointsEarned': 'sum',
                                                                             'PointsRedeemed': 'sum' })\
                                                                        .rename(columns={'CustomerID':'QtdUsers'})\
                                                                        .reset_index()
    with open(LOCAL_SAVE, 'w',encoding='utf-8') as f: 
        print(df_churn.to_markdown(index=False, numalign='left',stralign='left'), file=f)
        print(f'\n\nTotal de usuários por TIer:', file=f)
        print(df_churn[['Tier', 'QtdUsers']].to_markdown(index=False, stralign='left',numalign='left'), file=f)
        print('\n', file=f)
        
        for col in df_churn[['TotalPointsEarned','PointsRedeemed']].columns:
            print(f'Média de {col} é {df_churn[col].mean().round(2)}', file=f)
            print('\n', file=f)
        print('-----------------------------------------', file=f)
    
    print('arquivo txt criado')

if __name__ == '__main__':
    main()