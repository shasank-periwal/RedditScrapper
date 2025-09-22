from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime 
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
# sys.path.insert(0, '/opt/airflow')

from pipelines.aws_pipeline import load_data_to_s3
from pipelines.reddit_pipeline import redditpipeline


default_args = {
    'owner' : 'Shasank Periwal',
    'retries' : 1,
    'start_date': datetime(2025, 9, 13)
}

file_postfix = datetime.now().strftime("%Y%m%d")

dag = DAG(
    dag_id= "etl_reddit_pipeline",
    default_args=default_args,
    catchup=False,
    schedule = '@daily',
    tags=['reddit', 'etl', 'pipeline']
)

extract = PythonOperator(
    task_id = 'reddit_extraction',
    python_callable = redditpipeline,
    op_kwargs = {
        'filename': f"reddit_{file_postfix}",
        'subreddit': 'dataengineering',
        'timefilter': 'day',
        'limit': 10
    },
    dag = dag
)

s3_aws = PythonOperator(
    task_id = 'local_to_aws',
    python_callable=load_data_to_s3,
    dag = dag
)

extract >> s3_aws