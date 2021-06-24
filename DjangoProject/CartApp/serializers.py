from rest_framework.serializers import ModelSerializer
from CartApp.models import Brand, Category, Cart


class BrandSerializer(ModelSerializer):
    class Meta:
        model = Brand
        fields = (
            "BrandName",
            "Description",
        )


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = (
            "CategoryName",
            "Description",
        )


class CartSerializer(ModelSerializer):
    class Meta:
        model = Cart
        fields = (
            "CartName",
            "Description",
        )
