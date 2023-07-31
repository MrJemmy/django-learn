import requests

api_url = "http://127.0.0.1:8000/drf/test_crud_view/"

get_response = {}

print("To GET data type 1")
print("To Create/Add data type 2")
print("To Update data type 3")
print("To Partial Update data type 4")
print("To Delete data type 5")
request_type = int(input())

if request_type == 1:
    get_response = requests.get(api_url, params={'with_model_serializer': 0}) # Http GET Request
    # get_response = requests.get(api_url, params={'id': 1, 'with_model_serializer': 0}) # Http GET Request
elif request_type == 2:
    get_response = requests.post(api_url, data={'title':'Hello jenny'}, params={'with_model_serializer': 0})  # Http POST Request
elif request_type == 3:
    get_response = requests.put(api_url, data={'id': 4, 'title':'Jemmy', 'content' : 'hello its me jemmy', 'price': 100}, params={'with_model_serializer': 0})  # Http POST Request
elif request_type == 4:
    get_response = requests.patch(api_url, data={'id': 2, 'title':'Harsh',}, params={'with_model_serializer': 0})  # Http POST Request
elif request_type == 5:
    get_response = requests.delete(api_url, data={'id':3})  # Http POST Request
else:
    get_response = requests.put(api_url)  # Http PUT Request / Do not know anything Learn.
    print('Not IN Option, Just For Testing.')

if get_response is not None:
    print(get_response)
    print(get_response.json())
    print(get_response.status_code)