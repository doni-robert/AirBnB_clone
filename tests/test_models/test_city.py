#!/usr/bin/python3
"""
Unittests for the class City
"""
import unittest
import models
import os
from datetime import datetime
from models.city import City
import pep8


class TestCity(unittest.TestCase):
    """ Tests to check the City class """

    new = City()

    def test_existance(self):
        """tests the class existance"""
        self.assertEqual(str(type(self.new)), "<class 'models.city.City'>")

    def test_inheritance(self):
        """test if city is a subclass of BaseModel"""
        self.assertTrue(self.new, City)

    def test_attributes(self):
        """ test the class's attributes """
        self.assertTrue(hasattr(self.new, 'id'))
        self.assertTrue(hasattr(self.new, 'name'))
        self.assertTrue(hasattr(self.new, 'state_id'))
        self.assertTrue(hasattr(self.new, 'created_at'))
        self.assertTrue(hasattr(self.new, 'updated_at'))


if __name__ == '__main__':
    unittest.main()
