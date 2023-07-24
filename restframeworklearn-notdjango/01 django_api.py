import requests

api_url = "http://127.0.0.1:8000/drf/django_api/" # get json response // REST API-response
# "http://127.0.0.1:8000/django_api?user_id=2614" -> params={'user_id': 2614} this are query params

get_response = requests.get(api_url, params={'user_id': 2614}, json={"query" : "my_query"}) # Http Request
print(get_response.json()) 
print(get_response.status_code)