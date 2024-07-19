# Generated by Django 5.0.6 on 2024-07-15 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='education_en',
            field=models.CharField(max_length=26, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='doctor',
            name='education_ru',
            field=models.CharField(max_length=26, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='doctor',
            name='specialty_en',
            field=models.CharField(max_length=50, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='doctor',
            name='specialty_ru',
            field=models.CharField(max_length=50, null=True, unique=True),
        ),
    ]