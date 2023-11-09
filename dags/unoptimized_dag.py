# from airflow import DAG
# from airflow.operators.python_operator import PythonOperator
# from datetime import datetime
# import requests

# default_args = {
#     'owner': 'Anirban Saha',
#     'start_date': datetime(2023, 10, 15),
#     'retries': 1,
# }
# FLASK_ENDPOINT_URL="http://flask-app:5001"
# dag = DAG(
#     'flask_call_dag',
#     default_args=default_args,
#     schedule_interval=None,  
#     catchup=False,
# )
# def get_flask_response():
#     try:
#         response = requests.get(FLASK_ENDPOINT_URL)
#         if response.status_code == 200:
#             print("Response - ", response.text)
#             return response.text
#         else:
#             return f"Request failed with status code {response.status_code}"
#     except requests.exceptions.RequestException as e:
#         return f"An error occurred: {e}"

# def print_flask_response(str_= None):
#     print(f"The Function returned the following output: {str_}")

# print_response_task = PythonOperator(
#     task_id='print_response_task',
#     python_callable=print_flask_response,
#     op_kwargs={"str_": get_flask_response()},
#     dag=dag,
# )

# print_response_task
