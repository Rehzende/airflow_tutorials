FROM apache/airflow:2.10.5

USER root
RUN apt-get update && apt-get install -y \
    curl \
    && rm -rf /var/lib/apt/lists/*
USER airflow
RUN pip install --no-cache-dir apache-airflow-providers-edge3 apache-airflow==2.10.5
EXPOSE 8080
