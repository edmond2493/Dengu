from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import *
from .forms import *
from datetime import datetime, date
from django.core.paginator import Paginator
from django.http import JsonResponse
import json
from django.contrib.auth.models import User
import uuid

# Create your views here.

currentMonth = datetime.now().month
months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
]
season = {
    "January": "WINTER",
    "February": "WINTER",
    "March": "SPRING",
    "April": "SPRING",
    "May": "SPRING",
    "June": "SUMMER",
    "July": "SUMMER",
    "August": "SUMMER",
    "September": "AUTUMN",
    "October": "AUTUMN",
    "November": "AUTUMN",
    "December": "WINTER",
}


def home(request, season=season[months[currentMonth - 1]]):
    # products = Product.objects.filter(product_gender='MAN', product_season='SUMMER').values()
    # products = Product.objects.filter(product_gender = 'MAN', product_season = 'SUMMER').values('product_type_id').distinct()
    men_products = Product.objects.raw(
        f'SELECT * FROM home_product WHERE product_gender = "MAN" AND product_season = "{season}" GROUP BY product_type_id'
    )
    women_products = Product.objects.raw(
        f'SELECT * FROM home_product WHERE product_gender = "WOMAN" AND product_season = "{season}" GROUP BY product_type_id'
    )
    kids_products = Product.objects.raw(
        f'SELECT * FROM home_product WHERE product_gender = "KID" AND product_season = "{season}" GROUP BY product_type_id'
    )
    men_images = Product.objects.raw(
        f'SELECT * FROM home_product WHERE product_gender = "MAN" AND product_season = "{season}"'
    )
    women_images = Product.objects.raw(
        f'SELECT * FROM home_product WHERE product_gender = "WOMAN" AND product_season = "{season}"'
    )
    kids_images = Product.objects.raw(
        f'SELECT * FROM home_product WHERE product_gender = "KID" AND product_season = "{season}"'
    )
    slideshow_images = Slideshow.objects.raw(
        f'SELECT * FROM home_slideshow WHERE image_season = "{season}"'
    )
    brand_images = Brand.objects.raw(f"SELECT * FROM home_brand")
    # slideshow_images = Slideshow.objects.filter(image_season = 'WINTER')
    context = {
        "men_products": men_products,
        "women_products": women_products,
        "kids_products": kids_products,
        "men_images": men_images,
        "women_images": women_images,
        "kid_images": kids_images,
        "slideshow_images": slideshow_images,
        "brand_images": brand_images,
    }
    return render(request, "home.html", context)


def item(request, id):
    single_item = Product.objects.get(product_id=id)
    similar_item = Product.objects.raw(
        f'SELECT * FROM home_product WHERE product_gender = "{single_item.product_gender}" and product_type_id = "{single_item.product_type_id}" ORDER BY RAND()'
    )
    context = {"single_item": single_item, "similar_item": similar_item}
    return render(request, "item.html", context)


def items(request, season, gender, type, brand="product_brand_id"):
    # items_gender = Product.objects.raw(f'SELECT * FROM home_product WHERE product_gender = "{gender}" AND product_season = "{season}" AND product_type LIKE "{type}"')
    p = Paginator(
        Product.objects.raw(
            f'SELECT * FROM home_product WHERE product_gender = "{gender}" AND product_season = "{season}" AND product_type_id = "{type}" AND product_brand_id = "{brand}"'
        ),
        8,
    )
    page = request.GET.get("page")
    items_gender = p.get_page(page)
    context = {"items_gender": items_gender}
    return render(request, "items.html", context)


def search(request):
    if request.method == "GET":
        # searched_items = Product.objects.raw(f'''SELECT * FROM home_product WHERE product_name LIKE "%{searchBar}%"
        # keyword = request.GET.get('keywords')
        searchBar = request.GET["searchBar"]
        p = Paginator(
            Product.objects.raw(
                f"""SELECT * FROM home_product WHERE product_name LIKE "%{searchBar}%" 
        OR product_brand_id LIKE "%{searchBar}%" OR product_type_id LIKE (SELECT type_id FROM home_type WHERE type_name LIKE "%{searchBar.capitalize()}%") 
        OR product_season LIKE "%{searchBar.capitalize()}%" ORDER BY product_gender DESC"""
            ),
            8,
        )
        page = request.GET.get("page")
        searched_items = p.get_page(page)
        context = {"searched_items": searched_items, "searchBar": searchBar}
        return render(request, "search.html", context)

    else:
        return render(request, "search.html")


def cart(request):
    if request.user.is_authenticated:
        customer = request.user
        order, created = Order.objects.get_or_create(customer=customer, completed=False)
        # cart_items = Order.objects.raw(f'SELECT * FROM home_order WHERE customer_id = "{customer}"')
        cart_items = order.orderitem_set.all()
        context = {"cart_items": cart_items, "order": order}
    else:
        cart_items = []
        order = {"get_cart_total": 0, "get_cart_items": 0}
        context = {"cart_items": cart_items, "order": order}
    return render(request, "cart.html", context)


def updateItem(request):
    data = json.loads(request.body)
    productID = data["productId"]
    action = data["action"]
    customer = request.user
    product = Product.objects.get(product_id=productID)
    order, created = Order.objects.get_or_create(customer=customer, completed=False)
    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)
    item_quantity = Product.objects.values_list("product_quantity", flat=True).filter(product_id=productID)[0]
    if action == "add":
        if item_quantity > orderItem.quantity:
            orderItem.quantity = orderItem.quantity + 1
    elif action == "remove":
        if orderItem.quantity >= 1:
            orderItem.quantity = orderItem.quantity - 1

    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()
    order, created = Order.objects.get_or_create(customer=customer, completed=False)

    cartCount = order.get_cart_items
    cartSum = order.get_cart_total
    itemCount = orderItem.quantity
    itemSum = orderItem.get_total
    return JsonResponse([cartCount, cartSum, itemCount, itemSum], safe=False)


def complete(request):
    data = json.loads(request.body)
    customer = request.user
    order, created = Order.objects.get_or_create(customer=customer, completed=False)
    transcation_id = uuid.uuid4()
    total = float(data["shippingInfo"]["total"])
    order.transaction_id = transcation_id

    for i in data['id_list']:
        product = Product.objects.get(product_id=i)
        # order, created = Order.objects.get_or_create(customer=customer, completed=False)
        orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)
        item_quantity = Product.objects.values_list("product_quantity", flat=True).filter(product_id=i)[0]
        Product.objects.filter(product_id=i).update(product_quantity = (item_quantity - orderItem.quantity))

    if total == order.get_cart_total:
        order.completed = True
    Shipping.objects.create(
        customer = customer,
        order = order,
        first_name = data["shippingInfo"]["first_name"],
        last_name = data["shippingInfo"]["last_name"],
        phone_number = data["shippingInfo"]["phone"],
        email = data["shippingInfo"]["email"],
        country = data["shippingInfo"]["country"],
        city = data["shippingInfo"]["city"],
        street = data["shippingInfo"]["street"],
        zip_code = data["shippingInfo"]["zip"],
        date_added = date.today(),
    )

    order.save()
    return JsonResponse("this is the compelete order", safe=False)


def checkout(request):
    return render(request, "checkout.html")

def about(request):
    return render(request, "about.html")
  
def contact(request):
    submittet = False
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('contact?submit')
    else: 
        form = ContactForm
        if 'submit' in request.GET:
            submittet = True
            print('this is the print', request.GET, f'{submittet}')
            

    return render(request, 'contact.html', {'form': form, 'submittet': submittet})

def profile(request):
    try:
        customer = request.user
        orders = Order.objects.filter(customer=customer, completed=True).values()
        order_list = []
        for order in orders:
            order1 = Order.objects.get(customer=customer, completed=True, id=order['id'])
            cart_items = order1.orderitem_set.all()
            order_list.append(cart_items)
        context = {'order_list': order_list}
    except TypeError:
        context = {'order_list': ''}
    
    return render(request, "profile.html", context)
