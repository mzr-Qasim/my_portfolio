# Generated by Django 5.0.6 on 2024-11-10 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(max_length=20, null=True)),
                ('description', models.TextField(max_length=20, null=True)),
                ('icon', models.CharField(max_length=300, null=True)),
            ],
            options={
                'verbose_name': '',
                'verbose_name_plural': 'Services',
            },
        ),
    ]
