# Generated by Django 2.1 on 2018-09-01 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('slider', '0002_remove_slide_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='slide',
            name='active',
            field=models.BooleanField(default=False, help_text='اسلاید فعال در ابتدا نمایش داده می شود', verbose_name='فعال'),
        ),
    ]
