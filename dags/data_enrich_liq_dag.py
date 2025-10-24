from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import os
from integrations import geocode_util
from transformers import address_transformer

def dataEnrichLiqRun():
	print('Data Enrichment with LocationIQ')
	results = geocode_util.get_structured_address()
	address_transformer.transform(results)
	print("File output_sample.json should be generated")
	print("Please check to directory ./data/int_output")

with DAG(dag_id="data_enrich_liq_dag",
	start_date=datetime(2025,9,5),
	schedule_interval=None,
	catchup=False) as dag:

	task_run = PythonOperator(
		task_id="run_task_id",
		python_callable=dataEnrichLiqRun
	)

task_run
