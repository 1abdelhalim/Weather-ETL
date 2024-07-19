from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

default_args = {
    'owner': 'abdelhalim',
    'depends_on_past': False,
    'start_date': datetime(2024, 7, 19),
    'retries': 5,
}

def run_main_py():
    exec(open("/path/to/your/main.py").read())

with DAG(
    'etl_dag',
    default_args=default_args,
    description='A simple ETL DAG',
    schedule='@daily',  
    catchup=False, 
) as dag:
    run_etl = PythonOperator(
        task_id='run_main_py_task',  
        python_callable=run_main_py,
    )

    run_etl 

