# Generated by Django 5.0.7 on 2024-08-14 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myShopApp', '0002_add_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=100)),
                ('category', models.CharField(default='', max_length=100)),
                ('subcategory', models.CharField(default='', max_length=50)),
                ('price', models.IntegerField(default=0)),
                ('desc', models.CharField(max_length=300)),
                ('image', models.ImageField(upload_to='images/images')),
            ],
        ),
        migrations.DeleteModel(
            name='Add_product',
        ),
    ]