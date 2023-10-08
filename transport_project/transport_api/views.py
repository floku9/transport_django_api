from rest_framework import generics, viewsets, status
from rest_framework.decorators import action
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response

from .models import Order, Company
from .serializers import OrderDetailSerializer, FullCompanySerializer, \
    StandardCompanySerializer, OrderCreateSerializer


class OrderDetailView(generics.RetrieveAPIView):
    serializer_class = OrderDetailSerializer
    queryset = Order.objects.all()


class OrderCreateView(generics.CreateAPIView):
    serializer_class = OrderCreateSerializer
    queryset = Order.objects.all()

    def post(self, request, *args, **kwargs):
        performer_company_id = request.data.get('performer_company')
        truck_id = request.data.get('truck')

        if not Company.objects.filter(id=performer_company_id, trucks__id=truck_id).exists():
            raise ValidationError(
                {'error': 'Performer company does not have the specified truck.'})

        return self.create(request, *args, **kwargs)

class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = StandardCompanySerializer
    http_method_names = ['get', 'head']

    @action(detail=True, methods=['GET'])
    def get_info(self, request, pk=None):
        company = self.get_object()
        serializer = FullCompanySerializer(company)
        return Response(serializer.data)

