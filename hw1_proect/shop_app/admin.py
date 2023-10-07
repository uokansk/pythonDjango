from django.contrib import admin

from .models import Client, Product, Order


class ClientAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone']
    ordering = ['-registered_at']
    list_filter = ['registered_at']
    search_fields = ['name', 'email', 'phone', 'address']
    search_help_text = 'Поиск клиентов по полям Имя, Email, Телефон, Адрес'
    readonly_fields = ['registered_at']
    fields = ['name', 'email', 'phone', 'address', 'registered_at']
    list_per_page = 10


@admin.action(description="Обнулить количество товаров")
def reset_quantity(modeladmin, request, queryset):
    queryset.update(quantity=0)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'quantity']
    ordering = ['-added_at']
    list_filter = ['price', 'added_at']
    search_fields = ['name', 'description']
    search_help_text = 'Поиск товаров по полям Название и Описание'
    actions = [reset_quantity]
    readonly_fields = ['added_at']
    list_per_page = 20
    fieldsets = [
        (
            'Основная информация',
            {
                'classes': ['wide'],
                'fields': ['name', 'description', 'image', 'added_at'],
            },
        ),
        (
            'Учёт',
            {
                'classes': ['collapse'],
                'fields': ['price', 'quantity'],
            }
        ),
    ]


class OrderAdmin(admin.ModelAdmin):
    list_display = ['created_at', 'client', 'total_amount']
    ordering = ['-created_at']
    list_filter = ['client', 'products']
    readonly_fields = ['total_amount', 'created_at']
    fields = ['client', 'products', 'total_amount', 'created_at']
    list_per_page = 10


admin.site.register(Client, ClientAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
