# Generated by Django 2.1.5 on 2019-02-03 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0032_auto_20190203_0529'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='img_text_2',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='service',
            name='content_1',
            field=models.CharField(max_length=400, null=True),
        ),
        migrations.AlterField(
            model_name='service',
            name='content_2',
            field=models.CharField(max_length=400, null=True),
        ),
        migrations.AlterField(
            model_name='service',
            name='content_3',
            field=models.CharField(max_length=400, null=True),
        ),
        migrations.AlterField(
            model_name='service',
            name='sub_title',
            field=models.CharField(max_length=400, null=True),
        ),
    ]