import requests
import json

get_response = {}

print("1. GET data")
print("2. Create/Add data")
print("3. Update data")
print("4. Partial Update data")
print("5. Delete data")
request_type = int(input())
"""
params={'with_model_serializer': 1}  -> for Model Serializer
params={'with_model_serializer': 0}  -> for Normal Serializer
"""
headers = {'content-Type' : 'application/json'}
if request_type == 1:
    # api_url = "http://127.0.0.1:8000/drf/test_crud_view/"
    # get_response = requests.get(api_url, params={'with_model_serializer': 1}, headers=headers) # Http GET Request
    api_url = "http://127.0.0.1:8000/drf/test_crud_view/1"
    get_response = requests.get(api_url, params={'with_model_serializer': 1}, headers=headers) # Http GET Request
elif request_type == 2:
    data = {
        'with_model_serializer': 1,
        'data' : {
            'title':'Hello 3',
            'content':'This is 3ed Hello'}
    }
    api_url = "http://127.0.0.1:8000/drf/test_crud_view/"
    get_response = requests.post(api_url, data=json.dumps(data), headers=headers)  # Http POST Request
elif request_type == 3:
    data = {
        'with_model_serializer': 1,
        'data': {
            'title': 'Hello 1',
            'content': 'This is 1st Hello'}
    }
    api_url = "http://127.0.0.1:8000/drf/test_crud_view/1"
    get_response = requests.put(api_url, data=json.dumps(data), headers=headers)  # Http put Request
elif request_type == 4:
    data = {
        'with_model_serializer': 1,
        'data': {
            'content': 'This is 2nd Hello'}
    }
    api_url = "http://127.0.0.1:8000/drf/test_crud_view/2"
    get_response = requests.patch(api_url, data=json.dumps(data), headers=headers)  # Http patch Request
elif request_type == 5:
    api_url = "http://127.0.0.1:8000/drf/test_crud_view/6"
    get_response = requests.delete(api_url, headers=headers)  # Http delete Request
else:
    get_response = requests.put(api_url)  # Http PUT Request / Do not know anything Learn.
    print('Not IN Option, Just For Testing.')

if get_response is not None:
    print(get_response)
    print(get_response.json())
    print(get_response.status_code)