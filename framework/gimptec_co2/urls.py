from django.conf.urls import url
from .views import co2


urlpatterns = [
    url(r'CO2', co2),
]
