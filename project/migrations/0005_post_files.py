# Generated by Django 2.2.3 on 2019-08-29 04:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0004_auto_20190828_1622'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='files',
            field=models.FileField(default='a.py', upload_to='', verbose_name='فایل ها'),
            preserve_default=False,
        ),
    ]