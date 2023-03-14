#!/usr/bin/python3
""" unittest for Filestorage"""
import unittest
import os
import pycodestyle
import json
from models.base_model import BaseModel
from models.place import Place
from models.user import User
from models.review import Review
from models.city import City
from models.state import State
from models.amenity import Amenity
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """testing file storage"""

    @classmethod
    def setUpClass(cls):
        cls.state = State()
        cls.state.name = "Lagos"

    @classmethod
    def tearDownClass(cls):
        del cls.state

    def teardown(self):
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_conformance(self):
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(['models/engine/file_storage.py'])
        self.assertEqual(result.total_errors, 0, "fix pep8")

    def test_all(self):
        """ test the all method"""
        storage = FileStorage()
        instance_dict = storage.all()
        self.assertIsNotNone(instance_dict)
        self.assertEqual(type(instance_dict), dict)
        self.assertIs(instance_dict, storage._FileStorage__objects)

    def test_new(self):
        n_storage = FileStorage()
        instance_dict = n_storage.all()
        my_user = User()
        my_user.id = "20383"
        my_user.name = "Sean"
        n_storage.new(my_user)
        key = my_user.__class__.__name__ + "." + str(my_user.id)
        self.assertIsNotNone(instance_dict[key])

    def test_reload(self):
        r_storage = FileStorage()
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass
        with open("file.json", "w") as file:
            file.write("{}")
        self.assertIs(r_storage.reload(), None)

    def test_save(self):
        s_storage = FileStorage()
        new_city = City()
        new_city.state_id = "ABuja"
        new_city.name = "Zembo"
        s_storage.new(new_city)
        s_storage.save()
        with open("file.json", 'r') as f:
            data = json.load(f)
            self.assertIn('City.{}'.format(new_city.id), data)
            self.assertEqual(data['City.{}'.format(new_city.id)],
                             new_city.to_dict())
