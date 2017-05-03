
from django.http import JsonResponse
from datetime import datetime
import random
import math

temperature_value = 20
humidity_value = 50


def temperature(request):
    global temperature_value
    temperature_value = temperature_value + random.normalvariate(0, 1)
    temperature_value = math.floor(temperature_value)
    return JsonResponse({'value': temperature_value, 'time': datetime.now().isoformat()})


def humidity(request):
    global humidity_value
    humidity_value = humidity_value + random.normalvariate(0, 1)
    humidity_value = math.floor(humidity_value)
    return JsonResponse({'value': humidity_value, 'time': datetime.now().isoformat()})
