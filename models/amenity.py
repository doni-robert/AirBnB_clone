#!/usr/bin/python3
"""Defines the Amenity class."""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    represents the amenity
    Attributes:
        name (str): the name of the amenity.
    """

    name = ""
