import requests

# TODO : DO not run using same Title will create repetition
api_url = "http://127.0.0.1:8000/product/create" # 1 is product id

params_dict = {
    "title": "Hello Harsh",
    "content": "telling Hello to Harsh",
    "price": 52.96
}

get_response = requests.post(api_url, json=params_dict)
print(get_response.json())
print(get_response.status_code)


# TODO : class ProductListCreateAPIview(generics.ListCreateAPIView):
# with just changing this we can create ProductListCreateAPIview
# with can view do create and view both