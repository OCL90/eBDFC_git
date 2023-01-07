# Generated by Django 3.2.7 on 2022-01-07 08:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0031_auto_20220107_0808'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sand_map',
            name='bol',
        ),
        migrations.AddField(
            model_name='sand_map',
            name='stage_number',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='projects.stage'),
        ),
        migrations.AddField(
            model_name='sand_map',
            name='well_name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='projects.well'),
        ),
    ]
