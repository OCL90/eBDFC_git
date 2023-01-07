# Generated by Django 3.2.7 on 2022-01-07 06:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0027_auto_20220107_0641'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sand_Map',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('stage_number', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='projects.stage')),
                ('well_name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='projects.well')),
            ],
        ),
    ]
