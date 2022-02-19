# Generated by Django 3.1.6 on 2022-02-19 20:23

from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('jdafinancialsapp', '0007_exchangemodel'),
        ('jdaanalyticsapp', '0010_auto_20220219_1521'),
    ]

    operations = [
        migrations.AddField(
            model_name='securitymodel',
            name='cntry',
            field=django_countries.fields.CountryField(blank=True, max_length=2, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='securitymodel',
            name='cntry_tax',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='securitymodel',
            name='currency',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='securitymodel',
            name='depsty',
            field=models.CharField(blank=True, choices=[('', 'Depository'), ('Bourse Regionale', 'Bourse Regionale')], max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='securitymodel',
            name='exchg',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='jdaanalyticsapp.exchangemodel'),
        ),
        migrations.AddField(
            model_name='securitymodel',
            name='exchg_tax',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='securitymodel',
            name='hghst_appl_rate',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='securitymodel',
            name='invstr_cntry_tax',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='securitymodel',
            name='issue',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='jdafinancialsapp.companymodel'),
        ),
        migrations.AddField(
            model_name='securitymodel',
            name='isur_type',
            field=models.CharField(blank=True, choices=[('', 'Issuer Type'), ('Private', 'Private'), ('Public', 'Public')], max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='securitymodel',
            name='listg_sts',
            field=models.CharField(blank=True, choices=[('', 'Listing Status'), ('Listed', 'Listed'), ('Unlisted', 'Unlisted'), ('Suspended', 'Suspended'), ('Deleted', 'Deleted')], max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='securitymodel',
            name='lwst_appl_rate',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='securitymodel',
            name='min_lot',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='securitymodel',
            name='nmnl_amt',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='securitymodel',
            name='rgstrr',
            field=models.CharField(blank=True, choices=[('', 'Registrar'), ('Central Bank', 'Central Bank')], max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='securitymodel',
            name='sector',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='jdafinancialsapp.sectormodel'),
        ),
        migrations.AddField(
            model_name='securitymodel',
            name='shr_class',
            field=models.CharField(blank=True, choices=[('', 'Share Class'), ('A', 'A'), ('B', 'B'), ('C', 'C')], max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='securitymodel',
            name='ttl_type',
            field=models.CharField(blank=True, choices=[('', 'Title Type'), ('Listed Share', 'Listed Share'), ('Listed Bond', 'Listed Bond'), ('Unlisted Share', 'Unlisted Share'), ('Unlisted Bond', 'Unlisted Bond')], max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='securitymodel',
            name='txtn_code',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='securitymodel',
            name='val_code',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]
