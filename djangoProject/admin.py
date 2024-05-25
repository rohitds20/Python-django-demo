from django.contrib import admin
from djangoProject.models import User, Product


#admin.site.register(User)
#admin.site.register(Product)
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    fields = ['username', 'name', 'email','address','age']
    list_display = ['id','username', 'name', 'email']
    search_fields = ['id','username', 'name']

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price','stock']
    search_fields = ['name']


