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

    def serialize_Place(self, obj):
        """Serialize a Place object to a dictionary."""
        data = obj.to_dict()
        return data
    
    def deserialize_Place(self, data):
        """Deserialize a dictionary to a Place object."""
        obj = Place(**data)
        return obj

    def serialize_State(self, obj):
        """Serialize a Place object to a dictionary."""
        obj_dic = obj.to_dict()
        return obj_dic

    def deserialize_State(self, data):
        """Deserialize a dictionary to a Place object."""
        obj = State(**obj_dic)
        return obj

    def serialize_City(self, obj):
        """Serialize a Place object to a dictionary."""
        obj_dic = obj.to_dict()
        return obj_dic

    def deserialize_City(self, obj_dic):
        """Deserialize a dictionary to a Place object."""
        obj = City(**obj_dic)
        return obj

    def serialize_Amenity(self, obj):
        """Serialize a Place object to a dictionary."""
        obj_dic = obj.to_dict()
        return obj_dic

    def deserialize_Amenity(self, obj_dic):
        """Deserialize a dictionary to a Place object."""
        obj = Amenity(**obj_dic)
        return obj

    def serialize_Review(self, obj):
        """Serialize a Place object to a dictionary."""
        obj_dic = obj.to_dict()
        return obj_dic

    def deserialize_Review(self, obj_dic):
        """Deserialize a dictionary to a Place object."""
        obj = Review(**obj_dic)
        return obj

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
            classname = key.split('.')[0]
            if classname == 'Place':
                obj_dic[key] = self.serialize_Place(value)
            elif classname == 'State':
                obj_dic[key] = self.serialize_State(value)
            elif classname == 'City':
                obj_dic[key] = self.serialize_City(value)
            elif classname == 'Amenity':
                obj_dic[key] = self.serialize_Amenity(value)
            elif classname == 'Review':
                obj_dic[key] = self.serialize_Review(value)
            else:
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
