import requests
FLASK_ENDPOINT_URL="http://flask-app:5001"

def get_flask_response(**kwargs):
    try:
        response = requests.get(FLASK_ENDPOINT_URL)
        if response.status_code == 200:
            result = response.text
            print("Response - ", result)
            return result
        else:
            return f"Request failed with status code {response.status_code}"
    except requests.exceptions.RequestException as e:
        return f"An error occurred: {e}"


def get_flask_response_wth_arguments(op_str=None):
    try:
        response = requests.get(FLASK_ENDPOINT_URL)
        if response.status_code == 200:
            result = response.text
            print(f"Response - {op_str} - ", result)
            return result
        else:
            return f"Request failed with status code {response.status_code}"
    except requests.exceptions.RequestException as e:
        return f"An error occurred: {e}"