from django.shortcuts import render, get_object_or_404

from .models import Meetings, Room


# Create your views here.
def detail(request, id):
    meeting = get_object_or_404(Meetings, pk=id)
    return render(request, "meetings/detail.html", {"meeting": meeting})


def room(request, id):
    rooms = get_object_or_404(Room, pk=id)
    return render(request, "meetings/rooms.html", {"Room": rooms})
