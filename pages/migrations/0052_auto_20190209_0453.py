# Generated by Django 2.1.5 on 2019-02-09 04:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0051_auto_20190209_0451'),
    ]

    operations = [
        migrations.RenameField(
            model_name='apply',
            old_name='City',
            new_name='city',
        ),
    ]
