from django.shortcuts import render,redirect
from .models import (Amenities,Hotel)
from django.db.models import Q


# Create your views here.
def hotel(request):
    amenities_objs=Amenities.objects.all()
    hotels_objs=Hotel.objects.all()
    sort_by=request.GET.get('sort_by')
    search=request.GET.get('search')

    if sort_by:
        sort_by=request.GET.get('sort_by')
        if sort_by =='ASC':
            hotels_objs=hotels_objs.order_by('hotel_price')
        elif sort_by =='DSC':
            hotels_objs=hotels_objs.order_by('-hotel_price')
    if search:
        hotels_objs=hotels_objs.filter(
            Q(hotel_name__icontains=search) |  Q(description__icontains=search))


    context={
        'amenities_objs':amenities_objs,
        'hotels_objs':hotels_objs,
        'sort_by':sort_by,
        'search':search,
    }
    return render(request, 'hotel.html',context)