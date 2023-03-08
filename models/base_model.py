#!/usr/bin/python3
from uuid import uuid4
from datetime import datetime

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
            for key, val in kwargs.item():
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
