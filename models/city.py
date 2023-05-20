#!/usr/bin/python3
"""Defines the City class."""
from models.base_model import BaseModel


class City(BaseModel):
    """
    represents the City

    Attributes:
        name (str): the City name
    """

    state_id = ""
    name = ""
