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
