# Generated by Django 2.1.5 on 2019-02-12 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0054_auto_20190212_0514'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='apply',
            name='sub_title',
        ),
        migrations.RemoveField(
            model_name='apply',
            name='title',
        ),
        migrations.AddField(
            model_name='jobad',
            name='sub_header_3',
            field=models.CharField(max_length=80, null=True),
        ),
        migrations.AddField(
            model_name='jobad',
            name='third_bullet_1',
            field=models.CharField(max_length=80, null=True),
        ),
        migrations.AddField(
            model_name='jobad',
            name='third_bullet_2',
            field=models.CharField(max_length=80, null=True),
        ),
        migrations.AddField(
            model_name='jobad',
            name='third_bullet_3',
            field=models.CharField(max_length=80, null=True),
        ),
    ]
