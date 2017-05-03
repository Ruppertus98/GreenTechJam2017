from django.conf.urls import url
from django.shortcuts import render



def flatgui(request):
    return render(request, "flatgui.html", {})


urlpatterns = [
    url(r'flatgui', flatgui),
]
