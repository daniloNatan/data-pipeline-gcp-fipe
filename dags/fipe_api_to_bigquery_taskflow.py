import pendulum
from airflow.sdk import dag, task
from scripts.extract_fipe import extrair_dados
from scripts.data_transform import data_transform
from scripts.load_bigquery import load_to_bigquery

@dag(
    dag_id='fipe_api_to_bigquery_taskflow',
    start_date=pendulum.datetime(2026, 4, 1, tz='America/São_Paulo'),
    schedule='@daily',
    catchup= True,
    max_active_runs= 1,
    tags=["fipe", "api", "bigquery", "etl"]
)
def fipe_pipeline():
    """Orquestra a extração de dados da API da FIPE e seu carregamento no BigQuery utilizando arquivos intermediários em disco.

    Returns:
        DAG: Objeto da DAG do Airflow contendo o fluxo de tarefas.
    """
    
    @task()
    def extract():
        return extrair_dados()

    @task()
    def transform(caminho_bruto):
        return data_transform(caminho_bruto=caminho_bruto)

    @task()
    def load(caminho_limpo):
        load_to_bigquery(caminho_limpo=caminho_limpo)

    raw_path = extract()
    transformed_path = transform(raw_path)
    load(transformed_path)

fipe_pipeline()
