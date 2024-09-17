from django.shortcuts import render,  redirect
from main.forms import productForm
from main.models import Products
from django.http import HttpResponse
from django.core import serializers
from xml.etree.ElementTree import Element, SubElement, tostring
import json



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

def show_json(request):
    data = Products.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml(request):
    data = Products.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_xml_by_id(request, id):
    data = Products.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Products.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")