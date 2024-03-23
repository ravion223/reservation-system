from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from hotel.models import *
from django.utils import timezone
import datetime
from calendar import monthrange

# Create your views here.

def get_rooms_list(request):
    rooms = Room.objects.all()

    context = {
        "rooms": rooms
    }

    return render(
        request,
        "hotel/rooms_list.html",
        context,
    )


def get_users_list(request):
    users = User.objects.all()

    context = {
        "users": users
    }

    return render(
        request,
        "hotel/users_list.html",
        context,
    )


def get_room_detail(request, pk: int):
    room = get_object_or_404(Room, pk=pk)
    today = timezone.now()
    first_day_of_month = datetime.date(today.year, today.month, 1)
    last_day_of_month = datetime.date(today.year, today.month, monthrange(today.year, today.month)[1])
    bookings = Booking.objects.filter(room=room, start_time__range=(first_day_of_month, last_day_of_month))
    booked_days = []
    for booking in bookings:
        for i in range(booking.start_time.day, booking.end_time.day + 1):
            booked_days.append(i)
    days_of_month = range(1, monthrange(today.year, today.month)[1] + 1)

    context = {
            'room': room,
            'days_of_month': days_of_month,
            'booked_days': booked_days,
            'today': today,
    }

    return render(
        request,
        "hotel/room_detail.html",
        context
    )


def booking_form(request):
    if request.method == "GET":
        return render(request, "hotel/booking_form.html")
    else:
        room_number = request.POST.get("room_number")
        start_time = request.POST.get("start_time")
        end_time = request.POST.get("end_time")

        try:
            room = Room.objects.get(number=room_number)

        except ValueError:
            return HttpResponse("Wrong room number", status=404)
        
        except Room.DoesNotExist:
            return HttpResponse("Room does not exist", status=404)
        
        booking = Booking.objects.create(
            room = room,
            user = request.user,
            start_time =  start_time,
            end_time = end_time
        )

        return redirect("booking_detail", pk = booking.id)


def get_booking_detail(request, pk: int):
    booking = Booking.objects.get(id = pk)

    context = {
        "booking": booking
    }

    return render(
        request,
        "hotel/booking_detail.html",
        context
    )


