from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime
from macros import get_flask_response_wth_arguments

default_args = {
    'owner': 'Anirban Saha',
    'start_date': datetime(2023, 10, 15),
    'retries': 1,
}
dag = DAG(
    'macros__with_arguments_dag',
    default_args=default_args,
    schedule_interval=None,
    user_defined_macros = {'get_flask_response_wth_arguments': get_flask_response_wth_arguments},
    render_template_as_native_obj = True,  
    catchup=False,
)

def print_flask_response(str_):
    print(f"The Function returned the following output: {str_}")

op_str_='abc'
print_response_task = PythonOperator(
    task_id='print_response_task',
    python_callable=print_flask_response,
    op_kwargs = {"str_": f"{{{{ get_flask_response_wth_arguments(op_str='{op_str_}') }}}}"},
    provide_context=True,
    dag=dag,
)

print_response_task  # Set the task dependency

