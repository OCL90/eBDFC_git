# Generated by Django 3.2.7 on 2022-06-25 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0041_alter_pad_working_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='sandtype',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]
