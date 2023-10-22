from django.urls import path
from .views import ProductList, ProductDetail


#Endpoints
# /products/
# /products/<pk>

urlpatterns = [
    path("products/", ProductList.as_view()),
    path("products/<int:pk>/", ProductDetail.as_view()),
]