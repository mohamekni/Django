from django.contrib import admin
from .models import Product, TestDate
# Register your models here.

admin.site.register(Product)
admin.site.register(TestDate)
admin.site.site_header = 'Admin Panel'
admin.site.site_title = 'MohaSoGoodNoLove'