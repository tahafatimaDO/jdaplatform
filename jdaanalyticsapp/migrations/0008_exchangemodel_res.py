# Generated by Django 3.1.6 on 2022-02-19 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jdaanalyticsapp', '0007_auto_20220219_1456'),
    ]

    operations = [
        migrations.AddField(
            model_name='exchangemodel',
            name='res',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
