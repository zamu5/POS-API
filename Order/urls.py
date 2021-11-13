from django.urls import path
from .views import CreateOrder, order_detail, order_list

urlpatterns = [
    path('create/', CreateOrder.as_view()),
    path('detail/<str:pk>/', order_detail),
    path('', order_list)
]