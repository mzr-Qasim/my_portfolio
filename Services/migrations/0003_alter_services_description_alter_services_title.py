# Generated by Django 5.0.6 on 2024-11-10 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Services', '0002_alter_services_description_alter_services_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='services',
            name='description',
            field=models.TextField(max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='services',
            name='title',
            field=models.TextField(max_length=50, null=True),
        ),
    ]
