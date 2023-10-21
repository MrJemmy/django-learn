from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated

from restframeworklearn.serializers import ProductModelSerializer

from restframeworklearn.models import Product


## ---------------- This Class only require for perfoming CRUD --------------------- #
class ProductModleViewSet(viewsets.ModelViewSet):
    """
    This class base view used when for one URL you want to create GET, POST, PUT, DELETE all
    to use in urls : path('url/', ClassBaseView.as_view()),
    """
    queryset = Product.objects.all()
    serializer_class = ProductModelSerializer
    # authentication_classes = [SessionAuthentication]
    # permission_classes = [IsAuthenticated]

## ---------------- Ready only --------------------- #
class ProductReadOnlyModleViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This class base view used when for one URL you want to create GET, POST, PUT, DELETE all
    to use in urls : path('url/', ClassBaseView.as_view()),
    """
    queryset = Product.objects.all()
    serializer_class = ProductModelSerializer