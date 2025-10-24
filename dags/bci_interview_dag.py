from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import os
from integrations import geocode_util
from transformers import address_transformer

def bciInterviewRun():
	print('BCI Interview Run')
	results = geocode_util.get_structured_address()
	address_transformer.transform(results)
	print("File output_sample.json should be generated")
	print("Please check to directory ./data/int_test_output")

with DAG(dag_id="bci_interview_dag",
	start_date=datetime(2025,9,5),
	schedule_interval=None,
	catchup=False) as dag:

	task_run = PythonOperator(
		task_id="run_task_id",
		python_callable=bciInterviewRun
	)

task_run
