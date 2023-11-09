from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime
from macros import get_flask_response

default_args = {
    'owner': 'Anirban Saha',
    'start_date': datetime(2023, 10, 15),
    'retries': 1,
}
dag = DAG(
    'macros_dag',
    default_args=default_args,
    schedule_interval=None,
    user_defined_macros = {'get_flask_response': get_flask_response},
    render_template_as_native_obj = True,  
    catchup=False,
)

def print_flask_response(str_):
    print(f"The Function returned the following output: {str_}")


print_response_task = PythonOperator(
    task_id='print_response_task',
    python_callable=print_flask_response,
    op_kwargs = {"str_": f"{{{{ get_flask_response() }}}}"},
    provide_context=True,
    dag=dag,
)

print_response_task  # Set the task dependency

