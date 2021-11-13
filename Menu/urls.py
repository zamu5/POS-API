from django.urls import path
from .views import item_list, item_detail, item_create, item_update, item_delete

urlpatterns = [
    path('', item_list),
    path('detail/<str:pk>/', item_detail),
    path('create/', item_create),
    path('update/<str:pk>/', item_update),
    path('delete/<str:pk>/', item_delete)
]