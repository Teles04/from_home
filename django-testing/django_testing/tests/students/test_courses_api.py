import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.status import HTTP_201_CREATED, HTTP_200_OK
from rest_framework.test import APIClient, APITestCase

from students.models import Course


@pytest.mark.django_db
def test_course_create_one():
    client = APIClient()
    course = Course.objects.create(name='test')
    url = reverse('courses-list')

    resp = client.get(url)

    assert resp.status_code == HTTP_200_OK
    assert course.id
    assert course.name == 'test'


@pytest.mark.django_db
def test_course_create_list():
    client = APIClient()
    url = reverse('courses-list')
    course1 = Course.objects.create(name='test1')
    course2 = Course.objects.create(name='test2')
    resp = client.get(url)

    assert resp.status_code == HTTP_200_OK
    resp_json = resp.json()
    resp_ids = {r['id'] for r in resp_json}
    assert resp_ids == {course1.id, course2.id}




