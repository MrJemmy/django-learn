from rest_framework import generics, viewsets  # generics has many view's
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated

from .serializers import ProductModelSerializer

from .models import Product


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


## ---------------- This 2 generics Class Only Needed to Create CRUD --------------------- #
class ProductListCreateAPIview(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductModelSerializer


class ProductRetrieveUpdateDestroyAPIview(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductModelSerializer


## ---------------- This Class only require for perfoming CRUD --------------------- #
class ProductModleViewSet(viewsets.ModelViewSet):
    """
    This class base view used when for one URL you want to create GET, POST, PUT, DELETE all
    to use in urls : path('url/', ClassBaseView.as_view()),
    """
    queryset = Product.objects.all()
    serializer_class = ProductModelSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]

## ---------------- Ready only --------------------- #
class ProductReadOnlyModleViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This class base view used when for one URL you want to create GET, POST, PUT, DELETE all
    to use in urls : path('url/', ClassBaseView.as_view()),
    """
    queryset = Product.objects.all()
    serializer_class = ProductModelSerializer