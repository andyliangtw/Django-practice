from django.contrib import admin
from django.utils.translation import gettext_lazy as _


class Morethanfifty(admin.SimpleListFilter):

    title = _('price')
    parameter_name = 'compareprice'  # url最先要接的參數

    def lookups(self, request, model_admin):
        return (
            ('>50', _('>50')),  # 前方對應下方'>50'(也就是url的request)，第二個對應到admin顯示的文字
            ('<=50', _('<=50')),
        )

    # 定義查詢時的過濾條件
    def queryset(self, request, queryset):
        if self.value() == '>50':
            return queryset.filter(price_name__gt=50)
        if self.value() == '<=50':
            return queryset.filter(price_name__lte=50)
