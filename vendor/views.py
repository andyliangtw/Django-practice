from django.shortcuts import render
from .models import Vendor


def vendor_index(request):
    vendor_list = Vendor.objects.all()  # 把所有 Vendor 的資料取出來
    context = {'vendor_list': vendor_list}  # 建立 Dict 對應到 Vendor 的資料，
    return render(request, 'vendor/detail.html', context)
