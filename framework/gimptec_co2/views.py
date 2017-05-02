
import requests
import re
from django.http import HttpResponse, JsonResponse
import random
from _datetime import datetime


def co2(request):
    resp = requests.get("http://corina.gimptec.at/index.php?DeviceID=13966733")

    m = re.search("\['Co2 \[PPM\]', ([0-9]*)", resp.text)
    try:
        co2_val = int(m.group(1))
    except:
        co2_val = random.randint(500, 2000)

    return JsonResponse({'value': co2_val, 'time': datetime.utcnow().isoformat()})

