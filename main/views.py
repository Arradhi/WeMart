from django.shortcuts import render

def show_main(request):
    context = {
        'name' : 'Mentega Wisjman 1kg',
        'price': '450.000',
        'description': 'mentega premium untuk masakan anda',
        'image': 'https://i.imgur.com/cLr9moz.jpeg'
    }

    return render(request, "main.html", context)

# Create your views here.
