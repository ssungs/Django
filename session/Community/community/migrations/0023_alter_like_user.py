# Generated by Django 3.2.1 on 2021-05-14 05:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0022_auto_20210514_0502'),
    ]

    operations = [
        migrations.AlterField(
            model_name='like',
            name='user',
            field=models.ManyToManyField(related_name='like', to='community.UserPro'),
        ),
    ]
