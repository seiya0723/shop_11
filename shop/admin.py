from django.contrib import admin

from .models import Product,Cart,Address,Order


class OrderAdmin(admin.ModelAdmin):

    list_display    = ["dt","user","prefecture","city","address","paid","deliverd","session_id",]



admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(Address)

admin.site.register(Order,OrderAdmin)

