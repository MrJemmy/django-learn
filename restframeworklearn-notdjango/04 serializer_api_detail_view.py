import requests

# using generics.RetrieveAPIView getting full data of id 1 from Product model
api_url = "http://127.0.0.1:8000/drf/product/1/" # 1 is product id

get_response = requests.get(api_url)
print(get_response.json())
print(get_response.status_code)