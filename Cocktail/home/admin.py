from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Recipe)
admin.site.register(Food)
admin.site.register(Tool)
admin.site.register(Alcohol)