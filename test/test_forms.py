from django.contrib.auth import get_user_model
from django.test import TestCase

from taxi.forms import (
    CarModelSearchForm,
    ManufacturerNameSearchForm,
    DriverLicenseUpdateForm,
    DriverUsernameSearchForm,
    DriverCreationForm
)
from taxi.models import Manufacturer


class TestCarForms(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="new_driver1",
            password="root1234",
        )
        self.client.force_login(self.user)

        self.manufacturer = Manufacturer.objects.create(
            name="Manufacture Test", country="China"
        )

    def test_car_search_form_with_arg(self):
        form_data = {
            "model": "X3",
        }
        form = CarModelSearchForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_car_search_form_without_arg(self):
        form_data = {
            "model": "",
        }
        form = CarModelSearchForm(data=form_data)
        self.assertTrue(form.is_valid())


class TestManufacturerForms(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="new_driver1",
            password="root1234",
        )
        self.client.force_login(self.user)

        self.manufacturer = Manufacturer.objects.create(
            name="Manufacture Test", country="China"
        )

    def test_manufacturer_search_form_with_arg(self):
        form_data = {
            "name": "Manufacture Test",
        }
        form = ManufacturerNameSearchForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_manufacturer_search_form_without_arg(self):
        form_data = {
            "name": "",
        }
        form = ManufacturerNameSearchForm(data=form_data)
        self.assertTrue(form.is_valid())


class TestDriverForms(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="new_driver1",
            password="root1234",
        )
        self.client.force_login(self.user)

        self.manufacturer = Manufacturer.objects.create(
            name="Manufacture Test", country="China"
        )

    def test_driver_form(self):
        form_data = {
            "username": "another_driver",
            "license_number": "HRN84739",
            "password1": "Root1234",
            "password2": "Root1234"
        }
        form = DriverCreationForm(form_data)
        self.assertTrue(form.is_valid())

    def test_driver_search_form_with_arg(self):
        form_data = {
            "username": "new_driver",
        }
        form = DriverUsernameSearchForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_update_license_form_incorrect_num(self):
        form_data = {"license_number": "HrN8473"}
        form = DriverLicenseUpdateForm(form_data)
        self.assertEqual(form.is_valid(), False)

    def test_driver_search_form_without_arg(self):
        form_data = {
            "username": "",
        }
        form = DriverUsernameSearchForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_update_license_form_correct_num(self):
        form_data = {"license_number": "HRN84739"}
        form = DriverLicenseUpdateForm(form_data)
        self.assertTrue(form.is_valid())
