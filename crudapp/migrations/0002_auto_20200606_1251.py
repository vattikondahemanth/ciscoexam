# Generated by Django 3.0.2 on 2020-06-06 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crudapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ciscomodel',
            name='hostname',
            field=models.CharField(blank=True, max_length=18, null=True),
        ),
        migrations.AlterField(
            model_name='ciscomodel',
            name='loopback',
            field=models.CharField(blank=True, max_length=18, null=True),
        ),
        migrations.AlterField(
            model_name='ciscomodel',
            name='macaddress',
            field=models.CharField(blank=True, max_length=18, null=True),
        ),
        migrations.AlterField(
            model_name='ciscomodel',
            name='sapid',
            field=models.CharField(blank=True, max_length=18, null=True),
        ),
    ]