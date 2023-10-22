from django.urls import path
from .views import ProductList, ProductDetail

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
   openapi.Info(
      title="Product API",
      default_version='v1',
      description="CRUD API for products of an E-Commerce shopping website.",
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)


#Endpoints
# /products/
# /products/<pk>

urlpatterns = [
    path("products/", ProductList.as_view()),
    path("products/<int:pk>/", ProductDetail.as_view()),
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
