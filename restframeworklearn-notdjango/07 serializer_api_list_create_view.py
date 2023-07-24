import requests

# TODO : DO not run using same Title will create repetition
api_url = "http://127.0.0.1:8000/drf/product/create_list/" # 1 is product id

get_response = {}

create_params_dict = {
    "title": "Hello Rekha",
    "content": "telling Hello to Rekha",
    "price": 100.99
}
view_params_dict = {
    "title": "Hello Rekha",
}

request_type = input("What you want 1. Create or 2. View 3. View All : ")
request_type = request_type.lower()

if request_type == 'create':
    get_response = requests.post(api_url, json=create_params_dict)
elif request_type == 'view':
    get_response = requests.post(api_url, json=view_params_dict)
elif request_type == 'view all':
    get_response = requests.get(api_url)
else:
    print('Not IN Option')



print(get_response.json())
print(get_response.status_code)

