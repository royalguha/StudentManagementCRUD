# Generated by Django 2.1 on 2020-05-26 03:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StudData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('roll', models.IntegerField()),
                ('name', models.CharField(max_length=100)),
                ('phone', models.IntegerField()),
                ('address', models.TextField()),
            ],
        ),
    ]
