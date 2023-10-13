from django.contrib import admin
from .models import Client, Product, Order



@admin.action(description="Сбросить количество в ноль")
def reset_quantity(modeladmin, request, queryset):
    queryset.update(quantity=0)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'quantity']
    ordering = ['price', '-quantity']
    list_filter = ['added_at', 'price']
    search_fields = ['description']
    search_help_text = 'Поиск по полю Описание продукта (description)'
    actions = [reset_quantity]

    """Отдельный продукт."""
    fields = ['name', 'description', 'added_at', 'price', 'quantity']
    readonly_fields = ['added_at', 'price']


admin.site.register(Client)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order)
