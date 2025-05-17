from django.contrib import admin

from .models import IMT,Dish,Category,catDietary,Dietary

admin.site.register(IMT)
admin.site.register(Dietary)
admin.site.register(Dish)
admin.site.register(catDietary)
admin.site.register(Category)

# Register your models here.
