from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView, DetailView, CreateView, UpdateView

from .models import Vendor
from .forms import VendorModelForm


# def index(request):
#     vendor_list = Vendor.objects.all()  # 把所有 Vendor 的資料取出來
#     context = {'vendor_list': vendor_list}  # 建立 Dict 對應到 Vendor 的資料，
#     return render(request, 'vendor/index.html', context)

class VendorListView(ListView):
    model = Vendor
    template_name = 'vendor/index.html'


# def create_view(request):
#     form = RawVendorForm(request.POST or None)
#     if form.is_valid():
#         Vendor.objects.create(**form.cleaned_data)
#         form = RawVendorForm()

#     context = {
#         'form': form
#     }
#     return render(request, "vendor/create.html", context)

class VendorCreateView(CreateView):
    # model = Vendor
    # fields = '__all__'
    # fields = ['vendor_name', 'store_name']
    form_class = VendorModelForm
    template_name = 'vendor/create.html'


# def singleVendor(request, id):
#     vendor = get_object_or_404(Vendor, id=id)  # appeared when DEBUG=False
#     # try:
#     #     vendor = Vendor.objects.get(id=id)
#     # except Vendor.DoesNotExist:
#     #     raise Http404
#     context = {
#         'vendor': vendor
#     }
#     return render(request, 'vendor/detail.html', context)

class VendorDetailView(DetailView):
    model = Vendor
    template_name = 'vendor/detail.html'


class VendorUpdateView(UpdateView):
    form_class = VendorModelForm
    template_name = 'vendor/create.html'
    queryset = Vendor.objects.all()  # 這很重要
