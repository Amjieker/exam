# Generated by Django 2.2.5 on 2022-03-19 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('arrange', '0006_auto_20220318_0956'),
    ]

    operations = [
        migrations.AddField(
            model_name='exam',
            name='address',
            field=models.CharField(default='', max_length=250),
        ),
    ]
