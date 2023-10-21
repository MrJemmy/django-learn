from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.
class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, default=1)  # default=1 very 1st user
    title = models.CharField(max_length=160)
    content = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=15, decimal_places=2, default=99.99)

    @property
    def sale_price(self):
        return '%.2f' %(float(self.price) * 0.1)