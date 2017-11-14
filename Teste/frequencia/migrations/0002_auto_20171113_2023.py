# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-13 23:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('frequencia', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='frequencia',
            name='funcionarios',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='frequencia.Funcionario'),
        ),
        migrations.AlterField(
            model_name='faixahoraria',
            name='horaF',
            field=models.TimeField(null=True),
        ),
        migrations.AlterField(
            model_name='faixahoraria',
            name='horaF2',
            field=models.TimeField(null=True),
        ),
        migrations.AlterField(
            model_name='faixahoraria',
            name='horaI',
            field=models.TimeField(null=True),
        ),
        migrations.AlterField(
            model_name='faixahoraria',
            name='horaI2',
            field=models.TimeField(null=True),
        ),
    ]
