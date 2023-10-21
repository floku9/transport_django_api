from django.db import models
from django.contrib.auth.models import AbstractUser

class Company(models.Model):
    name = models.CharField(max_length=255)
    contact_number = models.CharField(max_length=11)
    trucks = models.ManyToManyField('Truck', blank=True, through="CompanyTruck")

    class Meta:
        db_table = "companies"


class User(models.Model):
    login = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)


class Warehouse(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)


class Truck(models.Model):
    model = models.CharField(max_length=255)
    lifting_capacity = models.DecimalField(max_digits=10, decimal_places=2)


class CustomUser(AbstractUser):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True, blank=True)


class Order(models.Model):
    starting_warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE,
                                           related_name="starting_warehouse")
    destination_warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE,
                                              related_name="destination_warehouse")
    performer_company = models.ForeignKey(Company, on_delete=models.CASCADE)
    truck = models.ForeignKey(Truck, on_delete=models.CASCADE)
    goods = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)


class CompanyTruck(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    truck = models.ForeignKey(Truck, on_delete=models.CASCADE)
