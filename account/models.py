from django.db import models


# from teacher.models import Teacher


# Create your models here.
# 教师账号
class Account(models.Model):
    nick = models.CharField(default="", verbose_name="教师姓名", max_length=20)
    account = models.BigIntegerField(primary_key=True, verbose_name="教师账号")
    password = models.CharField(default="", max_length=20)
    wx_uid = models.CharField(default="", unique=True, max_length=250)

    def __str__(self):
        return self.nick
