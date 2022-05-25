# Generated by Django 4.0.4 on 2022-05-11 03:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=255)),
                ('prooduct_price', models.PositiveIntegerField()),
                ('product_image', models.ImageField(upload_to='images/')),
                ('product_description', models.CharField(max_length=255)),
                ('main_category', models.CharField(choices=[('BASIC NECESSITIES', 'BASIC NECESSITIES'), ('PRIME COMMODITIES', 'PRIME COMMODITIES')], max_length=255)),
                ('product_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dtiApi.productcategory')),
            ],
        ),
    ]