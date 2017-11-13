# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-23 23:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='curso',
            name='ativo',
            field=models.BooleanField(default=True, verbose_name='Ativo?'),
        ),
        migrations.AddField(
            model_name='curso',
            name='descricao',
            field=models.TextField(blank=True, verbose_name='Descrição'),
        ),
        migrations.AlterField(
            model_name='curso',
            name='carga_horaria',
            field=models.IntegerField(verbose_name='Carga Horária'),
        ),
        migrations.AlterField(
            model_name='curso',
            name='nome',
            field=models.CharField(max_length=20, verbose_name='Nome'),
        ),
        migrations.AlterField(
            model_name='curso',
            name='professor',
            field=models.CharField(max_length=20, verbose_name='Professor'),
        ),
        migrations.AlterField(
            model_name='curso',
            name='tipo',
            field=models.CharField(max_length=20, verbose_name='Tipo'),
        ),
    ]
