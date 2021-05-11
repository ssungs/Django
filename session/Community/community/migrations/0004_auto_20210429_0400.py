# Generated by Django 3.2 on 2021-04-29 04:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0003_rename_wirter_content_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('name', models.CharField(max_length=30)),
                ('content', models.TextField()),
                ('Id_M', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contents', to='community.category')),
            ],
        ),
        migrations.DeleteModel(
            name='Content',
        ),
    ]