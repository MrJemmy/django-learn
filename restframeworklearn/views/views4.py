from rest_framework import generics, mixins
from rest_framework.permissions import IsAuthenticated

from restframeworklearn.serializers import ProductModelSerializer
from restframeworklearn.models import Product


class MixinsAPIView(generics.GenericAPIView, mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.CreateModelMixin):
    """
    generics.ListAPIView use mixins.ListModelMixin and works
    but
    """
    serializer_class = ProductModelSerializer
    queryset = Product.objects.all()
    # queryset = Product.objects.filter(price__exact=99.99)
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        print("request :", request)
        print("request headers :", request.headers)
        print("request dir :", dir(request))
        print("request auth:", request.auth)
        print("request authenticators:", request.authenticators)
        print("request parsers:", request.parsers)
        print("args :", args)
        print("kwargs :", kwargs)
        pk = kwargs.get('pk')
        if pk is not None:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        """
        we can overwrite 'perform_create' method to perform custom tasks
        we can directly call 'perform_create' or 'create' method will call indirectly
        """
        return self.create(request, *args, **kwargs)