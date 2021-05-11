# Generated by Django 3.2 on 2021-04-23 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyClass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_num', models.IntegerField()),
                ('Teacher', models.CharField(max_length=30)),
                ('class_room', models.CharField(max_length=30)),
                ('students_num', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='MyStudents',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('phone_num', models.CharField(max_length=30)),
                ('intro_text', models.TextField()),
            ],
        ),
    ]
