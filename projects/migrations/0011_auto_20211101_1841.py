# Generated by Django 3.2.7 on 2021-11-01 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0010_bol_bol_comments'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bol',
            old_name='bol_comments',
            new_name='bol_comment_1',
        ),
        migrations.AddField(
            model_name='bol',
            name='bol_comment_2',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
