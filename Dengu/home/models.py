from django.db import models
from django.contrib.auth.models import User

# Create your models here.
SEASON_CHOICES = [
        ('SPRING', 'Spring'),
        ('SUMMER', 'Summer'),
        ('AUTUMN', 'Autumn'),
        ('WINTER', 'Winter')
    ]

GENDER_CHOICES = [
        ('MAN', 'Man'),
        ('WOMAN', 'Woman'),
        ('KID', 'Kid')
    ]


class Brand(models.Model):
    brand_id = models.AutoField(primary_key=True)
    brand_name = models.CharField(max_length=50)
    brand_image = models.ImageField(upload_to='static/media/brands')

    def __str__(self):
        return f'{self.brand_name}'

class Type(models.Model):
    type_id = models.AutoField(primary_key=True)
    type_name = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.type_name}'


class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=50)
    product_image = models.ImageField(upload_to='static/media/products')
    product_brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    product_season = models.CharField(max_length=50, choices=SEASON_CHOICES)
    product_gender = models.CharField(max_length=50, choices=GENDER_CHOICES)
    product_type = models.ForeignKey(Type, on_delete=models.CASCADE)
    product_price = models.DecimalField(max_digits=10, decimal_places=2)
    product_quantity = models.PositiveIntegerField()
    product_description = models.TextField(max_length=500)

    def __str__(self):
        return f'{self.product_season}, {self.product_gender}, {self.product_type}, {self.product_price}, {self.product_brand}, {self.product_quantity}, {self.product_name}'


class Slideshow(models.Model):
    image_season = models.CharField(max_length=50, choices=SEASON_CHOICES)
    image_file = models.ImageField(upload_to='static/media/slideshow')

    def __str__(self):
        return f'{self.image_season} {self.image_file}'


class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)
    transaction_id = models.CharField(max_length=255)

    def __str__(self):
        # return f'Customer: {self.customer}, Transaction ID: {self.transaction_id}, Date: {self.date_ordered}'
        return str(self.id)

    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total

    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total

    

class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    quantity = models.PositiveBigIntegerField(default=0)

    def __str__(self):
        return f'{self.product}, {self.order}, {self.quantity}'

    @property
    def get_total(self):
        total = self.product.product_price * self.quantity
        return total


class Shipping(models.Model):
    customer = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=150)
    email = models.EmailField(max_length=150)
    country = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    street = models.CharField(max_length=150)
    zip_code = models.CharField(max_length=50)
    date_added = models.DateTimeField(auto_now_add=True)

class Contact(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=250)
    phone = models.CharField(max_length=100)
    comment = models.TextField(max_length=1000)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'