import json
from django.http import JsonResponse
from django.forms.models import model_to_dict
from restframeworklearn.models import Product
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import ProductSerializer
from rest_framework import generics  # generics has many view's

def test_api(request, *args, **kwargs):
    request_body = request.body  # this request -> Django's HttpRequest : it returns binary string (b'')
    data = {}
    try:
        data = json.loads(request_body)  # to convert json b'' -> to dict format
    except:
        pass
    data['headers'] = dict(request.headers)  # request.headers is not json serializable
    data['query_params'] = request.GET  # request params data
    # data['content_type'] = request.content_type # headers has already this info
    return JsonResponse(data)

def get_product_model(request, *args, **kwargs):
    model_data = Product.objects.all().order_by('?').first()
    data = {}
    if model_data:
        # 'model_to_dict' can not handel models property, can not return as json
        data = model_to_dict(model_data, fields=['id', 'title', 'price', 'sale_price'])
    return JsonResponse(data)

@api_view(['GET', 'POST'])
def drf_api_view(request, *args, **kwargs):  # Django Rest Framework API
    if request.method == 'GET':
        instance = Product.objects.all().order_by('?').first()
        data = {}
        if instance:
            # serializer can handel models property, can return in json
            data = ProductSerializer(instance).data
        return Response(data)
    elif request.method == 'POST':
        data = request.data
        serializer = ProductSerializer(data=data)
        if serializer.is_valid():
            # instance = serializer.save()  # will save data into database
            print(serializer.data)  # will give hole models data
        return Response(serializer.data)

class ProductDetailAPIview(generics.RetrieveAPIView):
    # Using this we want to serialize data of model
    # Detail view take one single item
    queryset = Product.objects.all()  # we can get custom queryset in djagno find??
    serializer_class = ProductSerializer
    # lookup_field = 'pk'# on which fild we want to perform lookup on

class ProductCreateAPIview(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        print(serializer)
        print(serializer.validated_data)
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content')
        if content is None:
            content = title
        # serializer.save(content=content)  # we do not save here then it will not save and also specify value ....
        # which we want to add
        # we can also use Django signals # need to learn this

class ProductListAPIview(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductListCreateAPIview(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer