# Generated by Django 3.2 on 2021-04-23 07:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Id_M', models.IntegerField()),
                ('Title', models.CharField(max_length=30)),
                ('Date', models.DateField()),
                ('Lists', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=30)),
                ('Date', models.DateField()),
                ('TextBox', models.TextField()),
                ('Wirter', models.CharField(max_length=30)),
                ('Id_M', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category', to='community.category')),
            ],
        ),
    ]
