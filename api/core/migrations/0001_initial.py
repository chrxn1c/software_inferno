# Generated by Django 5.0.6 on 2024-05-24 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Software',
            fields=[
                ('name', models.CharField(max_length=100, primary_key=True, serialize=False, unique=True)),
                ('version', models.CharField(max_length=10)),
                ('description', models.TextField()),
                ('license_number', models.CharField(max_length=30)),
                ('developer_company', models.CharField(max_length=30)),
            ],
        ),
    ]
