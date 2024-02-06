from django.shortcuts import render
from .models  import Product , ProductImages , CartOrder , CartOrderItems , Category , Vendor
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def index(request):
    products = Product.objects.order_by('-id').all()
    context = {
        'products' : products
    }
    return render(request , 'apps/index.html' , context)
@login_required
def category_list(request):
    categories = Category.objects.all()
    context = {
        'categories' : categories
    }
    return render(request , 'apps/category_list.html', context)
@login_required
def display_list_category_of_product(request , productCategory_id):
    category = Category.objects.get(id=productCategory_id)
    products = Product.objects.filter(products_status = 'published' , category = category)
    products_count = products.count()
    context = {
        'category' : category, 
        'products' : products,
        'products_count' : products_count
    }
    return render(request, 'apps/displayCategoryOfProduct.html', context)
@login_required
def vendor_list(request):
    vendors = Vendor.objects.all()
    vendors_count = vendors.count()
    context = {
        'vendor':vendors,
        'vendors_count' : vendors_count
    }
    return render(request , 'apps/listVendors.html', context)

@login_required
def vendor_detail(request , vendor_id):
    vendors = Vendor.objects.get(id=vendor_id)
    context = {
        "vendors": vendors
    }
    return render(request , 'apps/vendorDetail.html', context)