import json

from django.shortcuts import render
from django.http import Http404
from Tools import *
from sipder import login
from . import models
import account.models


# Create your views here.

def get_College(request):
    if request.method == 'POST':
        query_res = models.College.objects.all().values('id', 'name')
        return_res = []
        for loop in query_res:
            return_res.append(loop)
        return to_json(return_res)
    else:
        raise Http404("not found")


def update(request):
    if request.method == 'POST':
        try:

            resp = json.loads(request.body.decode())
            res = account.models \
                .Account \
                .objects \
                .all() \
                .filter(wx_uid=resp['wx_uid'],
                        account=resp['account']
                        )
            if len(res) is 0:
                return to_json({"code": False})
            try:
                res = models \
                    .Teacher \
                    .objects \
                    .all() \
                    .filter(teacher_account_id=resp['account'])
                if len(res) is 0:
                    q = models.Teacher(
                        teacher_account_id=int(resp['account']),
                        name=resp['name'],
                        tell=resp['tell'],
                        address=resp['address']
                    )
                    q.save(force_insert=True)
                else:
                    res.update(
                        name=resp['name'],
                        tell=resp['tell'],
                        address=resp['address']
                    )
                return to_json({"code": True})
            except Exception as e:
                print(e)
                return to_json({"code": False})
        except Exception as e:
            print(e)
            return to_json({"code": False})
    else:
        return to_html("hello")


def test(request):
    if request.method == 'POST':
        resp = json.loads(request.body.decode())
        save_course_table(resp['account'], resp['password'], resp['year'], resp['semester'])
        return to_json({"code": True})
    else:
        return to_html("1")

def save_course_table(username, password, year, semester):
    conn = login.Longin(
        user=username,
        password=password,
        login_url=login.login_url,
        login_KeyUrl=login.login_KeyUrl
    )
    session = ""
    try:
        session = conn.Longin_Home()
    except Exception as e:
        print(e)
        try:
            session = conn.Longin_Home()
        except Exception as e:
            print(e)
    data = {"xnm": 2021, "xqm": 12, 'kzlx': 'ck'}
    table_info = session.post(login.table_url, data=data).json()
    for each in table_info["kbList"]:
        plt = r'{} | {:<8s} | {:<13s} | {:<15s} | {:<22s}'
        # print(plt.format(each["xqjmc"], each["jc"], each["cdmc"], each["zcd"], each["kcmc"]))
        p = models.Course(
            course_name=each["kcmc"],
            week=each["zcd"],
            teacher_account_id=int(username),
            year=year,
            semester=semester,
            day=each["xqjmc"],
            time=each["jc"]
        )
        p.save(force_insert=True)
