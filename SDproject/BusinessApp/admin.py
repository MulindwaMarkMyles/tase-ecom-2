from django.contrib import admin
from .models import Business,Product,Service,Feedback


class BusinessAdmin(admin.ModelAdmin):
    pass
admin.site.register(Business, BusinessAdmin)

class ProductAdmin(admin.ModelAdmin):
    pass
admin.site.register(Product, ProductAdmin)

class ServiceAdmin(admin.ModelAdmin):
    pass
admin.site.register(Service, ServiceAdmin)

class FeedbackAdmin(admin.ModelAdmin):
    pass
admin.site.register(Feedback, FeedbackAdmin)

