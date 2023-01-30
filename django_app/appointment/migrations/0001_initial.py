# Generated by Django 3.2.5 on 2022-12-26 19:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('email', models.CharField(max_length=250)),
                ('phone', models.CharField(max_length=250)),
                ('message', models.TextField(blank=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doctor_name', models.CharField(max_length=250)),
                ('doctor_email', models.CharField(max_length=250)),
                ('doctor_phone', models.CharField(max_length=250)),
                ('doctor_address', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Patient_name', models.CharField(max_length=250)),
                ('Patient_email', models.CharField(max_length=250)),
                ('Patient_phone', models.CharField(max_length=250)),
                ('Patient_address', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Meeting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('hour', models.TextField()),
                ('doctor_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appointment.doctor')),
                ('patient_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appointment.patient')),
            ],
        ),
    ]