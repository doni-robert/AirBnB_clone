#!/usr/bin/env python3
""" Defines the class BaseModel """

from uuid import uuid4
from datetime import datetime

class BaseModel:
    """ Represents a BaseModel with common attributes for other classes"""
    def __init__(self):
        """ Initialize a new instance of BaseModel """
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()

    def __str__(self):
        """ Prints a class representation of class name, id and dictionary """
        """ class_name = self.__class__.__name__"""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """ Updates the public instance attribute 'updated_at' """
        self.updated_at = datetime.today()

    def to_dict(self):
        """ Returns a dictionary containing the base model instance """
        new_dict = self.__dict__.copy()
        new_dict["__class__"] = self.__class__.__name__
        new_dict["created_at"] = self.created_at.isoformat()
        new_dict["updated_at"] = self.updated_at.isoformat()

        return new_dict
