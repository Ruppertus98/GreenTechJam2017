
from django.http import JsonResponse
from datetime import datetime
import random
import math

temperature_value = 20
humidity_value = 50


def temperature(request):
    global temperature_value
    temperature_value = temperature_value + random.triangular(-1, 1)
    temperature_value = min(max(temperature_value, 0), 35)
    return JsonResponse({'value': math.floor(temperature_value), 'time': datetime.now().isoformat()})


def humidity(request):
    global humidity_value
    humidity_value = humidity_value + random.triangular(-1, 1)
    humidity_value = min(max(humidity_value, 20), 90)
    return JsonResponse({'value': math.floor(humidity_value), 'time': datetime.now().isoformat()})
