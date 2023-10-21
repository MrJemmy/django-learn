from django.urls import path, include
from restframeworklearn.views.views1 import test_api, get_random_product, drf_api_view
from restframeworklearn.views.views2 import TestCRUDView
from restframeworklearn.views.views3 import (
    ProductListAPIview, ProductListCreateAPIview, ProductRetrieveUpdateDestroyAPIview, ProductDetailAPIview,
    ProductCreateAPIview, ProductUpdateAPIview)
from .views.views4 import MixinsAPIView
from .routers import router

urlpatterns = [
    path('test_api/', test_api),
    path('get_random_product/', get_random_product),
    path('get_by_drf_api/', drf_api_view),
    # views2
    path('test_crud_view/', TestCRUDView.as_view()),
    path('test_crud_view/<int:id>/', TestCRUDView.as_view()),
    # views3
    path('product/', ProductListAPIview.as_view()),  # , name='product-list'
    path('product/<int:pk>/', ProductDetailAPIview.as_view(), name='product-detail'), # pk is set in ProductDetailAPIview.lookup_field, we use pk we can change it also
    path('product/create/', ProductCreateAPIview.as_view()),
    path('product/<int:pk>/update/', ProductUpdateAPIview.as_view(), name='product-edit'),
    path('product/getList_create/', ProductListCreateAPIview.as_view()),
    path('product/getSingle_update_delete/<int:pk>/', ProductRetrieveUpdateDestroyAPIview.as_view()),
    # views4
    path('product/mixins/', MixinsAPIView.as_view()),  # for get: List, post: Create,
    path('product/mixins/<int:pk>/', MixinsAPIView.as_view()),  #  for get: Retrive
    # views5
    path('', include(router.urls)),
    # ProductListCreateAPIview.as_view()
]
