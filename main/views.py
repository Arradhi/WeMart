from django.shortcuts import render,  redirect
from main.forms import productForm
from main.models import Products
from django.http import HttpResponse
from django.core import serializers
from xml.etree.ElementTree import Element, SubElement, tostring



def show_main(request):
    product_entries = Products.objects.all()
    
    context = {
        'name' : 'Mentega Wijsman 1kg',
        'price': 450000,
        'description': 'mentega premium untuk masakan anda',
        'image': 'https://i.imgur.com/cLr9moz.jpeg',
        "product_entries": product_entries
        
    }

    return render(request, "main.html", context)

def create_product_entry(request):
    form = productForm(request.POST, request.FILES or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_product_entry.html", context)


def show_xml(request):
    data = Products.objects.all()
    root = Element('items')
    item_element = SubElement(root, 'item')
    image_url = SubElement(item_element, 'image_url')
    image_url.text = request.build_absolute_uri(data.image.url)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
# Create your views here.

