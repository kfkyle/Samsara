# Generated by Django 2.1.5 on 2019-02-03 06:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0034_auto_20190203_0608'),
    ]

    operations = [
        migrations.RenameField(
            model_name='career',
            old_name='title',
            new_name='section',
        ),
    ]
