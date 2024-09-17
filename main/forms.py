from django.forms import ModelForm
from main.models import Products

class productForm(ModelForm):
    class Meta:
        model = Products
        fields = ["name", "description", "price", "image"]