# Generated by Django 3.2.7 on 2021-11-01 16:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0005_bol_destination_on'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bol',
            old_name='destination_on',
            new_name='arrived_time',
        ),
    ]
