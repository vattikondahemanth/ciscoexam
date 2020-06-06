# Generated by Django 3.0.2 on 2020-06-06 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CiscoModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sapid', models.TextField(blank=True, max_length=18, null=True)),
                ('hostname', models.TextField(blank=True, max_length=18, null=True)),
                ('loopback', models.TextField(blank=True, max_length=18, null=True)),
                ('macaddress', models.TextField(blank=True, max_length=18, null=True)),
            ],
        ),
    ]
