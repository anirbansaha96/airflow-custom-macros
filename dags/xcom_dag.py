from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime
import requests

default_args = {
    'owner': 'Anirban Saha',
    'start_date': datetime(2023, 10, 15),
    'retries': 1,
}
FLASK_ENDPOINT_URL="http://flask-app:5001"
dag = DAG(
    'xcom_dag',
    default_args=default_args,
    schedule_interval=None,  
    catchup=False,
)
def get_flask_response(**kwargs):
    try:
        response = requests.get(FLASK_ENDPOINT_URL)
        if response.status_code == 200:
            result = response.text
            print("Response - ", result)
            kwargs['ti'].xcom_push(key='flask_response', value=result)  # Push the result to XCom
            return result
        else:
            return f"Request failed with status code {response.status_code}"
    except requests.exceptions.RequestException as e:
        return f"An error occurred: {e}"

def print_flask_response(**kwargs):
    ti = kwargs['ti']
    response_text = ti.xcom_pull(task_ids='get_flask_response_task', key='flask_response')
    print(f"The Function returned the following output: {response_text}")

get_flask_response_task = PythonOperator(
    task_id='get_flask_response_task',
    python_callable=get_flask_response,
    provide_context=True,
    dag=dag,
)

print_response_task = PythonOperator(
    task_id='print_response_task',
    python_callable=print_flask_response,
    provide_context=True,
    dag=dag,
)

get_flask_response_task >> print_response_task  # Set the task dependency

