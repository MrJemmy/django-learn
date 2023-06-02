import requests

api_url = "http://127.0.0.1:8000/get_by_drf_api"

get_response = {}

request_type = input("Please input request type 1. GET or 2. POST : ")
request_type = request_type.lower()

if request_type == 'get':
    get_response = requests.get(api_url) # Http GET Request
elif request_type == 'post':
    get_response = requests.post(api_url, json={'title':'Hello Harsh'})  # Http GET Request
else:
    print('Not IN Option')

if get_response:
    print(get_response.json())
    print(get_response.status_code)