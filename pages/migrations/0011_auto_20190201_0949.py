# Generated by Django 2.1.5 on 2019-02-01 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0010_auto_20190201_0944'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='sub_header_1',
            field=models.TextField(),
        ),
    ]