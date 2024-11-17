#!/usr/bin/python3
"""
Module for FileStorage class.
Handles serialization of objects to JSON and deserialization back to objects.
"""
import json


class FileStorage:
    """
    Serializes instances to a JSON file and
    seserializes JSON file to instances.
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns the dictionary __objects.
        """
        return self.__objects

    def new(self, obj):
        """
        Sets a new object in __objects with the key <obj class name>.id.
        """
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """
        Serializes __objects to the JSON file (__file_path).
        """
        obj_dict = {key: obj.to_dict() for key, obj in self.__objects.items()}
        with open(self.__file_path, 'w') as json_file:
            json.dump(obj_dict, json_file)

    def reload(self):
        """
        Deserializes the JSON file (__file_path)
        to __objects, if the file exists.
        """
        from models.base_model import BaseModel
        try:
            with open(self.__file_path, 'r') as json_file:
                obj_dict = json.load(json_file)
                for key, value in obj_dict.items():
                    self.__objects[key] = BaseModel(**value)
        except FileNotFoundError:
            pass
