from django.urls import path

from Doctors.views import DoctorsViewSet, SpecializationViewSet

urlpatterns = [
    path('doctors_list/', DoctorsViewSet.as_view({'get': 'list'})),
    path('doctors_details/<int:pk>/', DoctorsViewSet.as_view({'get': 'retrieve'})),
    path('specializations_list/', SpecializationViewSet.as_view({'get': 'list'})),
]
