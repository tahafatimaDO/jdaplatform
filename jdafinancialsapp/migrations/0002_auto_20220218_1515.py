# Generated by Django 3.1.6 on 2022-02-18 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jdafinancialsapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='companymodel',
            name='id_cntry',
        ),
        migrations.AlterField(
            model_name='companymodel',
            name='company',
            field=models.CharField(max_length=300),
        ),
    ]
