# Generated by Django 3.0.5 on 2020-08-22 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applications', '0011_certificate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='certificate',
            name='certificate',
            field=models.FileField(blank=True, null=True, upload_to='certificates/', verbose_name='Certificate'),
        ),
    ]
