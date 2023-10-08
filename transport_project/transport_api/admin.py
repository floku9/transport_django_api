from django.contrib import admin
from .models import Company, Warehouse, Truck, Order

admin.site.register(Company)
admin.site.register(Warehouse)
admin.site.register(Truck)
admin.site.register(Order)
