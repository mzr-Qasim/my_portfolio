# Generated by Django 5.0.6 on 2024-11-09 19:37

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Skills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill_name', models.CharField(blank=True, max_length=30, null=True)),
                ('skill_percentage', models.PositiveSmallIntegerField(validators=[django.core.validators.MinValueValidator(10), django.core.validators.MaxValueValidator(100)])),
            ],
            options={
                'verbose_name': '',
                'verbose_name_plural': 'Skills',
            },
        ),
    ]