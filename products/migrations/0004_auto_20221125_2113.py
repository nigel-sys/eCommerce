# Generated by Django 2.1.15 on 2022-11-25 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20221125_2100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_image',
            field=models.ImageField(default='/media/images/no_product_image.png', upload_to='products'),
        ),
    ]
