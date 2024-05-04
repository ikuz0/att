from django.contrib import admin

from internet_shop.models import Client, Goods, Order


@admin.action(description="Сбросить количество в ноль")
def reset_amount(modeladmin, request, queryset):
    queryset.update(amount=0)


class ClientAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'create_at']
    ordering = ['name']
    list_filter = ['create_at']
    search_fields = ['name']
    search_help_text = 'Поиск по полю Имя (name)'


class GoodsAdmin(admin.ModelAdmin):
    actions = [reset_amount]


class OrderAdmin(admin.ModelAdmin):
    """Список продуктов."""

    list_display = ['client_id', 'goods_id', 'price']

    fieldsets = [
        (
            'Товар',
            {
                'classes': ['collapse'],
                'description': 'Клиент и товар',
                'fields': ['client_id', 'goods_id'],
            },
        ),
        (
            'Цена',
            {
                'fields': ['price'],
            }
        ),
    ]


# Register your models here.
admin.site.register(Client, ClientAdmin)
admin.site.register(Goods, GoodsAdmin)
admin.site.register(Order, OrderAdmin)
