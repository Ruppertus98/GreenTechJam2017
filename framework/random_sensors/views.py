
from django.http import JsonResponse
from datetime import datetime
import random

temperature_value = 20
humidity_value = 50


def temperature(request):
    global temperature_value
    temperature_value = temperature_value + random.normalvariate(0, 1)
    return JsonResponse({'value': temperature_value, 'time': datetime.utcnow().isoformat()})


def humidity(request):
    global humidity_value
    humidity_value = humidity_value + random.normalvariate(0, 1)
    return JsonResponse({'value': humidity_value, 'time': datetime.utcnow().isoformat()})
