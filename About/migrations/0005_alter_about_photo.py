# Generated by Django 5.0.6 on 2024-11-11 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('About', '0004_about_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='photo',
            field=models.FileField(max_length=200, null=True, upload_to='Profile_photo'),
        ),
    ]