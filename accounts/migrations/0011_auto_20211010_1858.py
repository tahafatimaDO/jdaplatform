# Generated by Django 3.1.6 on 2021-10-10 22:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_auto_20211010_1851'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='logo',
            field=models.ImageField(default='default.jpg', upload_to='profile_logo'),
        ),
    ]
