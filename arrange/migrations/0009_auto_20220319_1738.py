# Generated by Django 2.2.5 on 2022-03-19 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('arrange', '0008_auto_20220319_1647'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exam',
            name='date',
            field=models.DateTimeField(auto_now=True, max_length=0),
        ),
    ]