# Generated by Django 3.0.5 on 2020-08-21 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_remove_user_full_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Applicant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='full_name',
            field=models.CharField(default='John Doe', max_length=50, verbose_name='Full Name'),
            preserve_default=False,
        ),
    ]
