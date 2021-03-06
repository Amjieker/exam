# Generated by Django 2.2.5 on 2022-03-17 10:51

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('teacher', '0006_course'),
        ('account', '0002_auto_20220317_1637'),
    ]

    operations = [
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.CharField(default='', max_length=250)),
                ('detail', models.CharField(default='', max_length=250)),
                ('date', models.DateTimeField(default=datetime.datetime(2022, 3, 17, 18, 51, 24, 683903))),
                ('time_length', models.DecimalField(decimal_places=2, default=0.0, max_digits=20)),
                ('person', models.IntegerField(default=0)),
                ('semesters', models.CharField(default='', max_length=250)),
                ('collage', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='teacher.College')),
                ('teacher_account', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='account.Account')),
            ],
        ),
    ]
