import datetime

from django.db import models
from django.utils.html import format_html

# Create your models here.

class Exam(models.Model):
    course = models.CharField(default="", verbose_name="考试名称", max_length=250)
    detail = models.TextField(default="", verbose_name="考试信息")
    date = models.DateTimeField(verbose_name="考试时间")
    time_length = models.DecimalField(default=0.00, verbose_name="考试时长", max_digits=20, decimal_places=2)
    person = models.IntegerField(default=0, verbose_name="考试人数")
    semesters = models.CharField(default="", max_length=250, verbose_name="学期")
    collage = models.ForeignKey("teacher.College",null=True, on_delete=models.DO_NOTHING)
    address = models.CharField(default="", max_length=250)

    def __str__(self):
        return self.course


class Arrange(models.Model):
    STATE = ((0, "未确认"), (1, "已同意"), (2, "反对监考"))
    teacher_account = models.ForeignKey("account.Account",verbose_name="教师姓名", on_delete=models.NOT_PROVIDED)
    exam_id = models.ForeignKey(Exam, verbose_name="考试名称", on_delete=models.NOT_PROVIDED)
    invigilate_state = models.IntegerField(default=0, verbose_name="教师确认状态", choices=STATE)
    add_date = models.DateTimeField()
    def invigilate(self):
        code = "black"
        if self.invigilate_state == 1:
            code = "green"
        elif self.invigilate_state == 2:
            code = "red"
        return format_html(
            '<span style="color: {}">{}</span>',
            code,
            self.STATE[self.invigilate_state][-1]
        )
    invigilate.short_description = u"状态" 


class Message(models.Model):
    teacher_account = models.ForeignKey("account.Account", on_delete=models.NOT_PROVIDED)
    title = models.CharField(max_length=250)
    detail = models.TextField(max_length=25000)
    date = models.DateTimeField(auto_now=True)
