from rest_framework import generics, viewsets, status
from rest_framework.decorators import action
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response

from .models import Order, Company, Warehouse, CustomUser
from .permissions import IsInSameCompany
from .serializers import OrderDetailSerializer, FullCompanySerializer, \
    StandardCompanySerializer, OrderCreateSerializer, WarehouseSerializer, UserAddCompanySerializer



class OrderViewSet(viewsets.ModelViewSet):
    serializer_class = OrderCreateSerializer
    queryset = Order.objects.all()
    permission_classes = (IsAuthenticated,)
    http_method_names = ("get", "post")

    def create(self, request, *args, **kwargs):
        performer_company_id = request.data.get('performer_company')
        truck_id = request.data.get('truck')

        if not Company.objects.filter(id=performer_company_id, trucks__id=truck_id).exists():
            raise ValidationError(
                {'error': 'Performer company does not have the specified truck.'})

        return super().create(request, *args, **kwargs)

    def list(self, request, *args, **kwargs):
        if self.request.user.is_superuser:
            self.queryset = Order.objects.all()
        else:
            self.queryset = Order.objects.filter(company=self.request.user.company)

        return super().list(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        self.serializer_class = OrderDetailSerializer
        return super().retrieve(request, *args, **kwargs)


class CompanyGetView(generics.RetrieveAPIView):
    queryset = Company.objects.all()
    serializer_class = FullCompanySerializer


class WarehouseView(generics.ListCreateAPIView):
    serializer_class = WarehouseSerializer
    permission_classes = (IsAuthenticated, IsInSameCompany,)

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Warehouse.objects.all()
        return Warehouse.objects.filter(company=self.request.user.company)


class AddUserToCompanyView(generics.UpdateAPIView):
    serializer_class = UserAddCompanySerializer
    queryset = CustomUser.objects.all()
    permission_classes = (IsAuthenticated, IsAdminUser,)
