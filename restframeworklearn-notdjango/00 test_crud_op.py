import requests

api_url = "http://127.0.0.1:8000/drf/test_crud_view/"

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
    get_response = requests.get(api_url, params={'with_model_serializer': 1}, headers=headers) # Http GET Request
    # get_response = requests.get(api_url, params={'id': 1, 'with_model_serializer': 1}, headers=headers) # Http GET Request
elif request_type == 2:
    get_response = requests.post(api_url, data={'title':'GJ', 'content':'This is Gunjan and Jaimin'}, params={'with_model_serializer': 1}, headers=headers)  # Http POST Request
elif request_type == 3:
    get_response = requests.put(api_url, data={'id': 4, 'title':'Roshni', 'content' : 'hello I am a Teacher', 'price': 500}, params={'with_model_serializer': 1}, headers=headers)  # Http put Request
elif request_type == 4:
    get_response = requests.patch(api_url, data={'id': 5, 'content':'This is Gunjan Here',}, params={'with_model_serializer': 1}, headers=headers)  # Http patch Request
elif request_type == 5:
    get_response = requests.delete(api_url, data={'id':3}, headers=headers)  # Http delete Request
else:
    get_response = requests.put(api_url)  # Http PUT Request / Do not know anything Learn.
    print('Not IN Option, Just For Testing.')

if get_response is not None:
    print(get_response)
    print(get_response.json())
    print(get_response.status_code)