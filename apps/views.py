from django.shortcuts import render
from .models  import Product , ProductImages , CartOrder , CartOrderItems , Category , Vendor
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def index(request):
    products = Product.objects.order_by('-id').all()
    category = Category.objects.order_by('-id').all()
    product = Product.objects.all()[:3]
    context = {
        'products' : products,
        'category' : category,
        'product' : product
    }
    return render(request , 'apps/index.html' , context)
@login_required
def category_list(request):
    categories = Category.objects.all()
    product = Product.objects.all()[:3]
    context = {
        'categories' : categories,
        'product' : product
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
        'vendors_count' : vendors_count,
        
        
    }
    return render(request , 'apps/listVendors.html', context)

@login_required
def vendor_detail(request , vendor_id):
    vendor = Vendor.objects.get(id=vendor_id)
    products = Product.objects.filter(vendor = vendor , products_status = 'published')
    product = Product.objects.all()[:3]
    category = Category.objects.order_by('-id').all()
    context = {
        "vendor": vendor,
        'products' : products,
        'product' : product,
        'category' : category,
    }
    return render(request , 'apps/vendorDetail.html', context)
@login_required
def product_detail(request , product_id):
    product = Product.objects.get(id=product_id)
    category = Category.objects.order_by('-id').all()
    products = Product.objects.all()[:5]
    p_image = product.p_images.all()
    context  = {
        'product': product,
        'category' : category,
        'products' : products,
        'p_images': p_image,
    }
    return render(request , 'apps/productDetail.html', context)
