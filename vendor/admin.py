from django.contrib import admin

from .models import Vendor, Food
from .list_filter import Morethanfifty


@admin.register(Vendor)
class VendorAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Vendor._meta.fields]
    # list_display = ['id', 'vendor_name', 'store_name', 'phone_number', 'address']


@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Food._meta.fields]
    list_filter = [Morethanfifty]
    fileds = ['price_name']  # 限制 Admin 可以修改的欄位
    search_fields = ['food_name', 'price_name']  # 搜尋欄位
    ordering = ['price_name']  # 價格 由小到大 排序
    # ordering = ['-price_name']  # 價格 由大到小 排序
