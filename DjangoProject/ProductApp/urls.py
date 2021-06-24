from django.urls import path
from ProductApp.views import ProductAPIView, ProductDetailAPIView

urlpatterns = [
    path("", ProductAPIView.as_view(), name="product-list"),
    path("detail/<int:id>", ProductDetailAPIView.as_view(), name="product-detail"),
]
