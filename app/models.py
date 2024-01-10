from django.db import models
import uuid
from django.contrib.auth.models import User
# Create your models here.
class BaseModel(models.Model):
    uid=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    created_at=models.DateField(auto_now_add=True)
    updated_at=models.DateField(auto_now_add=True)

    class Meta:
        abstract=True

class Amenities(BaseModel):
    amenity_name=models.CharField(max_length=100)
    def __str__(self) -> str:
        return self.amenity_name



class Hotel(BaseModel):
    hotel_name=models.CharField(max_length=180)
    hotel_price=models.IntegerField()
    description=models.TextField()
    amenities=models.ManyToManyField(Amenities)
    room_count=models.IntegerField(default=10)

    def __str__(self) -> str:
        return self.hotel_name
    
class HotelImages(BaseModel):
    hotel=models.ForeignKey(Hotel,related_name='images', on_delete=models.CASCADE)
    images=models.ImageField(upload_to='hotel/')

class HotelBooking(BaseModel):
    hotel=models.ForeignKey(Hotel,related_name='hotel_booking', on_delete=models.CASCADE)
    user=models.ForeignKey(User,related_name='user_booking', on_delete=models.CASCADE)
    start_date=models.DateField()
    end_date=models.DateField()
    booking_type=models.CharField(choices=(('Pre Book','Pre Book'),('Post Book','Post Book')),max_length=180)

