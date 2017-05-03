
from django.http import JsonResponse
from datetime import datetime
import random
import math

temperature_value = 25
outside_temperature_value = 10
humidity_value = 50

import window.views as winview


def temperature(request):
    global temperature_value
    global outside_temperature_value

    if request.POST:
        temperature_value = int(request.POST['value'])

    if winview.window_open:
        d = outside_temperature_value - temperature_value
        temperature_value = temperature_value + d*random.random()*0.5
    else:
        temperature_value = temperature_value + random.triangular(-1, 1.4)

    temperature_value = min(max(temperature_value, 15), 35)
    return JsonResponse({'value': math.floor(temperature_value), 'time': datetime.now().isoformat()})


def humidity(request):
    global humidity_value
    if request.POST:
        humidity_value = int(request.POST['value'])

    if winview.window_open:
        humidity_value = humidity_value + random.triangular(-1, 0)
    else:
        humidity_value = humidity_value + random.triangular(-1, 1)

    humidity_value = min(max(humidity_value, 20), 90)
    return JsonResponse({'value': math.floor(humidity_value), 'time': datetime.now().isoformat()})


def outside_temperature(request):
    global outside_temperature_value
    if request.POST:
        outside_temperature_value = int(request.POST['value'])
    outside_temperature_value = outside_temperature_value + random.triangular(-1, 1)
    outside_temperature_value = min(max(outside_temperature_value, -10), 45)
    return JsonResponse({'value': math.floor(outside_temperature_value), 'time': datetime.now().isoformat()})

