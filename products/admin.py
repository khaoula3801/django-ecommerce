from django.contrib import admin
from .models import Category, Product, Comment, Order, OrderItem

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')
    search_fields = ('name',)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock', 'category', 'created_at')
    list_filter = ('category',)
    search_fields = ('name', 'description')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('product', 'user', 'created_at')
    search_fields = ('product__name', 'user__username', 'content')


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0
    readonly_fields = ('product_name', 'price', 'quantity')


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'total', 'payment_method', 'status', 'created_at')
    list_filter = ('status', 'payment_method', 'created_at')
    inlines = [OrderItemInline]