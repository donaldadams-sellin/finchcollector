# Generated by Django 3.2.9 on 2022-01-11 03:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Finch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('color', models.CharField(max_length=25)),
                ('favorite_music', models.CharField(max_length=25)),
                ('age', models.IntegerField()),
            ],
        ),
    ]
