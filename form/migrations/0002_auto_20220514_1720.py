# Generated by Django 3.1.7 on 2022-05-14 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='age',
            field=models.CharField(max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='phone',
            field=models.CharField(max_length=10, null=True),
        ),
    ]