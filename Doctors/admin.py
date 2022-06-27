import datetime

from django.contrib import admin
from django.db.models import F

from Doctors.models import Doctor, Specialization


@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('name', 'get_work_experience', 'slug')
    list_filter = ('specializations',)
    search_fields = ('name',)
    ordering = ('slug', 'name')

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        qs = qs.annotate(
            _work_experience=F('date_of_employment'),)
        return qs

    def get_work_experience(self, obj):
        return (datetime.date.today() - obj.date_of_employment).days
    get_work_experience.short_description = "work experience (days)"
    get_work_experience.admin_order_field = '_work_experience'


@admin.register(Specialization)
class SpecializationAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    search_fields = ('name',)

    ordering = ('slug', 'name',)
