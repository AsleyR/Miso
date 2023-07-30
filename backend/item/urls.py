from django.urls import path
from . import views

app_name = "item"

urlpatterns = [
    path('all/', views.get_all_items),
    path('name/<str:pk>/', views.get_item_by_name),
    path('price/<str:pk>/', views.get_item_by_price),
    path('sold/<str:pk>/', views.get_item_by_sold_status),
    path('add/', views.add_item),
    path('update/<str:pk>', views.update_item),
    path('delete/<str:pk>', views.delete_item),
]
