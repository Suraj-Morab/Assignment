from django.urls import path
from CartApp.views import CartAPIView, CartDetailAPIView

urlpatterns = [
    path("", CartAPIView.as_view(), name="cart-list"),
    path("detail/<int:id>", CartDetailAPIView.as_view(), name="cart-detail"),
]
