# Generated by Django 3.1.6 on 2021-04-26 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jdatester', '0005_indexpricemodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='indexpricemodel',
            name='index_date',
            field=models.DateTimeField(unique=True),
        ),
    ]
