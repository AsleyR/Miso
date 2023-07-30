from django.urls import path
from . import views

app_name = "category"

urlpatterns = [
    path('all/', views.get_all_categories),
    path('name/<str:pk>/', views.get_category_by_name),
    path('create/', views.create_category),
    path('update/<str:pk>/', views.update_category),
    path('delete/<str:pk>/', views.delete_category)
]
