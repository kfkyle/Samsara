# Generated by Django 2.1.5 on 2019-02-01 09:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_auto_20190201_0705'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aboutus',
            name='content',
        ),
        migrations.RemoveField(
            model_name='whyus',
            name='content',
        ),
    ]
