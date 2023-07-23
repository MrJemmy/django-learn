from django.urls import path

from .views import (
    recipe_list_view, recipe_detail_view, recipe_create_view, recipe_update_view, recipe_delete_view, recipe_ingredient_delete_view
)

app_name = 'recipes'
urlpatterns = [
    path('', recipe_list_view, name='list'),
    path('create/', recipe_create_view, name='create'),
    path('<int:id>/', recipe_detail_view, name='detail'),
    path('update/<int:id>/', recipe_update_view, name='update'),
    path('delete/<int:id>/', recipe_delete_view, name='delete'),
    path('delete/<int:parent_id>/<int:id>', recipe_ingredient_delete_view, name='ingredient-delete'),
]