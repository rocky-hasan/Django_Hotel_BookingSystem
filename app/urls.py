
from django.urls import path
from . import views

urlpatterns = [
    path('', views.hotel, name='hotel' ),
    path('hotel-detail/<uid>/' , views.hotel_detail , name="hotel_detail"),
]
