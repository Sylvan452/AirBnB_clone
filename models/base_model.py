#!/usr/bin/python3
from uuid import uuid4
from datetime import datetime
import models

"""
    BaseModel- parent of all classes in this project
"""


class BaseModel():
    """
        Parent class for the Airbnb_clone project
        Methods:
          __init__(self, *args, **kwargs)
          __str__(self)
          __save__(self)
          to_dict(self)
    """

    def __init__(self, *args, **kwargs):
        """ Initializes the class with a random uuid, update/create dates """
        if kwargs:
            for key, val in kwargs.items():
                if key == "created_at":
                    self.created_at = datetime.strptime(kwargs["created_at"],
                                                        "%Y-%m-%dT%H:%M:%S.%f")
                elif key == "updated_at":
                    self.updated_at = datetime.strptime(kwargs["updated_at"],
                                                        "%Y-%m-%dT%H:%M:%S.%f")
                elif key == "__class__":
                    pass
                else:
                    setattr(self, key, val)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """ Returns string info about class """
        info = '[{}] ({}) {}'.format(self.__class__.__name__, self.id,
                                     self.__dict__)
        return info

    def save(self):
        """updates the public instance attribute updated_at with the current
           datetime
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """ returns a dictionary containing all keys/values of __dict__ of the
            instance"""
        new_dict = {}
        new_dict["__class__"] = self.__class__.__name__
        for key, val in self.__dict__.items():
            if isinstance(val, (datetime, )):
                new_dict[key] = val.isoformat()
            else:
                new_dict[key] = val
        return new_dict
