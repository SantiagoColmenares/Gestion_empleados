# Generated by Django 5.0.2 on 2024-03-23 19:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('country_code', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('desciption', models.TextField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Salary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amound', models.CharField(max_length=50)),
                ('extra_dec', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('country_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='empleados.country')),
            ],
        ),
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=50)),
                ('location_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='empleados.location')),
            ],
        ),
        migrations.CreateModel(
            name='Employe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_number', models.CharField(max_length=50)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('job_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='empleados.job')),
                ('place_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='empleados.place')),
            ],
        ),
        migrations.AddField(
            model_name='job',
            name='salary_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='empleados.salary'),
        ),
    ]