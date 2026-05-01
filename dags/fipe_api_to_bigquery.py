from airflow.sdk.definitions.context import render_template_as_native
from airflow import DAG
import pendulum
from airflow.operators.python import PythonOperator
from scripts.extract_fipe import extrair_dados
from scripts.data_transform import data_transform
from scripts.load_bigquery import load_to_bigquery
from dotenv import load_dotenv
import os

load_dotenv()
project_id = os.getenv('GCP_PROJECT_ID')
table_id = os.getenv('GCP_TABLE_ID')
url = os.getenv('FIPE_API_URL')

with DAG(
    dag_id='fipe_api_to_bigquery',
    start_date=pendulum.datetime(2026, 4, 30, 0, 0, 0, tz='America/São_Paulo'),
    schedule= '@daily',
    catchup= True,
    max_active_runs = 1,
    render_template_as_native_obj=True
) as dag:

    extract_data = PythonOperator(
        dag=dag,
        task_id='extract_data',
        python_callable=extrair_dados,
        op_kwargs={ "url" : url }
    )

    transform_data = PythonOperator(
        dag=dag,
        task_id='transform_data',
        python_callable=data_transform,
        op_kwargs={ "dados_brutos_json" :  "{{ ti.xcom_pull(task_ids='extract_data') }}"}
    )

    load_data = PythonOperator(
        dag=dag,
        task_id='load_data',
        python_callable=load_to_bigquery,
        op_kwargs={ "df" : "{{ ti.xcom_pull(task_ids='transform_data')}}",
        "project_id" : project_id,
        "table_id" : table_id
        }
    )

    extract_data >> transform_data >> load_data
