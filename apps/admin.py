from django.contrib import admin
from apps.models import Product , ProductImages , Tags , CartOrder , CartOrderItems , Category , Vendor 


class ProductImagesAdmin(admin.TabularInline):
    model = ProductImages
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImagesAdmin]
    list_display = ['user' , 'title' , 'product_image' , 'price' , 'category' , 'vendor' , 'tags', 'featured' , ]

@admin.register(Category)
class CatgeoryAdmin(admin.ModelAdmin):
    list_display = ['title' , 'image']
    
@admin.register(Vendor)
class VendorAdmin(admin.ModelAdmin):
    list_display = ['title' , 'image']

@admin.register(CartOrder)
class CartOrderAdmin(admin.ModelAdmin):
    list_display = ['user' , 'price' , 'paid_status' , 'order_date'  , 'products_status']

@admin.register(CartOrderItems)
class CartOrderItemsAdmin(admin.ModelAdmin):
    list_display = ['order' , 'item' , 'image' , 'quantity' , 'price' ]

