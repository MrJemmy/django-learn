import json

from django.http import JsonResponse
from django.forms.models import model_to_dict

from rest_framework.response import Response
from rest_framework.decorators import api_view

from restframeworklearn.models import Product
from restframeworklearn.serializers import ProductModelSerializer, ProductSerializer

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

def get_random_product(request, *args, **kwargs):
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
            instance = serializer.save()  # will save data into database
            print('Direct data : ', data)  # This is Direct data
            print('serialized data : ',serializer.data)  # This Returns All filed
            print('serialized data : ',serializer.validated_data)  # This is validated data
        else:
            # we can raise Exception also if we want
            print(serializer.errors)  # return Error Dict
            print(f'{data} is not valid data')
        return Response(serializer.data)
    # else:
    #     # This else condition will automatically be handled by DRF
    #     return Response({'detail': f'{request.method} is not allowed.'}, status=405)



