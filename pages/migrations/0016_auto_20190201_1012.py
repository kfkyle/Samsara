# Generated by Django 2.1.5 on 2019-02-01 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0015_auto_20190201_1009'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='sub_header_2',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='service',
            name='sub_header_3',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
