# Generated by Django 2.1.5 on 2019-02-01 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0006_auto_20190201_0918'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='sub_header_1',
            field=models.TextField(default=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='service',
            name='sub_header_2',
            field=models.TextField(default=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='service',
            name='sub_header_3',
            field=models.TextField(default=None),
            preserve_default=False,
        ),
    ]
