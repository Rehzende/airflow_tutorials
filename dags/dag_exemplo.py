import os
import time
import pendulum
from airflow import DAG
from airflow.decorators import task
from airflow.settings import AIRFLOW_HOME

with DAG(
    dag_id="dag_exemplo_conta_ate_20",
    schedule=None,
    start_date=pendulum.datetime(2021, 1, 1, tz="UTC"),
    catchup=False,
    tags=["example"]
) as dag:
    @task(pool="worker-1", queue="worker-1")
    def count_to_twenty():
        for i in range(1, 21):
            print(f"Contando: {i} segundo(s)")
            time.sleep(1)
        print("Contagem concluída!")
        return "Contagem finalizada com sucesso"
    count_to_twenty()
