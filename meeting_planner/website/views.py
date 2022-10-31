from datetime import datetime

from django.shortcuts import render
from django.http import HttpResponse
from meetings.models import Meetings, Room


def welcome(request):
    return render(request, "website/welcome.html", {"meetings": Meetings.objects.all(), "Room": Room.objects.all()})


def date(request):
    return HttpResponse("This page was served at: " + str(datetime.now()))


def about(request):
    return HttpResponse("Nothing about this web app here, go back to <a href = '/'>home page</a>.")
