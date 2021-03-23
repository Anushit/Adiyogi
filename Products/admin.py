from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin

from .models import Product,Category


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'parent', 'status']
    search_fields = ['status']
    list_per_page = 5


class CategoryAdmin2(DraggableMPTTAdmin):
    mptt_indent_field = "title"
    list_display = ('tree_actions', 'indented_title',
                    'related_products_count', 'related_products_cumulative_count')
    list_display_links = ('indented_title',)

    def get_queryset(self, request):
        qs = super().get_queryset(request)

        # Add cumulative product count
        qs = Category.objects.add_related_count(
                qs,
                Product,
                'category',
                'products_cumulative_count',
                cumulative=True)

        # Add non cumulative product count
        qs = Category.objects.add_related_count(qs,
                 Product,
                 'category',
                 'products_count',
                 cumulative=False)
        return qs

    def related_products_count(self, instance):
        return instance.products_count
    related_products_count.short_description = 'Related products (for this specific category)'

    def related_products_cumulative_count(self, instance):
        return instance.products_cumulative_count
    related_products_cumulative_count.short_description = 'Related products (in tree)'

class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'title','category', 'image_tag', 'status']
    list_filter = ['category']
    search_fields = ['title']
    list_per_page = 5


admin.site.register(Product,ProductAdmin)
admin.site.register(Category,CategoryAdmin2)