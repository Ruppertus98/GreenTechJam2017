from django.conf.urls import url
from django.http import JsonResponse

window_open = False


def window(request):
    global window_open
    if request.POST:
        newstate = request.POST['open']
        if newstate.lower() == "true":
            window_open = True
        else:
            window_open = False
    return JsonResponse({'open': window_open})


urlpatterns = [
    url(r'window', window),
]
