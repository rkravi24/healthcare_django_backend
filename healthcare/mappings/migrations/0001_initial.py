# Generated by Django 4.2.7 on 2025-05-13 18:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('doctors', '0001_initial'),
        ('patients', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PatientDoctorMapping',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('notes', models.TextField(blank=True, null=True)),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='patient_mappings', to='doctors.doctor')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='doctor_mappings', to='patients.patient')),
            ],
            options={
                'ordering': ['-created_at'],
                'unique_together': {('patient', 'doctor')},
            },
        ),
    ]
