from ProductApp.models import Product
from rest_framework import permissions
from ProductApp.serializers import ProductSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class ProductAPIView(ListCreateAPIView):
    serializer_class = ProductSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)

    def get_queryset(self):
        return Product.objects.filter(owner=self.request.user)


class ProductDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = ProductSerializer
    permission_classes = (IsAuthenticated,)
    lookup_field = "id"

    def get_queryset(self):
        return Product.objects.filter(owner=self.request.user)
