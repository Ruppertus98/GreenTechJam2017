from django.conf.urls import url
from .views import temperature, humidity, outside_temperature


urlpatterns = [
    url(r'humidity', humidity),
    url(r'outside_temperature', outside_temperature),
    url(r'temperature', temperature),

]
