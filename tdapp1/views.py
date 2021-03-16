from django.shortcuts import render
from time import localtime, strftime

# Create your views here.
def root(request):
    context = {
        "date" : strftime("%b %d, %Y"),
        "time" : strftime("%I:%M %p")
    }
    return render(request,'base.html',context )
