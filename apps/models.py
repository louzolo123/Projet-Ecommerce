from django.db import models
from pyexpat import model
from email.policy import default
from shortuuid.django_fields import ShortUUIDField
from usersauths.models import User
# for install ShortUUIDField
#pip install shortuuid let of genere identifiers
from django.utils.html import mark_safe

STATUS_CHOICE = {
    ("process" , "Processing"),
    ('Shipped' , 'Shipped'),
    ('delivered' , 'Delivered')
}
STATUS = {
    ("draft" , "Draft"),
    ('disable' , 'Disable'),
    ('rejected' , 'Rejected'),
    ('in_review' , 'In Review'),
    ('published' , 'Published'),
}
RATING = {
    ("1" , "⭐"),
    ("2" , "⭐⭐"),
    ("3" , "⭐⭐⭐"),
    ("4" , "⭐⭐⭐⭐"),
    ("5" , "⭐⭐⭐⭐⭐"),
}
def user_directory_path(instance , filename):
    return 'user_{0}/{1}'.format(instance.user.id, filename)
class Category(models.Model):
    categoryId = ShortUUIDField(unique=True , length=10, max_length=30 , prefix='cat' , alphabet='abcdefgh12345')
    title =models.CharField(max_length=255)
    image = models.ImageField(upload_to='category' , default='category.jpg')
    
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
    def category_image(self):
        return mark_safe ('<img src="%s" width="50" height="50" />' % (self.image.url))
    def __str__(self):
        return self.title
class Tags (models.Model):
    responses = models.CharField(choices = RATING , max_length = 1000000000 , default='⭐')
class Vendor(models.Model):
    vendorId = ShortUUIDField(unique=True , length=10, max_length=30 , prefix='ven' , alphabet='abcdefgh12345')
    title =models.CharField(max_length=255 )
    image = models.ImageField(upload_to=user_directory_path, default='vendor.jpg')
    description = models.TextField(max_length=1000 , null=True , blank=True  , default='I am amazing Vendor' )
    address =models.CharField(max_length=255 , default='Ngoyo')
    contact =models.CharField(max_length=255 , default='+242068195646')
    chat_resp_time =models.CharField(max_length=255 , default='100')
    shipping_on_time = models.CharField(max_length=255 , default='100')
    authentic_rating = models.CharField(max_length=255 , default='100')
    days_return = models.CharField(max_length=255 , default='100')
    warranty_period = models.CharField(max_length=255 , default='100')
    user = models.ForeignKey(User, on_delete = models.SET_NULL , null=True)
    date = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'Vendor'
        verbose_name_plural = 'Vendors'
    def vendor_image(self):
        return mark_safe ('<img src="%s" width="50" height="50" />' % (self.image.url))
    def __str__(self):
        return self.title
    
class Product(models.Model):
    productId = ShortUUIDField(unique=True , length=10, max_length=30  , alphabet='abcdefgh12345')
    title =models.CharField(max_length=255 , default='Fresh Product')
    image = models.ImageField(upload_to=user_directory_path, default='product.jpg')
    description = models.TextField(max_length=1000 , null=True , blank=True  , default='This is the product' )
    user = models.ForeignKey(User, on_delete = models.SET_NULL , null=True)
    category = models.ForeignKey(Category, on_delete = models.SET_NULL , null=True, related_name="category")
    vendor = models.ForeignKey(Vendor, on_delete = models.SET_NULL , null=True, related_name="vendor")
    
    price =  models.DecimalField(max_digits=99999999999999999 , decimal_places=2, default='1000.00')
    old_price = models.DecimalField(max_digits=99999999999999999 , decimal_places=2, default='1500.00')
    
    specifications = models.TextField(null=True, blank=True)
    products_status = models.CharField(choices=STATUS , max_length=10 , default='In_review')
    tags = models.CharField(Tags , max_length=10 , default="1")
    status = models.BooleanField(default=True)
    in_stock = models.BooleanField(default=True)
    featured =  models.BooleanField(default=False)
    digital =  models.BooleanField(default=False)
    sku = ShortUUIDField(unique=True , length=4, max_length=10 , prefix='sku' , alphabet='1234567890')
    date = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(null=True  , blank=True)
    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
    def product_image(self):
        return mark_safe ('<img src="%s" width="50" height="50" />' % (self.image.url))
    def __str__(self):
        return self.title
    def get_pourcentage(self):
        new_price = (self.price / self.old_price) * 100
        return new_price
    
class ProductImages(models.Model):
    image = models.ImageField(upload_to='product-image' , default='products.jpg')
    product = models.ForeignKey(Product , on_delete= models.SET_NULL , null=True, blank=True , related_name='p_image')
    date = models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name = 'Product-image'
        verbose_name_plural = 'Products-images'
class CartOrder(models.Model):
    user  = models.ForeignKey(User, blank=True, null=True , on_delete = models.CASCADE)
    price =  models.DecimalField(max_digits=99999999999999999 , decimal_places=2, default='1000.00')
    paid_status = models.BooleanField()
    order_date = models.DateTimeField()
    products_status = models.CharField(choices=STATUS_CHOICE , max_length=30 , default='Processing')
    class Meta:
        verbose_name = 'Cart Order'
        verbose_name_plural = 'Carts Orders'
        
class CartOrderItems(models.Model):
    order = models.ForeignKey(CartOrder , on_delete= models.CASCADE)
    product_status = models.CharField(max_length=200)
    image = models.ImageField(upload_to='cart-image')
    item = models.CharField(max_length=200)
    quantity = models.IntegerField(default=0)
    price =  models.DecimalField(max_digits=99999999999999999 , decimal_places=2, default='1000.00')

class Adress(models.Model):
    user = models.ForeignKey(User , on_delete=models.SET_NULL, null=True)
    adress = models.CharField(max_length=100 , null=True)
    status = models.BooleanField(default=False)
    
    def __str__(self):
        return self.adress
    
class WhisList(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL , null=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL , null=True)
    date = models.DateTimeField(auto_now_add=True)
    
    def __str(self):
        return self.product.title