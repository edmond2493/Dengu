# Generated by Django 4.1.4 on 2022-12-12 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('product_id', models.AutoField(primary_key=True, serialize=False)),
                ('product_name', models.CharField(max_length=50)),
                ('product_image', models.ImageField(upload_to='')),
                ('product_brand', models.CharField(max_length=50)),
                ('product_season', models.CharField(choices=[('SPRING', 'Spring'), ('SUMMER', 'Summer'), ('AUTUMN', 'Autumn'), ('WINTER', 'Winter')], max_length=50)),
                ('product_gender', models.CharField(choices=[('MAN', 'Man'), ('WOMAN', 'Woman'), ('KID', 'Kid')], max_length=50)),
                ('product_type', models.CharField(choices=[('HATS', 'Hats'), ('HOODIE', 'Hoodie'), ('PANTS', 'Pants'), ('JACKET', 'Jacket'), ('SHIRT', 'Shirt'), ('SWEATER', 'Sweater'), ('SCARF', 'Scarf'), ('DRESS', 'Dress'), ('SHOES', 'Shoes')], max_length=50)),
                ('product_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('product_quantity', models.PositiveIntegerField()),
                ('product_description', models.TextField(max_length=500)),
            ],
        ),
    ]