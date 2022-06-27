import datetime

import django_filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import PageNumberPagination

from rest_framework.viewsets import ReadOnlyModelViewSet

from Doctors.models import Doctor, Specialization
from Doctors.serializers import DoctorSerializer, SpecializationSerializer


class DoctorPagination(PageNumberPagination):
    page_size = 2
    page_size_query_param = 'page_size'
    max_page_size = 15


class DoctorFilter(django_filters.FilterSet):
    specialization_name = django_filters.CharFilter(method='_specialization_name')
    min_work_experience = django_filters.NumberFilter(method='_min_work_experience')

    ordering = django_filters.OrderingFilter(
        fields=('date_of_birth', 'name', 'work_experience'),
        method='_ordering'
    )

    def _ordering(self, queryset, name, value):
        if 'work_experience' in value:
            return queryset.order_by('date_of_employment')
        elif '-work_experience' in value:
            return queryset.order_by('-date_of_employment')
        return queryset.order_by(*value)

    class Meta:
        model = Doctor
        fields = ['name', 'date_of_birth', 'date_of_employment', 'specializations']

    def _specialization_name(self, queryset, name, value):
        return queryset.filter(specializations__name=value)

    def _min_work_experience(self, queryset, name, value):
        return queryset.filter(date_of_employment__lte=datetime.date.today() - datetime.timedelta(days=int(value)))


class DoctorsViewSet(ReadOnlyModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    pagination_class = DoctorPagination
    filter_backends = (DjangoFilterBackend,)
    filterset_class = DoctorFilter
    ordering = ('id', 'name',)

    class Meta:
        model = Doctor
        fields = '__all__'


class DefaultPagination(PageNumberPagination):
    page_size = 30
    page_size_query_param = 'page_size'
    max_page_size = 100


class SpecializationViewSet(ReadOnlyModelViewSet):
    queryset = Specialization.objects.all()
    serializer_class = SpecializationSerializer
    pagination_class = DefaultPagination

    class Meta:
        model = Specialization
        fields = '__all__'
        ordering = ('name',)
