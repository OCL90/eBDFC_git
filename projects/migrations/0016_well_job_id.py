# Generated by Django 3.2.7 on 2021-12-09 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0015_well_crew_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='well',
            name='job_id',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
