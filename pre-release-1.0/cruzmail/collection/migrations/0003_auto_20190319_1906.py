# Generated by Django 2.0.6 on 2019-03-20 02:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collection', '0002_auto_20190319_1903'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mailstops_master',
            name='ms_route',
            field=models.CharField(choices=[('W', 'W'), ('C', 'C'), ('E', 'E')], default='W', max_length=10),
        ),
        migrations.AlterField(
            model_name='packages_master',
            name='pkg_email',
            field=models.CharField(choices=[('y', 'yes'), ('n', 'no')], default='y', max_length=10),
        ),
        migrations.AlterField(
            model_name='packages_master',
            name='pkg_sign',
            field=models.CharField(choices=[('y', 'yes'), ('n', 'no')], default='n', max_length=10),
        ),
    ]
