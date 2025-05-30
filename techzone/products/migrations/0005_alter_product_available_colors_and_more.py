# Generated by Django 5.2.1 on 2025-05-12 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_color_storage_remove_product_product_color_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='available_colors',
            field=models.ManyToManyField(blank=True, null=True, to='products.color'),
        ),
        migrations.AlterField(
            model_name='product',
            name='available_storage',
            field=models.ManyToManyField(blank=True, null=True, to='products.storage'),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_category',
            field=models.CharField(blank=True, choices=[('smartphones', 'smartphones'), ('laptops', 'laptops'), ('accessories', 'accessories')], default='smartphones', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_key_features',
            field=models.TextField(blank=True, help_text='Separate each feature with a semicolon (;)', null=True),
        ),
    ]
