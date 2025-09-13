FROM apache/airflow:3.0.6-python3.9

USER root
RUN apt-get update && apt-get install -y gcc python3-dev && apt-get clean

USER airflow

COPY requirements.txt /opt/airflow/
RUN pip install --no-cache-dir -r /opt/airflow/requirements.txt