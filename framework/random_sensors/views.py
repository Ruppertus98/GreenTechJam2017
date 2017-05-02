
from django.http import JsonResponse
from datetime import datetime
import random

def temperature(request):
    temperature = random.randint(18, 35)
    return JsonResponse({'value': temperature, 'time': datetime.utcnow().timestamp()})


def humidity(request):
    humidity = random.randint(30, 100)
    return JsonResponse({'value': humidity, 'time': datetime.utcnow().timestamp()})
