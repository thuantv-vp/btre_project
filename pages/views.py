from django.shortcuts import render
from django.http import HttpResponse
from listings.models import Listing
from realtors.models import Realtor
from listings.choice import price_choices, bedroom_choices, state_choices
# Create your views here.
# def index(request):
#     return HttpResponse('<h1>Hello world</h1>')
def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]
    context = {
        'listings':listings,
        'state_choices': state_choices,
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices,
    }
    return render   (request,'pages/index.html',context)

def about(request):
    return render   (request,'pages/about.html')

def home(request):
    return render(request, 'home.html')