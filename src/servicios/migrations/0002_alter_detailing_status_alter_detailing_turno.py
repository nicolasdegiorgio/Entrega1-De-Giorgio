# Generated by Django 4.0.6 on 2022-08-08 23:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servicios', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detailing',
            name='status',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='detailing',
            name='turno',
            field=models.CharField(max_length=30),
        ),
    ]
