from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

with DAG(
    dag_id='simple_sequential_dag',
    start_date=datetime(2023, 1, 1),
    schedule_interval='@daily',
    catchup=False,
    default_args={
        'owner': 'airflow',
        'depends_on_past': False,
        'email_on_failure': False,
        'email_on_retry': False,
        'retries': 1,
        'retry_delay': timedelta(minutes=5),
    },
) as dag:
    task_1 = BashOperator(
        task_id='task_1',
        bash_command='echo "Executing Task 1"',
    )

    task_2 = BashOperator(
        task_id='task_2',
        bash_command='echo "Executing Task 2"',
    )

    task_3 = BashOperator(
        task_id='task_3',
        bash_command='echo "Executing Task 3"',
    )

    task_1 >> task_2 >> task_3  # Define sequential dependency