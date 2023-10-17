from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

from .serializers import ProductModelSerializer, ProductSerializer

from .models import Product

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