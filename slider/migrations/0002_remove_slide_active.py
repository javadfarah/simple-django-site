# Generated by Django 2.1 on 2018-09-01 08:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('slider', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='slide',
            name='active',
        ),
    ]
