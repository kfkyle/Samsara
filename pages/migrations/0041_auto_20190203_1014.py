# Generated by Django 2.1.5 on 2019-02-03 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0040_auto_20190203_0932'),
    ]

    operations = [
        migrations.AddField(
            model_name='career',
            name='tag_line',
            field=models.CharField(max_length=80, null=True),
        ),
        migrations.AddField(
            model_name='main',
            name='tag_line',
            field=models.CharField(max_length=80, null=True),
        ),
        migrations.AddField(
            model_name='service',
            name='tag_line',
            field=models.CharField(max_length=80, null=True),
        ),
    ]
