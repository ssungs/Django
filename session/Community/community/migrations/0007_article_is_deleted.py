# Generated by Django 3.2.1 on 2021-05-04 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0006_rename_id_m_article_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
    ]
