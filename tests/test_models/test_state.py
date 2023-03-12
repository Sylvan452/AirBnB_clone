#!/usr/bin/python3
import unittest
from models.state import State
from models.base_model import BaseModel
import os
import pycodestyle


class TestUser(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """ fills user with data to test with at the start of the test """
        cls.states = State()
        cls.states.name = "Beverley Hills"

    @classmethod
    def tearDownClass(cls):
        """ removes all data created during test and deletes file.json if
            exists
        """
        del cls.states
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_conformance(self):
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(['models/state.py'])
        self.assertEqual(result.total_errors, 0, "Fix pep8")

    def test_is_subclass(self):
        """ checks if the class is a subclass of BaseModel """
        self.assertTrue(issubclass(self.states.__class__, BaseModel), True)

    def test_for_functions(self):
        self.assertIsNotNone(State.__doc__)

    def test_attribute_exist(self):
        self.assertTrue("id" in self.states.__dict__)
        self.assertTrue("name" in self.states.__dict__)
        self.assertTrue("created_at" in self.states.__dict__)
        self.assertTrue("updated_at" in self.states.__dict__)

    def test_attrbutesAreStrings(self):
        self.assertEqual(type(self.states.name), str)

    def test_itSaves(self):
        self.states.save()
        self.assertNotEqual(self.states.created_at, self.states.updated_at)

    def test_to_dict(self):
        self.assertTrue("to_dict" in dir(self.states), True)


if __name__ == "__main__":
    unittest.main()
