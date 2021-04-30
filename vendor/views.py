from django.shortcuts import render

from .models import Vendor
from .forms import RawVendorForm


def index(request):
    vendor_list = Vendor.objects.all()  # 把所有 Vendor 的資料取出來
    context = {'vendor_list': vendor_list}  # 建立 Dict 對應到 Vendor 的資料，
    return render(request, 'vendor/detail.html', context)


def create_view(request):
    form = RawVendorForm(request.POST or None)
    if form.is_valid():
        Vendor.objects.create(**form.cleaned_data)
        form = RawVendorForm()

    context = {
        'form': form
    }
    return render(request, "vendor/create.html", context)
