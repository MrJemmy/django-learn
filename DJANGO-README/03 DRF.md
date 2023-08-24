## GenericAPIView
#### Attributes
1. queryset
   1. either set this attribute of override the get_queryset() method and call this method
   2. it will cache for all subsequent requests.
2. serializer_class
   1. set or override get_serializer_class() method
3. lookup_field
   1. ?
4. lookup_url_kwarg
   1. ?
5. pagination_class
   1. ?
6. filter_backends
   1. list of filter that should be used for filtering the queryset.

#### Methods
1. get_queryset(self)
   1. it returns the queryset used for list views // specified in queryset attribute
   2. it is evaluated only once for subsequent request 
2. get_objects(self)
   1. returns and object used for detail views  // Default to using the lookup_field parameter to fileter the base queryset
3. get_serializer(self)
   1. return class of serializer  // default return serializer_class attribute.
4. get_serializer_context(self)
   1. ?
5. get_serializer(self, instance=None, data+None, many=False, partial=False)
   2. it returns a serializer instance.
6. get_paginated_response(self, data)
   1. ?
7. paginate_queryset(self, queryset)
   1. ?
8. filter_queryset(self, queryset)
   1. return new query based on filter_backends queryset


#### Mixins
- mainly use for CRUD operations. but not used much, many inbuilt classed are built using mixins
- mixins provides action methods used to provide view behavior rather than handler methods like get(). post() methods
1. ListModelMixin
2. CreateModelMixing
3. RetrieveModelMixing
4. UpdateModelMixing
5. DestroyModelMixing


#### Mixins + GenericAPIView = Concrete APIViews
- Basic APIView
1. ListAPIView (GET method)
   1. Implementation of ListModelMixin + GenericAPIView
2. CreateAPIView (POST method)
   1. Implementation of CreateModelMixing + GenericAPIView
3. RetrieveAPIView (GET method)
   1. Implementation of RetrieveModelMixing + GenericAPIView
   2. model instance only
4. UpdateAPIView (PUT & PATCH method)
   1. Implementation of UpdateModelMixing + GenericAPIView
   2. model instance only
5. DestroyAPIView (DELETE method)
   1. Implementation of DestroyModelMixing + GenericAPIView
   2. model instance only
- Combination Concrete APIview
6. ListCreateAPIView (GET & POST method)
    1. ListAPIView + CreateAPIView
7. RetrieveUpdateAPIView (GET & PUT & PATCH method)
   1. RetrieveAPIView + UpdateAPIView
   2. model instance only
8. RetrieveDestroyAPIView (GET & DELETE method)
   1. RetrieveAPIView + DestroyAPIView
   2. model instance only
9. RetrieveUpdateDestroyAPIView (GET & PUT & PATCH & DELETE method)
   1. RetrieveAPIView + UpdateAPIView + DestroyAPIView 
   2. model instance only

- ListCreateAPIView & RetrieveUpdateDestroyAPIView will create all CRUD oppressions.


#### ViewSet & ModelViewSet Class
- combine set of related views in a single class, called a ViewSet
- no longer need to deal with wiring up the URL conf ourselves.
- code :
  - code in these methods for ViewSet will be all most same as Class Based APIView.
  - code in these for ModelViewSet will be same as generics APIview (only 2 line of code)
```bash
  from rest_framework import viewsets
  class StudentViewSet(viewsets.ViewSet):
        # for ViewSet
        def list(self, request):
          ......
        def create(self, request):
          ......
        def retrieve(self, request, pk=None):
          ......
        def update(self, request, pk=None):
          ......
        def partial_update(self, request, pk=None):
          ......
        def destroy(self, request, pk=None):
          ......
      
  # for ModelViewSet
  class StudentViewSet(viewsets.ModleViewSet):
        queryset = Product.objects.all()
        serializer_class = ProductModelSerializer
    
  # for read only ModelViewSet
  class StudentViewSet(viewsets.ReadOnlyModleViewSet):
        queryset = Product.objects.all()
        serializer_class = ProductModelSerializer
```
- URL configration for this
```bash
   from django.urls import path, include
   from django_app import views
   from rest_framework.routers import DefaultRouter
   
   router = DefaultRouter()
   router.register('url_of_view_set', views.ClassViewSet, basename='test')
   
   urlpatterns = [
      path('base_url/', include(router.urls))
   ]
```

- during dispatch, following attributes are available on ViewSet Class (How can we use in ModelViewSet)
  - basename : URL names that are created.
  - action : 
  - detail : 
  - suffix :
  - name : 
  - description :


## Authentication 
    - BasicAuthentication
    - SessionAuthentication
    - TokenAuthentication
    - RemoteUserAuthentication
    - Custom Authentication
- first Authentication performs after that Permissions (Authorization) performs in view
- based on Authentication `self.user` and `self.auth` with get values 

### Permission
    - AllowAny
    - IsAuthenticated
    - IsAdminUser
    - IsAuthenticatedOrReadOnly
    - DjangoModelPermissions
    - DjangoModlePermissionsOrAnonReadOnly
    - DjangoObjectPermissions
    - Custom Permissions
- Grant or deny access of Class and different part of API
- it uses the `self.user` and `self.auth` to determine request should permitted or not.




