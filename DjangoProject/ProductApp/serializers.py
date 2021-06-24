from rest_framework.serializers import ModelSerializer
from ProductApp.models import Product


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = (
            "ProductName",
            "description",
            "UnitPrice",
        )
