# Generated by Django 5.0.6 on 2024-11-09 17:47

import About.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('About', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='cv',
            field=models.FileField(blank=True, null=True, upload_to='CV/', validators=[About.models.validate_pdf]),
        ),
    ]