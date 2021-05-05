# Generated by Django 3.1.6 on 2021-04-27 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jdatester', '0013_securitypricemodel_open'),
    ]

    operations = [
        migrations.AddField(
            model_name='securitypricemodel',
            name='close',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='securitypricemodel',
            name='high',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='securitypricemodel',
            name='low',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
    ]
