from django.db import models
from helpers.models import TrackingModel
from CartApp.models import Cart
from Authentication.models import User

# Create your models here.
class Product(TrackingModel):
    ProductID = models.IntegerField(primary_key=True)
    ProductName = models.CharField(max_length=40, blank=True)
    Cart = models.ForeignKey(to=Cart, on_delete=models.CASCADE)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    UnitPrice = models.DecimalField(max_digits=10, decimal_places=4)
    description = models.TextField()

    class Meta:
        managed = True
        db_table = "Products"

    def __str__(self):
        return self.ProductName
