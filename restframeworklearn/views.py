import json
# from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.http import JsonResponse, QueryDict
from django.forms.models import model_to_dict

from rest_framework.views import APIView
from restframeworklearn.models import Product
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import ProductModelSerializer, ProductSerializer
from rest_framework import generics, status  # generics has many view's

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
    model_data = Product.objects.all().order_by('?').first()  # we can get product in any order
    data = {}
    if model_data:
        # 'model_to_dict' can not handel models property, can not return as json
        # Here also get issue with Float price converson.
        data = model_to_dict(model_data, fields=['id', 'title', 'price', 'sale_price'])
    return JsonResponse(data)

@api_view(['GET', 'POST'])
def drf_api_view(request, *args, **kwargs):  # Django Rest Framework API
    if request.method == 'GET':
        instance = Product.objects.all().order_by('?').first()  # we can get product in any order
        data = {}
        if instance:
            # serializer can handel models property, can return in json
            data = ProductModelSerializer(instance).data
            data_s = ProductSerializer(instance).data
            print(data_s) # this did not get property
        return Response(data)
    elif request.method == 'POST':
        print(request.body)  # can not read ".body" after reading ".data"
        data = request.data
        print(request.POST)
        print('data :', data)
        serializer = ProductModelSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            # instance = serializer.save()  # will save data into database
            print('Direct data : ', data)  # This is Direct data
            print('serialized data : ',serializer.data)  # This is validated data
        else:
            # we can raise Exception also if we want
            print(serializer.errors)  # return Error Dict
            print(f'{data} is not valid data')
        return Response(serializer.data)
    # else:
    #     # This else condition will automatically be handled by DRF
    #     return Response({'detail': f'{request.method} is not allowed.'}, status=405)

class ProductDetailAPIview(generics.RetrieveAPIView):
    # Using this we want to serialize data of model
    # Detail view take one single item
    queryset = Product.objects.all()  # we can get custom queryset in djagno find??
    serializer_class = ProductModelSerializer
    # lookup_field = 'pk'# on which fild we want to perform lookup on

class ProductCreateAPIview(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductModelSerializer

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


## ---------------- This 2 Class Only Needed to Create CRUD --------------------- #
class ProductListCreateAPIview(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductModelSerializer

class ProductRetrieveUpdateDestroyAPIview(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductModelSerializer



"""
This class base view used when for one URL you want to create GET, POST, PUT, DELETE all
to use in urls : path('url/', ClassBaseView.as_view()),
"""
@method_decorator(csrf_exempt, name='dispatch')
class TestCRUDView(APIView):
    def get(self, request, id=0, *args, **kwargs):
        data = request.query_params  # request.GET
        with_model_serializer = int(data.get('with_model_serializer', 1))
        if with_model_serializer:
            serializer = ProductModelSerializer
            if id:
                query = Product.objects.get(id=id)
                serialized = serializer(query)
                return Response({"data": [serialized.data]}, status=status.HTTP_200_OK)
            query = Product.objects.all()
            serialized = serializer(query, many=True)
            return Response({"data": serialized.data}, status=status.HTTP_200_OK)
        else:
            serializer = ProductSerializer
            if id:
                query = Product.objects.get(id=id)
                serialized = serializer(query)
                return Response({"data": [serialized.data]}, status=status.HTTP_200_OK)
            query = Product.objects.all()
            serialized = serializer(query, many=True)
            return Response({"data": serialized.data}, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        init_data = request.data  # request.POST
        data = init_data.get('data')
        with_model_serializer = int(init_data.get('with_model_serializer', 1))
        if with_model_serializer:
            serializer = ProductModelSerializer
            serialized = serializer(data=data)  # **need to write data=data
            if serialized.is_valid():
                serialized.save()
                return Response({"data": "data is created"}, status=status.HTTP_201_CREATED)
            else:
                return Response({"data": serialized.errors}, status=status.HTTP_400_BAD_REQUEST)
        else:
            serializer = ProductSerializer
            serialized = serializer(data=data)  # **need to write data=data
            if serialized.is_valid():
                serialized.save()
                return Response({"data": "data is created"}, status=status.HTTP_201_CREATED)
            else:
                return Response({"data": serialized.errors}, status=status.HTTP_400_BAD_REQUEST)
    def put(self, request, id=None,  *args, **kwargs):
        init_data = request.data # QueryDict(request.body)
        data = init_data.get('data')
        with_model_serializer = int(init_data.get('with_model_serializer', 1))
        if with_model_serializer:
            serializer = ProductModelSerializer
            query = Product.objects.get(id=id)
            serialized = serializer(query, data=data)  # to update whole data
            if serialized.is_valid():
                serialized.save()
                return Response({"data": "data is Updated"}, status=status.HTTP_200_OK)
            else:
                return Response({"data": serialized.errors}, status=status.HTTP_400_BAD_REQUEST)
        else:
            serializer = ProductSerializer
            query = Product.objects.get(id=id)
            serialized = serializer(query, data=data)  # to update whole data
            if serialized.is_valid():
                serialized.save()
                return Response({"data": "data is Updated"}, status=status.HTTP_200_OK)
            else:
                return Response({"data": serialized.errors}, status=status.HTTP_400_BAD_REQUEST)
    def patch(self, request, id=None, *args, **kwargs):
        init_data = request.data # QueryDict(request.body)
        data = init_data.get('data')
        with_model_serializer = int(init_data.get('with_model_serializer', 1))
        if with_model_serializer:
            serializer = ProductModelSerializer
            query = Product.objects.get(id=id)
            serialized = serializer(query, data=data, partial=True)  # to update partial data
            if serialized.is_valid():
                serialized.save()
                return Response({"data": "data is Updated"}, status=status.HTTP_200_OK)
            else:
                return Response({"data": serialized.errors}, status=status.HTTP_400_BAD_REQUEST)
        else:
            serializer = ProductSerializer
            query = Product.objects.get(id=id)
            serialized = serializer(query, data=data, partial=True)  # to update partial data
            if serialized.is_valid():
                serialized.save()
                return Response({"data": "data is Updated"}, status=status.HTTP_200_OK)
            else:
                return Response({"data": serialized.errors}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id=None, *args, **kwargs):
        qs = Product.objects.filter(id__icontains=id)
        if qs.exists():
            Product.objects.get(id=id).delete()
            return Response({"data" : "deleted successfully"}, status=status.HTTP_200_OK)
        return Response({"data": "this data is not exist"}, status=status.HTTP_404_NOT_FOUND)

