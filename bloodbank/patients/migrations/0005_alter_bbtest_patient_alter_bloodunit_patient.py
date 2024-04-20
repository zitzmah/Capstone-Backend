# Generated by Django 5.0.4 on 2024-04-20 19:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0004_rename_patient_bbtest_patient'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bbtest',
            name='patient',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bbtests', to='patients.patient'),
        ),
        migrations.AlterField(
            model_name='bloodunit',
            name='patient',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='blood_units', to='patients.patient'),
        ),
    ]
