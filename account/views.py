import json

from django.shortcuts import render
from Tools import *
from . import models
from sipder import login


# Create your views here.

def checkIs(request):
    if request.method == 'POST':
        wx_uid = json.loads(request.body.decode())['wx_uid']
        res = models.Account.objects.all().filter(wx_uid=wx_uid)
        if len(res) is 0:
            return to_json({'code': False})
        else:
            return to_json({'code': True})
    else:
        return to_html("hello")


def check_account(res):
    conn = login.Longin(
        user=res['account'],
        password=res['password'],
        login_url=login.login_url,
        login_KeyUrl=login.login_KeyUrl
    )
    try:
        rep = conn.Longin_Home()
        if rep is False:
            return False
        else:
            return True
    except Exception as e:
        print(e)
        try:
            rep = conn.Longin_Home()
            if rep is False:
                return False
            else:
                return True
        except Exception as e:
            print(e)
            return False
    return False


def save_account(request):
    if request.method == 'POST':
        resp = json.loads(request.body.decode())
        res = models.Account.objects.all().filter(wx_uid=resp['wx_uid'])
        t = check_account(resp)
        if t is False:
            return to_json({"code": False})
        if len(res) is 0:
            q = models.Account(
                account=int(resp['account']),
                password=resp['password'],
                nick=resp['name'],
                wx_uid=resp['wx_uid']
            )
            q.save(force_insert=True)
        else:
            res.update(account=resp['account'],
                       password=resp['password'],
                       nick=resp['name'])
        return to_json({"code": True})
    else:
        return to_html("hello")
