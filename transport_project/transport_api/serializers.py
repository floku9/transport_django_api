from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import Company, Warehouse, Truck, Order


class BaseCompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['id']


class StandardCompanySerializer(serializers.ModelSerializer):
    class Meta(BaseCompanySerializer.Meta):
        fields = BaseCompanySerializer.Meta.fields + ['name', 'contact_number']


class TruckSerializer(serializers.ModelSerializer):
    class Meta:
        model = Truck
        fields = ('id', 'model', 'lifting_capacity')


class WarehouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Warehouse
        fields = ('id', 'name', 'address')


class FullCompanySerializer(serializers.ModelSerializer):
    trucks = TruckSerializer(many=True, read_only=True)
    warehouses = WarehouseSerializer(many=True, source='warehouse_set', read_only=True)

    class Meta(StandardCompanySerializer.Meta):
        fields = StandardCompanySerializer.Meta.fields + ['trucks', 'warehouses']


class OrderDetailSerializer(serializers.ModelSerializer):
    truck = TruckSerializer()
    starting_warehouse = WarehouseSerializer()
    destination_warehouse = WarehouseSerializer()
    performer_company = StandardCompanySerializer()

    class Meta:
        model = Order
        fields = '__all__'


class OrderCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = '__all__'
