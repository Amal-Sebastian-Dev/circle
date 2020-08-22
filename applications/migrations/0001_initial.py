# Generated by Django 3.0.5 on 2020-08-21 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Scheme',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name of the Scheme')),
                ('description', models.TextField(verbose_name='Description')),
                ('year_created', models.IntegerField(help_text='Year in which the scheme was declared', verbose_name='Year')),
                ('dept', models.CharField(choices=[('Health', 'Health'), ('Revenue', 'Revenue')], max_length=20, verbose_name='Department')),
                ('position', models.CharField(max_length=20, verbose_name='Position')),
                ('attachments', models.FileField(upload_to='schemes/', verbose_name='Supporting Documents')),
            ],
        ),
    ]
