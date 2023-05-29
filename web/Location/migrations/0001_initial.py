# Generated by Django 4.1.6 on 2023-05-26 13:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('abbr', models.CharField(max_length=3, unique=True)),
                ('name', models.CharField(max_length=20, unique=True)),
                ('slug', models.CharField(blank=True, max_length=50, verbose_name='SLUG/URL')),
                ('flag_path', models.ImageField(blank=True, upload_to='state_flag')),
                ('title', models.CharField(blank=True, max_length=150)),
                ('years_from_diag', models.IntegerField(blank=True, default=0)),
                ('years_from_death', models.IntegerField(blank=True, default=0)),
            ],
        ),
        migrations.CreateModel(
            name='ZipCode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=7, unique=True)),
            ],
            options={
                'verbose_name': 'Zip Code',
                'verbose_name_plural': 'Zip Code',
            },
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('slug', models.CharField(max_length=100)),
                ('search_slug', models.CharField(max_length=100, unique=True)),
                ('number_of_population', models.BigIntegerField(blank=True, default=0, null=True)),
                ('state', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='Location.state')),
                ('zipcode', models.ManyToManyField(blank=True, to='Location.zipcode')),
            ],
        ),
    ]
