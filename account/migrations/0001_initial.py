# Generated by Django 2.2.5 on 2022-03-17 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('nick', models.CharField(max_length=20)),
                ('account', models.AutoField(primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=20)),
                ('wx_uid', models.CharField(max_length=250)),
            ],
        ),
    ]
