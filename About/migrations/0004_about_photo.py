# Generated by Django 5.0.6 on 2024-11-11 05:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('About', '0003_alter_about_introduction_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='photo',
            field=models.FileField(blank=True, max_length=200, null=True, upload_to='Profile_photo'),
        ),
    ]
