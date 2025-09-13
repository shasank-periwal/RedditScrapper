from airflow import DAG
from airflow.providers.standard.operators.python import PythonOperator 
from datetime import datetime 
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from pipelines.reddit_pipeline import redditpipeline


default_args = {
    'owner' : 'Shasank Periwal',
    'retries' : 3,
    'start_date': datetime(2025, 9, 13)
}

file_postfix = datetime.now().strftime("%Y%m%d")

dag = DAG(
    dag_id= "etl_reddit_pipeline",
    default_args=default_args,
    catchup=False,
    schedule_interval = '@daily',
    tags=['reddit', 'etl', 'pipeline']
)

extract = PythonOperator(
    task_id = 'reddit_extraction',
    python_callable = redditpipeline,
    opkwargs = {
        'filename': f"reddit_{file_postfix}",
        'subreddit': 'dataengineering',
        'timefilter': 'day',
        'limit': 10
    },
    dag = dag
)