# Generated by Django 2.1.5 on 2019-02-01 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0012_remove_service_sub_header_1'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='sub_header_1',
            field=models.TextField(default='SOME STRING'),
        ),
    ]
