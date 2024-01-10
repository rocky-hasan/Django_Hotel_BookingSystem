from django.shortcuts import render,redirect
from .models import (Amenities,Hotel)
from django.db.models import Q


# Create your views here.
def hotel(request):
    amenities_objs=Amenities.objects.all()
    hotels_objs=Hotel.objects.all()
    context={
        'amenities_objs':amenities_objs,
        'hotels_objs':hotels_objs
    }
    return render(request, 'hotel.html',context)