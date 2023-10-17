from django.urls import path, include
from .views import test_api, get_product_model, drf_api_view, ProductDetailAPIview, ProductCreateAPIview
from .views2 import TestCRUDView
from .views3 import ProductListCreateAPIview, ProductRetrieveUpdateDestroyAPIview,  ProductModleViewSet, ProductReadOnlyModleViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('view_set', ProductModleViewSet, basename='full_crud')
router.register('view_set_read_only', ProductReadOnlyModleViewSet, basename='read_only')
# use 'test', do not use 'test/' it call request 2 time

urlpatterns = [
    path('django_api/', test_api),
    path('get_random_product/', get_product_model),
    path('get_by_drf_api/', drf_api_view),
    # views2
    path('product/<int:pk>/', ProductDetailAPIview.as_view()),  # pk is set in ProductDetailAPIview.lookup_field, we use pk we can chage it also
    path('product/create/', ProductCreateAPIview.as_view()),
    path('test_crud_view/', TestCRUDView.as_view()),
    path('test_crud_view/<int:id>/', TestCRUDView.as_view()),
    # views3
    path('product/getList_create/', ProductListCreateAPIview.as_view()),
    path('product/getSingle_update_delete/<int:pk>/', ProductRetrieveUpdateDestroyAPIview.as_view()),
    path('', include(router.urls)),
    # ProductListCreateAPIview.as_view()
]
