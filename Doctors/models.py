import datetime

from django.db import models

# Create your models here.


class Specialization(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Specialization'
        verbose_name_plural = 'Specializations'


class Doctor(models.Model):
    name = models.CharField(max_length=60)
    slug = models.SlugField(unique=True)
    specializations = models.ManyToManyField(Specialization)
    description = models.TextField(blank=True)
    date_of_birth = models.DateField()
    date_of_employment = models.DateField(default=datetime.date.today)

    def __str__(self):
        return self.name

    @property
    def work_experience(self):
        """
        Returns the number of days between the date of employment and today
        :return:
        """
        return (datetime.date.today() - self.date_of_employment).days

    work_experience.fget.short_description = "work experience (days)"

    class Meta:
        verbose_name = "Doctor"
        verbose_name_plural = "Doctors"
