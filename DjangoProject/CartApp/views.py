from ProductApp.models import Cart
from rest_framework import permissions
from CartApp.serializers import CartSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class CartAPIView(ListCreateAPIView):
    serializer_class = CartSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)

    def get_queryset(self):
        return Cart.objects.filter(owner=self.request.user)


class CartDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = CartSerializer
    permission_classes = (IsAuthenticated,)
    lookup_field = "id"

    def get_queryset(self):
        return Cart.objects.filter(Brand=self.request.Brand)
