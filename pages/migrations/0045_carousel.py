# Generated by Django 2.1.5 on 2019-02-04 04:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0044_auto_20190203_1019'),
    ]

    operations = [
        migrations.CreateModel(
            name='Carousel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('section', models.CharField(default='Carousel', editable=False, max_length=80)),
                ('header_1', models.CharField(max_length=80, null=True)),
                ('img_1', models.ImageField(upload_to='photos/%Y/%m/%d')),
                ('header_2', models.CharField(max_length=80, null=True)),
                ('img_2', models.ImageField(upload_to='photos/%Y/%m/%d')),
                ('header_3', models.CharField(max_length=80, null=True)),
                ('img_3', models.ImageField(upload_to='photos/%Y/%m/%d')),
            ],
        ),
    ]