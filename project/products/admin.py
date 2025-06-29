from django.contrib import admin
from .models import Product, TestDate
# Register your models here.

class productAdmin(admin.ModelAdmin):
    list_display = ['name', 'content', 'price','category','active']
    list_display_links = ['price']
    list_editable = ['name','category','active']
    search_fields = ['name','content','price','category','active']
    list_filter = ['price']
    fields = ['name','price','active']

admin.site.register(Product, productAdmin)
admin.site.register(TestDate)
admin.site.site_header = 'Admin Panel'
admin.site.site_title = 'MohaSoGoodNoLove'