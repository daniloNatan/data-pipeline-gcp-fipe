import pandas as pd
import pandas_gbq as gbq
from airflow.models import Variable

def load_to_bigquery(caminho_limpo: str) -> None:
    """Lê o arquivo parquet processado a partir do caminho informado no XCom e realiza o push para a tabela do Google BigQuery.

    Args:
        caminho_limpo (str): O caminho local para o arquivo parquet limpo.
    """
    try:
        project_id = Variable.get('GCP_PROJECT_ID')
        table_id = Variable.get('GCP_TABLE_ID')

        df = pd.read_parquet(caminho_limpo)
        gbq.to_gbq(df, table_id, project_id=project_id, if_exists='replace')

    except Exception as err:
        print(f'Erro ao carregar dados para o Big Query: {err}')
        raise
