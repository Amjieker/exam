# Generated by Django 2.2.5 on 2022-03-17 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='nick',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='account',
            name='password',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='account',
            name='wx_uid',
            field=models.CharField(default='', max_length=250),
        ),
    ]
