import json
import time
from datetime import datetime
from django.http import HttpResponse


def to_json(arg):
    return HttpResponse(
        json.dumps(arg),
        'application/json'
    )


def to_html(arg):
    return HttpResponse(arg)


def to_time(st):
    timeArray = time.localtime(st // 1000)
    otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray).__str__()
    # print(otherStyleTime)
    return otherStyleTime

