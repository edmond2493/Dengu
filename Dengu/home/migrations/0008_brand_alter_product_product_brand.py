# Generated by Django 4.1.4 on 2022-12-23 20:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0007_alter_product_product_brand_delete_brand"),
    ]

    operations = [
        migrations.CreateModel(
            name="Brand",
            fields=[
                ("brand_id", models.AutoField(primary_key=True, serialize=False)),
                ("brand_name", models.CharField(max_length=50)),
                ("brande_image", models.ImageField(upload_to="static/media/brands")),
            ],
        ),
        migrations.AlterField(
            model_name="product",
            name="product_brand",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="home.brand"
            ),
        ),
    ]
