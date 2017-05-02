from django.conf.urls import url
from django.http import JsonResponse

window_open = False


def window(request):
    global window_open
    if request.POST:
        newstate = request.POST['open']
        window_open = bool(newstate)
    return JsonResponse({'open': window_open})


urlpatterns = [
    url(r'window', window),
]
