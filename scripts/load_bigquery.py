import pandas as pd
import pandas_gbq as gbq
import os
from dotenv import load_dotenv

load_dotenv()

project_id = os.getenv('GCP_PROJECT_ID')
table_id = os.getenv('GCP_TABLE_ID')

def load_to_bigquery(df: pd.DataFrame, project_id: str, table_id: str) -> None:
    """Carrega um DataFrame do pandas em uma tabela do Google BigQuery.

    Args:
        df (pd.DataFrame): O DataFrame contendo os dados a serem carregados.
        project_id (str): O ID do Projeto no Google Cloud onde reside o dataset/tabela de destino.
        table_id (str): O ID da tabela de destino no BigQuery no formato 'dataset.tabela'.
    """
    try:
        gbq.to_gbq(df, table_id, project_id=project_id, if_exists='replace')

    except Exception as err:
        print(f'Erro ao carregar dados para o Big Query: {err}')
        raise