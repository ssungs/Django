# Generated by Django 3.2 on 2021-04-30 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todolist',
            name='is_complete',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='todolist',
            name='is_delete',
            field=models.BooleanField(default=False),
        ),
    ]