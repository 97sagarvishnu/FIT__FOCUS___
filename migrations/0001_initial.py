# Generated by Django 5.0.1 on 2024-01-20 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Trainers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trainer_name', models.CharField(max_length=255)),
                ('trainer_dept', models.CharField(max_length=255)),
                ('trainer_image', models.ImageField(upload_to='trainers')),
            ],
        ),
    ]