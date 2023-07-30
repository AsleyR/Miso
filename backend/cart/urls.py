from django.urls import path
from . import views

app_name = "cart"

urlpatterns = [
    path('all/', views.get_all_carts),
    path('name/<str:pk>/', views.get_cart_by_name),
    path('item/<str:pk>', views.get_cart_by_cart_items),
    path('user/<str:pk>', views.get_cart_by_username),
    path('create/<str:pk>', views.create_cart),
    path('update/<str:pk>', views.update_cart),
    path('delete/<str:pk>', views.delete_cart),
]
