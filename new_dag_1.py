from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

with DAG(
    "example_2",
    start_date=datetime(2025, 1, 1),
    schedule="@daily", catchup=False
) as dag:
    hello = BashOperator(task_id="task", bash_command="whoami")
    print(hello)