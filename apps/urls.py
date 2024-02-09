from django.urls import path
from .import views
app_name = 'apps'

urlpatterns = [
    path('index/' , views.index , name = 'index'),
    path('category/' , views.category_list , name='category'),
    path('displayCategoryOfProducts/<int:productCategory_id>' , views.display_list_category_of_product , name='displayCategoryOfProducts'),
    path('vendor/' , views.vendor_list , name='vendor'),
    path('vendorDetail/<int:vendor_id>' , views.vendor_detail , name='vendorDetail'),
    path('productDetail/<int:product_id>' , views.product_detail , name='productDetail'),
]
