from django.contrib import admin
from .models import User, ContactUs , Profile

# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass
@admin.register(ContactUs)
class ContactUsAdmin(admin.ModelAdmin):
    pass
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['full_name' , 'bio']