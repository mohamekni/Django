from django.contrib import admin
from .models import Female, Male, User, Product, Video, SimpleUser
# Register your models here.

admin.site.register(Female)
admin.site.register(Male)
admin.site.register(User)
admin.site.register(Product)
admin.site.register(Video)
admin.site.register(SimpleUser)