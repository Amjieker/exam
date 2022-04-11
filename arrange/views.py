import datetime
import time
import algorithm.oper_func
import algorithm.const_data
from algorithm import arrange
from django.shortcuts import render
from . import models
import account.models
from Tools import *
from Tools.Connect import *


# Create your views here.


def getMessage(request):
    if request.method == 'POST':
        resp = json.loads(request.body.decode())
        res = account \
            .models \
            .Account \
            .objects \
            .all() \
            .filter(wx_uid=resp['wx_uid'])
        acc = list(res)[0].account
        res = models \
            .Exam \
            .objects \
            .all() \
            .filter(arrange__teacher_account=acc)
        # print(res)
        return_res = []
        for loop in res:
            rang = loop.arrange_set.all()
            for i in rang:
                return_res.append(
                    {
                        "id": i.id,
                        "exam_name": loop.course,
                        "exam_detail": loop.detail,
                        "exam_date": loop.date.__str__(),
                        "exam_length": loop.time_length.__str__(),
                        "exam_person": loop.person.__str__(),
                        "invigilate_state": i.invigilate_state.__str__(),
                        "exam_address": loop.address,
                        "showItem": False
                    }
                )

        return_res.sort(key=lambda x: x['exam_date'], reverse=True)
        return_res.sort(key=lambda x: x['invigilate_state'])
        # print(return_res)
        return to_json(return_res)
    else:
        return to_html("hello")


def confirmArrange(request):
    if request.method == 'POST':
        resp = json.loads(request.body.decode())
        res = models \
            .Arrange \
            .objects \
            .all() \
            .filter(id=resp['id'])
        try:
            print(res)
            res.update(invigilate_state=1)
            return to_json({"code": True})
        except Exception as e:
            print(e)
            return to_json({"code": False})
    else:
        return to_html("hello")


def refuseArrange(request):
    if request.method == 'POST':
        resp = json.loads(request.body.decode())
        res = models \
            .Arrange \
            .objects \
            .all() \
            .filter(id=resp['id'])
        try:
            # print(res)
            res.update(invigilate_state=2)
            arr = list(res)[0]
            now_exam = list(models.Exam.objects.filter(id=arr.exam_id_id))[0]
            ans, err = arrange.arrange(
                exam_count=1,
                exam_date=now_exam.date.__str__(),
                exam_len=float(now_exam.time_length)
            )
            if ans is None:
                return to_json({"code": False})
            else:
                for loop in ans:
                    arr = models.Arrange(
                        teacher_account_id=int(loop),
                        invigilate_state=0,
                        add_date=now_exam.date,
                        exam_id_id=now_exam.id
                    )
                    arr.save(force_insert=True)
                    acc = account.models.Account.objects.all().filter(
                        account=int(loop)
                    )
                    temp = list(acc)[0]
                    if len(acc) != 0:
                        send_message(query_token(),
                                     temp.wx_uid,
                                     create_template(
                                         "老师 你好! 小程序有新的监考消息",
                                         algorithm.oper_func.transfer_date(to_time(resp['datatime'])).__str__()
                                         ,
                                         resp['course'])
                                     )
                    return to_json({"code": True})

            return to_json({"code": True})
        except Exception as e:
            print(e)
            return to_json({"code": False})
    else:
        return to_html("hello")


def arrangeExam(request):
    if request.method == 'POST':
        resp = json.loads(request.body.decode())
        print(resp)
        print(to_time(resp['datatime']))
        a, b = algorithm.oper_func.split_num(resp['semesters'])[0]
        algorithm.const_data.year = a
        algorithm.const_data.semester = b
        # print(a)
        ans, err = \
            arrange.arrange(
                exam_count=resp['teacher_count'],
                exam_date=to_time(int(resp['datatime'])),
                exam_len=resp['time_length']
            )
        print(err)
        if ans is None:
            return to_json({"code": False})
        try:
            exam = models.Exam(
                course=resp['course'],
                detail=resp['detail'],
                address=resp['address'],
                date=to_time(resp['datatime']),
                time_length=resp['time_length'],
                person=resp['person'],
                semesters=resp['semesters'],
                collage_id=resp['college']
            )
            print(exam.date)
            exam.save(force_insert=True)
            print(ans)
            for loop in ans:
                arr = models.Arrange(
                    teacher_account_id=int(loop),
                    invigilate_state=0,
                    add_date=to_time(resp['datatime']),
                    exam_id_id=exam.id
                )
                arr.save(force_insert=True)
                acc = account.models.Account.objects.all().filter(
                    account=int(loop)
                )
                temp = list(acc)[0]
                if len(acc) != 0:
                    send_message(query_token(),
                                 temp.wx_uid,
                                 create_template(
                                     "老师 你好! 小程序有新的监考消息",
                                     to_time(resp['datatime'])
                                     ,
                                     resp['course'])
                                 )
            return to_json({"code": True})
        except Exception as e:
            print(e)
        return to_json({"code": False})
    else:
        return to_html("hello")
