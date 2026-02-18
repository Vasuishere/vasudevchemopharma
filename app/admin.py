from django.contrib import admin
from .models import ProductCategory, Product, ProductSpec


class ProductSpecInline(admin.TabularInline):
    model = ProductSpec
    extra = 1


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "icon", "order")
    list_filter = ("category",)
    search_fields = ("name", "description")
    inlines = [ProductSpecInline]


@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ("label", "slug", "show_in_overview", "order")
    prepopulated_fields = {"slug": ("label",)}
