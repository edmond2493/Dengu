# Generated by Django 4.1.4 on 2022-12-23 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0006_brand_alter_product_product_brand"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="product_brand",
            field=models.CharField(max_length=50),
        ),
        migrations.DeleteModel(
            name="Brand",
        ),
    ]
