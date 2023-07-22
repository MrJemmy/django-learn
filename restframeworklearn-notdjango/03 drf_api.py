import requests

api_url = "http://127.0.0.1:8000/drf/get_by_drf_api"

get_response = {}

request_type = input("Please input request type 1. GET or 2. POST : ")
request_type = request_type.lower()

if request_type == 'get':
    get_response = requests.get(api_url) # Http GET Request
elif request_type == 'post':
    get_response = requests.post(api_url, json={'title':'Hello Harsh'})  # Http POST Request
else:
    get_response = requests.put(api_url)  # Http PUT Request / Do not know anything Learn.
    print('Not IN Option, Just For Testing.')

if get_response is not None:
    print(get_response)
    print(get_response.json())
    print(get_response.status_code)