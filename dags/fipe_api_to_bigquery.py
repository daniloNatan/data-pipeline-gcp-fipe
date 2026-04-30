from airflow.sdk.definitions.context import render_template_as_native
from pendulum import Timezone
from airflow import DAG
from datetime import datetime
import pendulum

with DAG(
    dag_id='fipe_api_to_bigquery',
    start_date=pendulum.datetime(2026, 4, 30, 0, 0, 0, tz='America/São_Paulo'),
    schedule= '@daily',
    catchup= True,
    max_active_runs = 1
) as dag:

    