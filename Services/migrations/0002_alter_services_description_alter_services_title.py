# Generated by Django 5.0.6 on 2024-11-10 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Services', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='services',
            name='description',
            field=models.TextField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='services',
            name='title',
            field=models.TextField(max_length=30, null=True),
        ),
    ]
