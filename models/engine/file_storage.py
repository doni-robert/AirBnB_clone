#!/usr/bin/python3
"""Defines the FileStorage class."""
import json
from models.base_model import BaseModel
from models.user import User
from json import load
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.place import Place
from models.city import City
from models.review import Review
from models.state import State


class FileStorage:
    """Represent a class FileStorage that serializes instances to a JSON file
    and deserializes JSON file to instances.

    Attributes:
        __file_path (str): The name of the file to save objects to.
        __objects (dict): A dictionary of objects.
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ Return the dictionary __objects """
        return self.__objects

    def new(self, obj):
        """ Set in __objects obj with key <obj_class_name>.id """
        key = obj.__class__.__name__ + "." + obj.id
        self.__objects[key] = obj

    def save(self):
        """ Serialize obj dictionaries to json file(__file_path) """
        obj_dic = {}

        for key, value in self.__objects.items():
            obj_dic[key] = value.to_dict()
        with open(self.__file_path, 'w', encoding="UTF-8") as f:
            json.dump(obj_dic, f)

    def reload(self):
        """
        deserializes the JSON file to __objects, only if the JSON file exists ;
        otherwise, does nothing.
        """
        try:
            with open(self.__file_path, "r", encoding="UTF-8") as f:
                json_dic = load(f)
            for obj in json_dic.values():
                cls_name = obj["__class__"]
                del obj["__class__"]
                self.new(eval(cls_name)(**obj))
        except FileNotFoundError:
            pass
