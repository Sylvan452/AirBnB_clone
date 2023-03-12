#!/usr/bin/python3
import unittest
from models.review import Review
from models.base_model import BaseModel
import os
import pycodestyle


class TestUser(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """ fills user with data to test with at the start of the test """
        cls.reviews = Review()
        cls.reviews.place_id = "Beverley"
        cls.reviews.user_id = "Pitous"
        cls.reviews.text = "Splendid"

    @classmethod
    def tearDownClass(cls):
        """ removes all data created during test and deletes file.json if
            exists
        """
        del cls.reviews
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_conformance(self):
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(['models/review.py'])
        self.assertEqual(result.total_errors, 0, "Fix pep8")

    def test_is_subclass(self):
        """ checks if the class is a subclass of BaseModel """
        self.assertTrue(issubclass(self.reviews.__class__, BaseModel), True)

    def test_for_functions(self):
        self.assertIsNotNone(Review.__doc__)

    def test_attribute_exist(self):
        self.assertTrue("id" in self.reviews.__dict__)
        self.assertTrue("place_id" in self.reviews.__dict__)
        self.assertTrue("created_at" in self.reviews.__dict__)
        self.assertTrue("updated_at" in self.reviews.__dict__)
        self.assertTrue("user_id" in self.reviews.__dict__)
        self.assertTrue("text" in self.reviews.__dict__)

    def test_attrbutesAreStrings(self):
        self.assertEqual(type(self.reviews.user_id), str)
        self.assertEqual(type(self.reviews.place_id), str)
        self.assertEqual(type(self.reviews.text), str)

    def test_itSaves(self):
        self.reviews.save()
        self.assertNotEqual(self.reviews.created_at, self.reviews.updated_at)

    def test_to_dict(self):
        self.assertTrue("to_dict" in dir(self.reviews), True)


if __name__ == "__main__":
    unittest.main()
