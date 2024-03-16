from django.urls import path
from .views import *

urlpatterns = [
    path('', get_rooms_list, name = "home"),
    path('users/', get_users_list, name = "users_list"),
    path('room/<int:pk>', get_room_detail, name = "get_room_detail"),
    path('booking/', booking_form, name = "booking_form"),
    path('booking_detail/<int:pk>', get_booking_detail, name = "booking_detail")
]