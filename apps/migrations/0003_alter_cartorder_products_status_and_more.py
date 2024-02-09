# Generated by Django 4.2.5 on 2024-02-06 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0002_alter_cartorder_products_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartorder',
            name='products_status',
            field=models.CharField(choices=[('Shipped', 'Shipped'), ('delivered', 'Delivered'), ('process', 'Processing')], default='Processing', max_length=30),
        ),
        migrations.AlterField(
            model_name='product',
            name='products_status',
            field=models.CharField(choices=[('disable', 'Disable'), ('rejected', 'Rejected'), ('draft', 'Draft'), ('published', 'Published'), ('in_review', 'In Review')], default='In_review', max_length=10),
        ),
        migrations.AlterField(
            model_name='tags',
            name='responses',
            field=models.CharField(choices=[('3', '⭐⭐⭐'), ('5', '⭐⭐⭐⭐⭐'), ('2', '⭐⭐'), ('1', '⭐'), ('4', '⭐⭐⭐⭐')], default='⭐', max_length=1000000000),
        ),
    ]
