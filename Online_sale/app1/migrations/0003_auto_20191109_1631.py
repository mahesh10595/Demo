# Generated by Django 2.2.6 on 2019-11-09 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_marchantmodel_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='marchantmodel',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]
