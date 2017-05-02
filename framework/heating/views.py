from django.conf.urls import url
from django.http import JsonResponse
heating_state = True


def heating(request):
    global heating_state
    newstate = request.POST['on']
    heating_state = newstate
    return JsonResponse({'on': heating_state})


urlpatterns = [
    url(r'heating', heating),
]

