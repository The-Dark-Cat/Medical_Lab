import datetime
from pprint import pprint
from random import randint
from typing import List

from django.test import TestCase

from pydantic import BaseModel

from Doctors.models import Doctor, Specialization


class SpecializationPD(BaseModel):
    name: str
    slug: str
    description: str


class DoctorPD(BaseModel):
    name: str
    slug: str
    specializations: List[SpecializationPD]
    description: str
    date_of_birth: str
    date_of_employment: str
    work_experience: int


class DoctorsTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.setUpspecializations()
        cls.setUpDoctors()

    @classmethod
    def setUpspecializations(cls):
        specializations = []
        for _ in range(10):
            specializations.append(Specialization(name=f"Specialization {_}",
                                                  slug=f"specialization-{_}", description=f"Description {_}"))
        Specialization.objects.bulk_create(specializations)

    @classmethod
    def setUpDoctors(cls):
        doctors = []
        for _ in range(10):
            doctors.append(Doctor(name=f"Doctor {_}", slug=f"doctor-{_}", description=f"Description {_}",
                                  date_of_birth=datetime.date.today() - datetime.timedelta(days=_ *3),
                                  date_of_employment=datetime.date.today() - datetime.timedelta(days=_ *3)))
        Doctor.objects.bulk_create(doctors)
        for doctor in Doctor.objects.all():
            doctor.specializations.set(Specialization.objects.filter(id=randint(1, 10)))

    def test_get_doctors(self):
        response = self.client.get('/doctors/doctors_list/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['count'], 10)
        self.assertEqual(response.json()['results'][0]['name'], "Doctor 0")
        self.assertEqual(len(response.json()['results']), 2)

        doctors_pd = [DoctorPD(**doc) for doc in response.json()['results']]

    def test_get_specializations(self):
        response = self.client.get('/doctors/specializations_list/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['count'], 10)
        self.assertEqual(response.json()['results'][0]['name'], "Specialization 0")
        self.assertEqual(len(response.json()['results']), 10)

        specializations_pd = [SpecializationPD(**spec) for spec in response.json()['results']]
        self.assertEqual(specializations_pd[0].name, "Specialization 0")
        self.assertEqual(specializations_pd[0].slug, "specialization-0")
        self.assertEqual(specializations_pd[0].description, "Description 0")
        self.assertEqual(specializations_pd[1].name, "Specialization 1")
        self.assertEqual(specializations_pd[1].slug, "specialization-1")
        self.assertEqual(specializations_pd[1].description, "Description 1")

    def test_doc_filters(self):
        response = self.client.get('/doctors/doctors_list/?specialization_name=specialization-0')
        self.assertEqual(response.status_code, 200)
        for doc in response.json()['results']:
            for spec in doc['specializations']:
                self.assertEqual(spec['name'], "specialization-0")

        response = self.client.get('/doctors/doctors_list/?name=Doctor 0')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['results'][0]['name'], "Doctor 0")
        self.assertEqual(response.json()['count'], 1)

    def test_doc_ordering(self):
        response = self.client.get('/doctors/doctors_list/?ordering=name&page_size=10')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['results'][0]['name'], "Doctor 0")
        self.assertEqual(response.json()['results'][1]['name'], "Doctor 1")
        self.assertEqual(response.json()['results'][2]['name'], "Doctor 2")
        self.assertEqual(response.json()['results'][3]['name'], "Doctor 3")
        self.assertEqual(response.json()['results'][4]['name'], "Doctor 4")
        self.assertEqual(response.json()['results'][5]['name'], "Doctor 5")
        self.assertEqual(response.json()['results'][6]['name'], "Doctor 6")
        self.assertEqual(response.json()['results'][7]['name'], "Doctor 7")
        self.assertEqual(response.json()['results'][8]['name'], "Doctor 8")
        self.assertEqual(response.json()['results'][9]['name'], "Doctor 9")

        response = self.client.get('/doctors/doctors_list/?ordering=-work_experience&page_size=10')
        self.assertEqual(response.status_code, 200)
        max_experience = 0
        for doc in response.json()['results']:
            self.assertGreaterEqual(doc['work_experience'], max_experience)
            max_experience = doc['work_experience']



