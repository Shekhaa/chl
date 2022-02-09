from django.contrib import admin

# Register your models here.
from shop.models import bloghome, product,contact,prod

admin.site.register(product)

admin.site.register(bloghome)
admin.site.register(contact)
admin.site.register(prod)