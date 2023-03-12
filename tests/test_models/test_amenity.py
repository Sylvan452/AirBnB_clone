#!/usr/bin/python3
import unittest
from models.amenity import Amenity
from models.base_model import BaseModel
import os
import pycodestyle


class TestUser(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """ fills user with data to test with at the start of the test """
        cls.amenity1 = Amenity()
        cls.amenity1.name = "shower"

    @classmethod
    def tearDownClass(cls):
        """ removes all data created during test and deletes file.json if
            exists
        """
        del cls.amenity1
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_conformance(self):
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(['models/amenity.py'])
        self.assertEqual(result.total_errors, 0, "Fix pep8")

    def test_is_subclass(self):
        """ checks if the class is a subclass of BaseModel """
        self.assertTrue(issubclass(self.amenity1.__class__, BaseModel), True)

    def test_for_functions(self):
        self.assertIsNotNone(Amenity.__doc__)

    def test_attribute_exist(self):
        self.assertTrue("id" in self.amenity1.__dict__)
        self.assertTrue("name" in self.amenity1.__dict__)
        self.assertTrue("created_at" in self.amenity1.__dict__)
        self.assertTrue("updated_at" in self.amenity1.__dict__)

    def test_attrbutesAreStrings(self):
        self.assertEqual(type(self.amenity1.name), str)

    def test_itSaves(self):
        self.amenity1.save()
        self.assertNotEqual(self.amenity1.created_at, self.amenity1.updated_at)

    def test_to_dict(self):
        self.assertTrue("to_dict" in dir(self.amenity1), True)


if __name__ == "__main__":
    unittest.main()
