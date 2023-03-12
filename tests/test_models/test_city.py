#!/usr/bin/python3
import unittest
from models.city import City
from models.base_model import BaseModel
import os
import pycodestyle


class TestUser(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """ fills user with data to test with at the start of the test """
        cls.cities = City()
        cls.cities.name = "Lagos"
        cls.cities.state_id = "lagos"

    @classmethod
    def tearDownClass(cls):
        """ removes all data created during test and deletes file.json if
            exists
        """
        del cls.cities
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_conformance(self):
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(['models/city.py'])
        self.assertEqual(result.total_errors, 0, "Fix pep8")

    def test_is_subclass(self):
        """ checks if the class is a subclass of BaseModel """
        self.assertTrue(issubclass(self.cities.__class__, BaseModel), True)

    def test_for_functions(self):
        self.assertIsNotNone(City.__doc__)

    def test_attribute_exist(self):
        self.assertTrue("id" in self.cities.__dict__)
        self.assertTrue("name" in self.cities.__dict__)
        self.assertTrue("created_at" in self.cities.__dict__)
        self.assertTrue("updated_at" in self.cities.__dict__)
        self.assertTrue("state_id" in self.cities.__dict__)

    def test_attrbutesAreStrings(self):
        self.assertEqual(type(self.cities.name), str)
        self.assertEqual(type(self.cities.state_id), str)

    def test_itSaves(self):
        self.cities.save()
        self.assertNotEqual(self.cities.created_at, self.cities.updated_at)

    def test_to_dict(self):
        self.assertTrue("to_dict" in dir(self.cities), True)


if __name__ == "__main__":
    unittest.main()
