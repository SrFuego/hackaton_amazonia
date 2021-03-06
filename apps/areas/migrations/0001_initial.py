# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-12 08:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0004_auto_20171112_0310'),
    ]

    operations = [
        migrations.CreateModel(
            name='Money',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('month', models.CharField(choices=[('jan', 'enero'), ('feb', 'febrero'), ('mar', 'marzo'), ('apr', 'abril'), ('may', 'mayo'), ('jun', 'junio'), ('jul', 'julio'), ('aug', 'agosto'), ('sep', 'septiembre'), ('oct', 'octubre'), ('nov', 'noviembre'), ('dic', 'diciembre')], max_length=3)),
                ('mount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='account', to='accounts.Account')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ProtectedNaturalArea',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('account', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='protected_natural_area', to='accounts.Account')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Visits',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('approved', models.BooleanField(default=False)),
                ('date', models.DateField()),
                ('exonerated', models.PositiveIntegerField()),
                ('foreign', models.PositiveIntegerField()),
                ('national', models.PositiveIntegerField()),
                ('non_paying', models.PositiveIntegerField()),
                ('payers', models.PositiveIntegerField()),
                ('protected_natural_area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='visits', to='areas.ProtectedNaturalArea')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
