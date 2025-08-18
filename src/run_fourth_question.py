import pandas as pd
from data_processing import load_data_csv
def main():
    """Função principal que orquestra a análise."""
    LOCAL_PATH = '/workspaces/Data/processed/dados_processados.csv'
    SAVE_REPORT_PATH = '/workspaces/outputs/reports/report_question02.txt'
    df = load_data_csv(LOCAL_PATH)
    
    df['AvgRedeemed'] = df['PointsRedeemed'] / df['TotalPointsEarned']
    lower_avg_redeemed = df['AvgRedeemed'].quantile(0.10)
    df_lower_avg_redeemed = df[df['AvgRedeemed'] < lower_avg_redeemed]

    avg_trans_value_75percentil = df['AvgTransactionValue'].quantile(0.75)
    df_lowerAvg_higherAvgTrans = df[(df["AvgRedeemed"] < lower_avg_redeemed) & 
                                    (df["AvgTransactionValue"] > avg_trans_value_75percentil)]

    with open(SAVE_REPORT_PATH, 'a', encoding='utf-8') as f:
        print('----------------\nResultado Questão 04', file=f)
        print(f'\nO 10º percentil da média de resgate é {lower_avg_redeemed}', file=f)
        print(f'\n O 75º percentil da média de transação é {avg_trans_value_75percentil}', file=f)
        print(f'\nOs IDS que estão com baixa média de resgate são:\n{df_lower_avg_redeemed[["CustomerID", "AvgRedeemed"]].to_markdown(index=False, numalign="left", stralign="left")}', file=f)
        print(f'\nOs IDS que estão com baixa média de resgate e alta média de transação são:\n{df_lowerAvg_higherAvgTrans[["CustomerID", "AvgRedeemed"]].to_markdown(index=False, numalign="left", stralign="left")}', file=f)
    
    print('dados carregados') 


if __name__ == '__main__':
    main()