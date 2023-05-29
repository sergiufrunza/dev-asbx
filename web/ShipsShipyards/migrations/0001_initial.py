# Generated by Django 4.1.6 on 2023-05-26 13:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Location', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Manufacturer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Shipyard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('slug', models.CharField(max_length=60, unique=True)),
                ('city', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Location.city')),
                ('state', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Location.state')),
            ],
        ),
        migrations.CreateModel(
            name='Ship',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60, unique=True)),
                ('slug', models.CharField(max_length=60, unique=True)),
                ('build_from', models.CharField(max_length=60)),
                ('build_to', models.CharField(max_length=60)),
                ('manufacturers', models.ManyToManyField(blank=True, to='ShipsShipyards.manufacturer')),
                ('shipyard', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='ShipsShipyards.shipyard')),
            ],
        ),
        migrations.CreateModel(
            name='Equipment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('nr', models.CharField(default='-', max_length=5)),
                ('manufacturer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='ShipsShipyards.manufacturer')),
                ('ship', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='ShipsShipyards.ship')),
            ],
        ),
    ]
