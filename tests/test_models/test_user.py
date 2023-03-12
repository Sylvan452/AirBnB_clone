#!/usr/bin/python3
import unittest
from models.user import User
from models.base_model import BaseModel
import os
import pycodestyle


class TestUser(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """ fills user with data to test with at the start of the test """
        cls.my_user = User()
        cls.my_user.first_name = "User1"
        cls.my_user.last_name = "Alx"
        cls.my_user.email = "user1@alx.com"
        cls.my_user.password = "root"

    @classmethod
    def tearDownClass(cls):
        """ removes all data created during test and deletes file.json if
            exists
        """
        del cls.my_user
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_conformance(self):
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(['models/user.py'])
        self.assertEqual(result.total_errors, 0, "Fix pep8")
    
    def test_is_subclass(self):
        """ checks if the class is a subclass of BaseModel """
        self.assertTrue(issubclass(self.my_user.__class__, BaseModel), True)

    def test_for_functions(self):
        self.assertIsNotNone(User.__doc__)

    def test_attribute_exist(self):
        self.assertTrue("email" in self.my_user.__dict__)
        self.assertTrue("id" in self.my_user.__dict__)
        self.assertTrue("created_at" in self.my_user.__dict__)
        self.assertTrue("password" in self.my_user.__dict__)
        self.assertTrue("updated_at" in self.my_user.__dict__)
        self.assertTrue("first_name" in self.my_user.__dict__)
        self.assertTrue("last_name" in self.my_user.__dict__)

    def test_attrbutesAreStrings(self):
        self.assertEqual(type(self.my_user.email), str)
        self.assertEqual(type(self.my_user.password), str)
        self.assertEqual(type(self.my_user.first_name), str)
        self.assertEqual(type(self.my_user.last_name), str)

    def test_itSaves(self):
        self.my_user.save()
        self.assertNotEqual(self.my_user.created_at, self.my_user.updated_at)

    def test_to_dict(self):
        self.assertTrue("to_dict" in dir(self.my_user), True)


if __name__ == "__main__":
    unittest.main()

