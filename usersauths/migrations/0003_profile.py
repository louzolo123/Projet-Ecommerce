# Generated by Django 4.2.5 on 2024-02-10 22:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usersauths', '0002_contactus'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=450)),
                ('bio', models.CharField(blank=True, max_length=500)),
                ('image', models.ImageField(upload_to='image')),
                ('phone', models.CharField(max_length=55)),
                ('verified', models.BooleanField(default=False)),
            ],
        ),
    ]
