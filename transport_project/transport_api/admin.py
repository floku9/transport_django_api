from django.contrib import admin
from .models import Company, Warehouse, Truck, Order, CustomUser, CompanyTruck

admin.site.register(Company)
admin.site.register(Warehouse)
admin.site.register(Truck)
admin.site.register(Order)
admin.site.register(CustomUser)
admin.site.register(CompanyTruck)
