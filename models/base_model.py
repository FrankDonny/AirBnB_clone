#!/usr/bin/python3
"""
This is the base class that defines the rest of the class
involved in the Airbnb_clone project
"""
import datetime
import uuid
from models import storage


class BaseModel:
    """The base class"""
    def __init__(self, *args, **kwargs):
        """
        initializing the base class
        args: multiple arguments to be passed
        kwargs: a key value pair of a dictionary argument
        """
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()
            storage.new(self)
        else:
            for ky, value in kwargs.items():
                if ky == "__class__":
                    continue
                if ky == "id":
                    self.id = value
                    setattr(self, ky, self.id)
                elif ky == "created_at" or ky == "updated_at":
                    value = datetime.datetime.now()
                    setattr(self, ky, value.strftime("%Y, %m, %d, %H, %M, %S"))
                else:
                    setattr(self, ky, value)

    def save(self):
        """
        This method updates the updated_at instance
        """
        self.updated_at = datetime.datetime.now()
        storage.save()

    def to_dict(self):
        """
        This method returns the dictionary representation of base class
        :return: _dict, the updated dictionary
        """
        _dict = self.__dict__.copy()
        add_dict = {
            "__class__": self.__class__.__name__,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat()
        }
        _dict.update(add_dict)
        return _dict

    def __str__(self):
        """
        :return: the string representation of the class
        """
        return f"[{__class__.__name__}] ({self.id}) {self.__dict__}"
