# Generated by Django 2.1.5 on 2019-02-03 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0035_auto_20190203_0617'),
    ]

    operations = [
        migrations.AddField(
            model_name='career',
            name='title',
            field=models.CharField(max_length=80, null=True),
        ),
    ]