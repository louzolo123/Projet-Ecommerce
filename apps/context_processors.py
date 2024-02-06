from .models  import Product , ProductImages , CartOrder , CartOrderItems , Category , Vendor
from django.contrib.auth.decorators import login_required
def default(request):
    categories  = Category.objects.all()
    return {
        'categories': categories
    }