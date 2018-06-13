# Generated by Django 2.0.6 on 2018-06-13 22:54

import PyLightCommon.pylightcommon.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ConnectedSystem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Name of Client')),
                ('lastIP', models.GenericIPAddressField(verbose_name='Last known IP address of client')),
                ('lastMacAddress', models.CharField(max_length=255, verbose_name='Mac Address of client')),
                ('serialNumber', models.CharField(max_length=255, unique=True, verbose_name='Serial Number of Pi')),
                ('connected', models.BooleanField(default=False, verbose_name='Status of connection to pi')),
                ('active', models.BooleanField(default=False, verbose_name='Status of Pi added in UI')),
            ],
        ),
        migrations.CreateModel(
            name='IO',
            fields=[
                ('ioNr', models.IntegerField(primary_key=True, serialize=False, verbose_name='physical io nr on pi')),
            ],
        ),
        migrations.CreateModel(
            name='IOType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ioType', models.CharField(choices=[(PyLightCommon.pylightcommon.models.EnumIOType('IOType.NONE'), 'IOType.NONE'), (PyLightCommon.pylightcommon.models.EnumIOType('IOType.OUTPUT'), 'IOType.OUTPUT'), (PyLightCommon.pylightcommon.models.EnumIOType('IOType.INPUT'), 'IOType.INPUT')], max_length=255, verbose_name='Type of output')),
            ],
        ),
        migrations.CreateModel(
            name='UsedIO',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='human readable name for the io')),
                ('active', models.BooleanField(default=False, verbose_name='Active/Non Active IO')),
                ('timeStart', models.TimeField(null=True, verbose_name='Start time of timer')),
                ('timeEnd', models.TimeField(null=True, verbose_name='End time of timer')),
                ('connectedSystem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pylightcommon.ConnectedSystem')),
                ('pin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pylightcommon.IO', verbose_name='Pin nr')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pylightcommon.IOType', verbose_name='Type of IO')),
            ],
        ),
    ]