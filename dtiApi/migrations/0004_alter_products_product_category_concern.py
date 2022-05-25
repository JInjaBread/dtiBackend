# Generated by Django 4.0.4 on 2022-05-19 06:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dtiApi', '0003_alter_products_prooduct_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='product_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category', to='dtiApi.productcategory'),
        ),
        migrations.CreateModel(
            name='Concern',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('receipt_image', models.ImageField(upload_to='complains/')),
                ('complainant_email', models.CharField(max_length=255)),
                ('complains', models.CharField(max_length=255)),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dtiApi.products')),
            ],
        ),
    ]