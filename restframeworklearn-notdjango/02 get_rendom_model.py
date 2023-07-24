import requests

api_url = "http://127.0.0.1:8000/drf/get_random_product/"

get_response = requests.get(api_url) # Http Request
print(get_response.json()) 
print(get_response.status_code)