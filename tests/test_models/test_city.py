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

   def test_pep8_conformance_city(self):
        """Test that we conform to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/city.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

if __name__ == '__main__':
    unittest.main()
