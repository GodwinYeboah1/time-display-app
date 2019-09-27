from django.shortcuts import render

from time import gmtime, strftime
from django.utils import timezone

# Create your views here.
def index(req):
    context = {
        "date": strftime("%b %d, %Y", gmtime()),
        "time": strftime("%I:%M %p")
    }
    return render(req, 'time_display/index.html', context)
    