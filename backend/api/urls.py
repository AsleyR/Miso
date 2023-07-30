from django.urls import path, include
from . import views

app_name = "api"

urlpatterns = [
    path('item/', include('item.urls')),
    path("category/", include('category.urls')),
    path('cart/', include('cart.urls')),
]
