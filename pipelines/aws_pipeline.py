from etls.aws_etl import connect_to_s3, create_bucket, upload_to_s3
from utils.constants import AWS_BUCKET_NAME


def load_data_to_s3(ti):
    file_path = ti.xcom_pull(task_ids = 'reddit_extraction', key='return_value')
    s3 = connect_to_s3()
    create_bucket(s3, AWS_BUCKET_NAME)
    upload_to_s3(s3, file_path, AWS_BUCKET_NAME, file_path.split('/')[-1])
