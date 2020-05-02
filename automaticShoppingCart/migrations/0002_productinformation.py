# Generated by Django 3.0.5 on 2020-05-02 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('automaticShoppingCart', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='productInformation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serialNo', models.IntegerField()),
                ('product', models.CharField(max_length=50)),
                ('product_details', models.CharField(max_length=50)),
                ('price', models.CharField(max_length=20)),
                ('quantity', models.IntegerField()),
                ('subtotal', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name_plural': 'Product Details',
            },
        ),
    ]