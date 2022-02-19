# Generated by Django 3.1.6 on 2022-02-19 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jdaanalyticsapp', '0002_auto_20220219_1017'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stockmodel',
            name='security',
        ),
        migrations.RemoveField(
            model_name='securitymodel',
            name='close_dt',
        ),
        migrations.RemoveField(
            model_name='securitymodel',
            name='cntry',
        ),
        migrations.RemoveField(
            model_name='securitymodel',
            name='cntry_tax',
        ),
        migrations.RemoveField(
            model_name='securitymodel',
            name='currency',
        ),
        migrations.RemoveField(
            model_name='securitymodel',
            name='depsty',
        ),
        migrations.RemoveField(
            model_name='securitymodel',
            name='desc',
        ),
        migrations.RemoveField(
            model_name='securitymodel',
            name='exchg',
        ),
        migrations.RemoveField(
            model_name='securitymodel',
            name='exchg_tax',
        ),
        migrations.RemoveField(
            model_name='securitymodel',
            name='hghst_appl_rate',
        ),
        migrations.RemoveField(
            model_name='securitymodel',
            name='instr_type',
        ),
        migrations.RemoveField(
            model_name='securitymodel',
            name='invstr_cntry_tax',
        ),
        migrations.RemoveField(
            model_name='securitymodel',
            name='issue',
        ),
        migrations.RemoveField(
            model_name='securitymodel',
            name='isu_dt',
        ),
        migrations.RemoveField(
            model_name='securitymodel',
            name='isur_type',
        ),
        migrations.RemoveField(
            model_name='securitymodel',
            name='listg_sts',
        ),
        migrations.RemoveField(
            model_name='securitymodel',
            name='lwst_appl_rate',
        ),
        migrations.RemoveField(
            model_name='securitymodel',
            name='min_lot',
        ),
        migrations.RemoveField(
            model_name='securitymodel',
            name='nmnl_amt',
        ),
        migrations.RemoveField(
            model_name='securitymodel',
            name='open_dt',
        ),
        migrations.RemoveField(
            model_name='securitymodel',
            name='rgstrr',
        ),
        migrations.RemoveField(
            model_name='securitymodel',
            name='sector',
        ),
        migrations.RemoveField(
            model_name='securitymodel',
            name='shr_class',
        ),
        migrations.RemoveField(
            model_name='securitymodel',
            name='ttl_type',
        ),
        migrations.RemoveField(
            model_name='securitymodel',
            name='txtn_code',
        ),
        migrations.RemoveField(
            model_name='securitymodel',
            name='val_code',
        ),
        migrations.AddField(
            model_name='securitymodel',
            name='name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.DeleteModel(
            name='BondModel',
        ),
        migrations.DeleteModel(
            name='ExchangeModel',
        ),
        migrations.DeleteModel(
            name='StockModel',
        ),
    ]
