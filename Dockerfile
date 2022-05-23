FROM apache/airflow:2.3.0
COPY requirements.txt .
RUN pip install -r requirements.txt
RUN python -m textblob.download_corpora