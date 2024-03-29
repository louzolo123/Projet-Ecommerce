# Generated by Django 4.2.5 on 2024-02-10 22:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usersauths', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=450)),
                ('email', models.CharField(max_length=450)),
                ('phone', models.CharField(max_length=450)),
                ('description', models.CharField(max_length=450)),
                ('messages', models.CharField(max_length=450)),
            ],
            options={
                'verbose_name': 'Contact Us',
                'verbose_name_plural': 'Contact Us',
            },
        ),
    ]
