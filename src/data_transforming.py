import pandas as pd
import dataframe_image as dfi
from typing import List, Any, Optional


def export_table_img(df: pd.DataFrame, local_path: str, title_table: str) -> pd.DataFrame:
    """Cria uma imagem de tabela para o dataset e exporta para pasta selecionada.

    Args:
        df (pd.DataFrame): dataset para transformar em tabela
        local_path (str): local onde imagem será salva.
        title_table (str): Título que vai em cima da tabela.

    Returns:
        pd.DataFrame: carrega dataset em tabela.
    """
    style_df = df.copy()

    style_df = style_df.style.set_table_styles([{'selector': 'tr:nth-child(even)',
                                                 'props': [('background', "#746f6f")]}]).hide()\
        .format(precision=2, thousands='.', decimal=',')\
        .set_caption(f'<h3>{title_table}</h3>')
    dfi.export(style_df, local_path, table_conversion='matplotlib')
    print('imagem gerada')
