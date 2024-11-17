#!/usr/bin/python3
"""Write a class BaseModel that defines all common
attributes/methods for other classes:"""
import uuid
from datetime import datetime


class BaseModel:
    """
    A base class that defines common attributes and methods
    for other classes.
    """
    def __init__(self, *args, **kwargs):
        """
        Initializes a new instance of BaseModel.
        Assigns a unique ID, and sets creation and update timestamps.
        """
        from models import storage
        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                if key in ("created_at", "updated_at"):
                    value = datetime.fromisoformat(value)
                setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            storage.new(self)

    def __str__(self):
        """
        Returns a string representation of the instance.
        Format: [<class name>] (<self.id>) <self.__dict__>
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """updates the public instance attribute
        updated_at with the current datetime"""

        from models import storage
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
        Returns a dictionary containing all keys/values of __dict__
        and adds the `__class__` key.
        Converts `created_at` and `updated_at` to ISO format strings.
        """
        dictionary = self.__dict__.copy()
        dictionary['__class__'] = self.__class__.__name__
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        return dictionary
