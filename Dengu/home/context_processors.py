from .models import *

def navCategory(request):
    men_categories = Product.objects.raw(f'SELECT * FROM home_product WHERE product_gender = "MAN" GROUP BY product_type_id')
    women_categories = Product.objects.raw(f'SELECT * FROM home_product WHERE product_gender = "WOMAN" GROUP BY product_type_id')
    kids_categories = Product.objects.raw(f'SELECT * FROM home_product WHERE product_gender = "KID" GROUP BY product_type_id')
    latest = Product.objects.raw(f'SELECT * FROM home_product ORDER BY product_id DESC LIMIT 20')
    brands = Brand.objects.raw(f'SELECT * FROM home_brand')
    print(latest[0])
    if request.user.is_authenticated:
        customer = request.user
        order, created = Order.objects.get_or_create(customer=customer, completed=False)
        numItems = order.get_cart_items
    else:
        cart_items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0}
        numItems = order['get_cart_items']
    context = {"men_categories": men_categories, "women_categories": women_categories, "kids_categories": kids_categories, 'brands': brands, 'numItems': numItems, 'latest': latest}
    return (context)