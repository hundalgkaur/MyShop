# Generated by Django 5.0.7 on 2024-08-14 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myShopApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Add_product',
            fields=[
                ('product_id', models.AutoField(primary_key=True, serialize=False)),
                ('product_name', models.CharField(max_length=50)),
                ('product_category', models.CharField(default='', max_length=50)),
                ('product_subcategory', models.CharField(default='', max_length=50)),
                ('product_price', models.IntegerField(default=0)),
                ('product_desc', models.CharField(max_length=300)),
                ('product_img', models.ImageField(upload_to='images/images')),
            ],
        ),
    ]