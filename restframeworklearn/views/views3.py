from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from rest_framework import generics  # generics has many view's

from restframeworklearn.serializers import ProductModelSerializer
from restframeworklearn.models import Product
from ..mixins import UserQuerySetMixin
from ..pagination import ProductListPagePagination, ProductListCursorPagination, ProductListLimitOffsetPagination


class ProductListAPIview(generics.ListAPIView, UserQuerySetMixin):
    """
    UserQuerySetMixin : this is not working Learn More.
    """
    queryset = Product.objects.all()
    serializer_class = ProductModelSerializer
    pagination_class = ProductListPagePagination
    # pagination_class = ProductListPagination
    # pagination_class = ProductListCursorPagination

    def list(self, request, *args, **kwargs):
        print("request :", request)  # dir(request)
        print("args :", args)
        print("kwargs :", kwargs)
        return super().list(self, request, *args, **kwargs)

    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset() # get_queryset() has not any  prams *args, **kwargs
        request = self.request
        user = request.user
        if not user.is_authenticated:
            return Product.objects.none()
        return qs.filter(user=user)


class ProductDetailAPIview(generics.RetrieveAPIView):
    # Using this we want to serialize data of model
    # Detail view take one single item
    queryset = Product.objects.all()  # we can get custom queryset in djagno find??
    serializer_class = ProductModelSerializer
    # lookup_field = 'pk'  # on which fild we want to perform lookup on

    def get(self, request, *args, **kwargs):
        print("request :", request)  # dir(request)
        print("args :", args)
        print("kwargs :", kwargs)
        return super().get(self, request, *args, **kwargs)

    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset() # get_queryset() has not any  prams *args, **kwargs
        request = self.request
        user = request.user
        if not user.is_authenticated:
            return Product.objects.none()
        return qs.filter(user=user)


@method_decorator(csrf_exempt, name='dispatch')
class ProductCreateAPIview(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductModelSerializer

    def perform_create(self, serializer):
        """
        if we are using create method in serialize then we do not need to over wright to this method here.
        """
        email = serializer.validated_data.pop('email')
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content') or None
        print('content :', content)
        print(content is None)
        print(content is not None)
        print(content == '')
        print(content != '')
        if content is None:
            serializer.validated_data['content'] = title
        print('request.user :', self.request.user)
        serializer.validated_data['user'] = self.request.user
        serializer.save() #  # we do not save here then it will not save and also specify value ....
        # serializer.save(user=self.request.user, content=content)  # this is not working why?
        # which we want to add
        # we can also use Django signals # need to learn this

    # def get_queryset(self, *args, **kwargs):
    #     qs = super().get_queryset() # get_queryset() has not any  prams *args, **kwargs
    #     request = self.request
    #     user = request.user
    #     if not user.is_authenticated:
    #         return Product.objects.none()
    #     return qs.filter(user=user)

@method_decorator(csrf_exempt, name='dispatch')
class ProductUpdateAPIview(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductModelSerializer

    def perform_update(self, serializer):
        """
        for update, we have this method to overwrite.
        """
        return super().perform_update(serializer)  # self is not required, why?


@method_decorator(csrf_exempt, name='dispatch')
class ProductDeleteAPIview(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductModelSerializer

    def perform_destroy(self, instance):
        """
        for update, we have this method to overwrite.
        """
        return super().perform_destroy(instance)  # self is not required, why?


## ---------------- This 2 generics Class Only Needed to Create CRUD --------------------- #
class ProductListCreateAPIview(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductModelSerializer


class ProductRetrieveUpdateDestroyAPIview(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductModelSerializer

