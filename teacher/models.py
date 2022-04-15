from django.db import models


# from user.models import Account


# Create your models here.
# 学院
class College(models.Model):
    name = models.CharField(default="",verbose_name="学院名", max_length=50)
    detail = models.TextField(default="", verbose_name="学院简介")

    def __str__(self):
        return self.name


# 系别
class Department(models.Model):
    name = models.CharField(default="", max_length=50, verbose_name="系名")
    detail = models.TextField(default="", verbose_name="系简介")

    def __str__(self):
        return self.name


# 专业
class Profession(models.Model):
    name = models.CharField(default="", max_length=50, verbose_name="专业名称")
    detail = models.TextField(default="", verbose_name="专业简介")

    def __str__(self):
        return self.name


# 教师信息
class Teacher(models.Model):
    SEX = (('男', '男'), ('女', '女'))
    name = models.CharField(default="", max_length=50, verbose_name="姓名")
    teacher_account = models.ForeignKey("account.Account", null=True, on_delete=models.CASCADE, verbose_name="工号")
    sex = models.CharField(default="男", max_length=1, choices=SEX, verbose_name="性别")
    tell = models.CharField(default="", max_length=12, verbose_name="电话")
    address = models.CharField(default="", max_length=250, verbose_name="所在地")
    college = models.ForeignKey(College, null=True, on_delete=models.CASCADE, verbose_name="所在学院")
    department = models.ForeignKey(Department, null=True, on_delete=models.CASCADE, verbose_name="所在系")
    profession = models.ForeignKey(Profession, null=True, on_delete=models.CASCADE, verbose_name="所在专业")

    def __str__(self):
        return self.name


# 课程信息
class Course(models.Model):
    teacher_account = models.ForeignKey("account.Account", null=True, on_delete=models.CASCADE)
    year = models.CharField(default="", max_length=20)
    semester = models.CharField(default="", max_length=20)
    week = models.CharField(default="", max_length=20)
    day = models.CharField(default="", max_length=20)
    time = models.CharField(default="", max_length=20)
    course_name = models.CharField(default="", max_length=250)

    def __str__(self):
        return str(self.teacher_account) + self.course_name
