from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Room(models.Model):
    number = models.CharField(max_length = 63)
    capacity = models.IntegerField()
    location = models.TextField()
    description = models.TextField()

    def __str__(self):
        return f"Room - {self.number}"
    
    class Meta:
        verbose_name = "Room"
        verbose_name_plural = "Rooms"
        ordering = ["number"]


class Booking(models.Model):
    room = models.ForeignKey(Room, on_delete = models.CASCADE, related_name = "bookings")
    user = models.ForeignKey(User, on_delete = models.CASCADE, related_name = "bookings")

    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return f"{self.room} booked - by {self.user}"
    
    class Meta:
        verbose_name = "Booking"
        verbose_name_plural = "Bookings"
        ordering = ["-end_time", "room"]
    
