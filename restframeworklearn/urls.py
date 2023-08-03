from django.urls import path
from .views import (
    test_api, get_product_model, drf_api_view, ProductDetailAPIview, ProductCreateAPIview, ProductListCreateAPIview, ProductRetrieveUpdateDestroyAPIview, TestCRUDView
)
# use 'test', do not use 'test/' it call request 2 time
urlpatterns = [
    path('django_api/', test_api),
    path('get_random_product/', get_product_model),
    path('get_by_drf_api/', drf_api_view),
    path('product/<int:pk>/', ProductDetailAPIview.as_view()),  # pk is set in ProductDetailAPIvie w.lookup_field, we use pk
    path('product/create/', ProductCreateAPIview.as_view()),
    path('product/getList_create/', ProductListCreateAPIview.as_view()),
    path('product/getSingel_update_delete/<int:id>', ProductRetrieveUpdateDestroyAPIview.as_view()),
    path('test_crud_view/', TestCRUDView.as_view()),
    path('test_crud_view/<int:id>', TestCRUDView.as_view()),
    # ProductListCreateAPIview.as_view()
]
