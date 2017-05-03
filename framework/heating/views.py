from django.conf.urls import url
from django.http import JsonResponse
heating_state = True


def heating(request):
    global heating_state
    if request.POST:
        newstate = request.POST['on']
        if newstate.lower() == "true":
            heating_state = True
        else:
            heating_state = False
    return JsonResponse({'on': heating_state})


urlpatterns = [
    url(r'heating', heating),
]

