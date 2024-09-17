from django.db import models
from django.db import models
import uuid 

# Create your models here.

class Products(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.IntegerField()
    image = models.ImageField()

# class productRating(models.Model):
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)  # tambahkan baris ini
#     nama_pemesan = models.CharField(max_length=255)
#     time = models.DateField(auto_now_add=True)
#     komentar = models.TextField()
#     rating = models.IntegerField(min=1, max=5)
