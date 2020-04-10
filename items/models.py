from django.db import models
from categories.models import Category

categories = Category.objects.all().order_by("id")
all_categories = []

for category in categories:
    all_categories.append (
        (category.id, category.title)
    )

# Create your models here.
class Item(models.Model):
    category = models.IntegerField(choices=all_categories, blank=False)
    title = models.CharField(max_length=100, blank=False)
    description = models.TextField(blank=False)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=False)
    quantity = models.IntegerField(blank=False)
    sku = models.CharField(max_length=100, blank=False)
    picture = models.ImageField(default='default.jpg', blank=True)

    def __str__(self):
        return self.title