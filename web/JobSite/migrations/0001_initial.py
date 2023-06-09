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
            name='Budget',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, unique=True)),
                ('initial_amount', models.BigIntegerField(blank=True, default=0, null=True)),
                ('available_amount', models.BigIntegerField(blank=True, default=0, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Compensation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('compensation_er', models.BigIntegerField(blank=True, default=0, null=True)),
                ('compensation_avg', models.BigIntegerField(blank=True, default=0, null=True)),
                ('compensation_ir', models.BigIntegerField(blank=True, default=0, null=True)),
                ('ratio', models.FloatField(blank=True, default=0.0, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Disease',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='ExposureHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year_from', models.IntegerField()),
                ('year_to', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='JobSiteContent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('list_part', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='CompensationAsbestosis',
            fields=[
                ('compensation_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='JobSite.compensation')),
                ('name', models.CharField(max_length=50, unique=True)),
            ],
            bases=('JobSite.compensation',),
        ),
        migrations.CreateModel(
            name='CompensationLungCancer',
            fields=[
                ('compensation_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='JobSite.compensation')),
                ('name', models.CharField(max_length=50, unique=True)),
            ],
            bases=('JobSite.compensation',),
        ),
        migrations.CreateModel(
            name='CompensationMesothelioma',
            fields=[
                ('compensation_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='JobSite.compensation')),
                ('name', models.CharField(max_length=50, unique=True)),
            ],
            bases=('JobSite.compensation',),
        ),
        migrations.CreateModel(
            name='CompensationOtherCancer',
            fields=[
                ('compensation_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='JobSite.compensation')),
                ('name', models.CharField(max_length=50, unique=True)),
            ],
            bases=('JobSite.compensation',),
        ),
        migrations.CreateModel(
            name='CompensationSevereAsbestosis',
            fields=[
                ('compensation_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='JobSite.compensation')),
                ('name', models.CharField(max_length=50, unique=True)),
            ],
            bases=('JobSite.compensation',),
        ),
        migrations.CreateModel(
            name='Trust',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(max_length=150, unique=True, verbose_name='SLUG/URL')),
                ('company_name', models.CharField(blank=True, max_length=150)),
                ('fund_name', models.CharField(blank=True, max_length=150)),
                ('abbr', models.CharField(blank=True, max_length=20)),
                ('start_production', models.IntegerField(blank=True, default=0, null=True)),
                ('end_production', models.IntegerField(blank=True)),
                ('description', models.TextField(blank=True)),
                ('logo', models.ImageField(blank=True, upload_to='trustfunds_logo')),
                ('budget', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='JobSite.budget')),
                ('states', models.ManyToManyField(to='Location.state')),
                ('asbestosis', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='JobSite.compensationasbestosis')),
                ('lung_cancer', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='JobSite.compensationlungcancer')),
                ('mesothelioma', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='JobSite.compensationmesothelioma')),
                ('other_cancer', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='JobSite.compensationothercancer')),
                ('severe_asbestosis', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='JobSite.compensationsevereasbestosis')),
            ],
        ),
        migrations.CreateModel(
            name='JobSite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('slug', models.CharField(max_length=150, unique=True)),
                ('city', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Location.city')),
                ('content', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='JobSite.jobsitecontent')),
                ('exposure', models.ManyToManyField(blank=True, to='JobSite.exposurehistory')),
                ('state', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Location.state')),
            ],
        ),
        migrations.AddField(
            model_name='exposurehistory',
            name='trust',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='JobSite.trust'),
        ),
        migrations.CreateModel(
            name='Boiler',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('manufacturer', models.CharField(max_length=255)),
                ('year_built', models.CharField(default='N/A', max_length=10)),
                ('city', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Location.city')),
                ('state', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Location.state')),
                ('zip', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Location.zipcode')),
            ],
        ),
    ]
