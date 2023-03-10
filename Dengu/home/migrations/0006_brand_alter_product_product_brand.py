# Generated by Django 4.1.4 on 2022-12-23 20:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0005_alter_product_product_image"),
    ]

    operations = [
        migrations.CreateModel(
            name="Brand",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
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
