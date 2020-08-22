# Generated by Django 3.0.5 on 2020-08-22 01:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20200821_2216'),
    ]

    operations = [
        migrations.AlterField(
            model_name='office',
            name='office_type',
            field=models.CharField(choices=[('Grama Panchayath', 'Grama Panchayath'), ('Village Office', 'Village Office'), ('Thalukk Office', 'Thalukk Office')], max_length=30, verbose_name='Office Type'),
        ),
    ]