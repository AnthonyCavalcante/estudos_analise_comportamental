import pandas as pd
import numpy as np 
from data_processing import load_data_csv

def main():
    LOAD_PATH = '/workspaces/Data/processed/desafio_semanal_4_dados_processados.csv'
    SAVE_TXT_PATH = '/workspaces/outputs/reports/report_question02.txt'

    df = load_data_csv(LOAD_PATH)
    #Create columns 
    condition = [(df['CustomerFeedbackScore'] < 3), 
                 (df['CustomerFeedbackScore'] == 3),
                 (df['CustomerFeedbackScore'] > 3)]
    score = ['negativo', 'neutro', 'positivo']

    df['CustomerScoreClass'] = np.select(condition, score, '-')
    transactionMeanSeries = df.groupby('Tier')['NumTransactionsLast90Days'].transform('mean')
        
    #Criando os datasets de respostas
    
    churned_series_classification = (df.groupby('CustomerScoreClass')['ChurnedLoyaltyProgram']
                                    .value_counts(normalize=True).reset_index()
                                    .rename(columns={'proportion':'ChurnRate'}).round(2)
                                    .loc[lambda churned_series_classification:churned_series_classification['ChurnedLoyaltyProgram'] ==True])
    
    
    df_neg_tier = df.loc[(df['CustomerScoreClass'] == 'negativo') &
                         (df['ChurnedLoyaltyProgram'] ==False) &
                         (df['NumTransactionsLast90Days'] > transactionMeanSeries), 
                         ['CustomerID', 'Tier', 'CustomerScoreClass','NumTransactionsLast90Days' ]].reset_index(drop=True)
    
   
    
    with open(SAVE_TXT_PATH, 'a', encoding='utf-8') as f:
        print('\n----------------------\n Questão 05\n', file=f)
        print('Taxa de classificação de feedbacks para usuários churnados', file=f)
        print(f'{churned_series_classification.to_markdown(index=False, stralign="left", numalign="left")}\n', file=f)
        print('Clientes com feedback negativo mas com taxa de transaçã acima da média', file=f)
        print(df_neg_tier.to_markdown(index=False, stralign="left", numalign="left"), file=f)
        print('arquivos salvos')



if __name__ == '__main__':
    main()