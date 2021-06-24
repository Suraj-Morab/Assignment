from django.db import models

# Create your models here.
class Brand(models.Model):
    BrandID = models.IntegerField(primary_key=True)
    BrandName = models.CharField(max_length=40)
    Description = models.TextField()

    class Meta:
        managed = True
        db_table = "Brand"

    def __str__(self):
        return self.BrandName


class Category(models.Model):
    CategoryID = models.IntegerField(primary_key=True)
    CategoryName = models.CharField(max_length=20)
    Description = models.TextField()

    class Meta:
        managed = True
        db_table = "Category"

    def __str__(self):
        return self.CategoryName


class Cart(models.Model):
    CartName = models.CharField(max_length=40, blank=True)
    Brand = models.ForeignKey(Brand, related_name="Brand", on_delete=models.CASCADE)
    Category = models.ForeignKey(
        Category, related_name="Category", on_delete=models.CASCADE
    )
    Description = models.TextField()

    class Meta:
        managed = True
        db_table = "Cart"

    def __str__(self):
        return self.CartName

    _is_from_custom_logic = False

    @classmethod
    def Cart_Based_Distrubusion(cls, Brand=None, Category=None):

        cls._is_from_custom_logic = True
        if Brand:
            _new = cls.objects.create(Brand=Brand)
        elif Category:
            _new = cls.objects.create(Category=Category)
        else:
            raise ValueError(" ")
        return _new

    def save(self, *args, **kwargs):
        if not self._is_from_custom_logic:
            raise Exception(" ")
        return super().save(*args, **kwargs)
