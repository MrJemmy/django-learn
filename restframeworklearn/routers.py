from restframeworklearn.views.views5 import ProductModleViewSet, ProductReadOnlyModleViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('view_set', ProductModleViewSet, basename='full_crud')
router.register('view_set_read_only', ProductReadOnlyModleViewSet, basename='read_only')
# use 'test', do not use 'test/' it call request 2 time
# print('router urls')
# for url in router.urls:
#     print(url)