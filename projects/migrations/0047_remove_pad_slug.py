# Generated by Django 3.2.7 on 2022-07-01 04:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0046_auto_20220701_0438'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pad',
            name='slug',
        ),
    ]
