# Generated by Django 4.1.4 on 2022-12-29 20:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("home", "0011_order_orderitem"),
    ]

    operations = [
        migrations.CreateModel(
            name="Shipping",
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
                ("first_name", models.CharField(max_length=50)),
                ("last_name", models.CharField(max_length=50)),
                ("phone_number", models.CharField(max_length=150)),
                ("email", models.EmailField(max_length=150)),
                ("country", models.CharField(max_length=50)),
                ("city", models.CharField(max_length=50)),
                ("street", models.CharField(max_length=150)),
                ("zip_code", models.CharField(max_length=50)),
                ("date_added", models.DateTimeField(auto_now_add=True)),
                (
                    "customer",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "order",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="home.order",
                    ),
                ),
            ],
        ),
    ]
