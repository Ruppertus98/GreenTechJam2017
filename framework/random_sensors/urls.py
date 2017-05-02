from django.conf.urls import url
from .views import temperature, humidity


urlpatterns = [
    url(r'humidity', humidity),
    url(r'temperature', temperature),
]
