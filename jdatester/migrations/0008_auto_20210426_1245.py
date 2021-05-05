# Generated by Django 3.1.6 on 2021-04-26 16:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jdatester', '0007_auto_20210426_0859'),
    ]

    operations = [
        migrations.CreateModel(
            name='SecurityModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ticker', models.CharField(max_length=12)),
                ('name', models.CharField(max_length=200)),
                ('isin', models.CharField(max_length=12)),
            ],
        ),
        migrations.AlterField(
            model_name='indexpricemodel',
            name='value',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=18, null=True),
        ),
        migrations.CreateModel(
            name='SecurityPriceModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('security_date', models.DateTimeField()),
                ('avg_price', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=10, null=True)),
                ('open', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=10, null=True)),
                ('close', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=10, null=True)),
                ('high', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=10, null=True)),
                ('low', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=10, null=True)),
                ('ask', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=10, null=True)),
                ('bid', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=10, null=True)),
                ('trans_total', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=18, null=True)),
                ('volume', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=18, null=True)),
                ('trans_value', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=18, null=True)),
                ('security', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jdatester.securitymodel')),
            ],
        ),
    ]
