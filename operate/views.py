from django.shortcuts import render
from Tools import *


# Create your views here.

def index(request):
    if request.method == 'POST':
        # print(json.loads(request.body.decode()))
        return to_json(json.loads(request.body.decode()))
    else:
        if request.user.is_authenticated:
            return to_html(request.user.username)
        else:
            return to_html("hello")


def arrange(request):
    if request.method == 'POST':
        return to_json(json.loads(request.body.decode()))
    else:
        if request.user.is_authenticated:
            return render(request, "arrange_exam.html")
        else:
            return to_html("hello")

