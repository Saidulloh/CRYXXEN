from django.contrib import admin

from apps.basket_detail.models import BasketDetail


class BasketDetailAdmin(admin.ModelAdmin):
    list_display = ['id', 'amount', 'owner']

admin.site.register(BasketDetail, BasketDetailAdmin)
