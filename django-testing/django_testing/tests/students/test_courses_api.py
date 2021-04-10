from django.urls import reverse
from model_bakery import baker
from rest_framework.status import HTTP_201_CREATED, HTTP_200_OK, HTTP_204_NO_CONTENT

from students.filters import CourseFilter
from students.models import Course

import pytest


@pytest.mark.django_db
def test_course_create_one(api_client, course_factory):
    course = course_factory(name="test")
    url = reverse('courses-detail', args=(course.id, ))

    resp = api_client.get(url)

    assert resp.status_code == HTTP_200_OK
    assert course.name == 'test'


@pytest.mark.django_db
def test_course_create_list(api_client, course_factory):
    url = reverse('courses-list')
    course1 = course_factory()
    course2 = course_factory()

    resp = api_client.get(url)

    assert resp.status_code == HTTP_200_OK
    resp_json = resp.json()
    resp_ids = {r['id'] for r in resp_json}
    assert resp_ids == {course1.id, course2.id}


@pytest.mark.django_db
def test_course_filter_id():
    course1 = baker.make("students.Course")
    filter_id = CourseFilter

    resp = filter_id(course1.id)

    assert resp.data


@pytest.mark.django_db
def test_course_filter_name():
    course1 = baker.make("students.Course")
    filter_id = CourseFilter

    resp = filter_id(course1.name)

    assert resp.data


@pytest.mark.django_db
def test_course_create(api_client):
    url = reverse("courses-list")
    payload = {"name": "test", "student": [], }

    resp = api_client.post(url, payload, format="json")

    assert resp.status_code == HTTP_201_CREATED
    assert Course.objects.count() == 1


@pytest.mark.django_db
def test_course_create(api_client, course_factory):
    course = course_factory(name="test")
    url = reverse('courses-detail', args=(course.id, ))
    data = {"name": "test1"}

    resp = api_client.put(url, data, format="json")

    assert resp.status_code == HTTP_200_OK
    assert Course.objects.get(name='test1')
    assert Course.objects.count() == 1


@pytest.mark.django_db
def test_course_delete(api_client, course_factory):
    course = course_factory(name="test")
    url = reverse('courses-detail', args=(course.id, ))

    resp = api_client.delete(url)

    assert resp.status_code == HTTP_204_NO_CONTENT
