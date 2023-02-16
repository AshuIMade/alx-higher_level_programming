#!/usr/bin/python3
"""defines unittests for rectangle.py"""

import io
import sys
import unittest
from models.base import Base
from models.rectangle import Rectangle

class TestRectangle_instantiation(unittest.TestCase):
    """test cases for Rectangle class"""

    def test_rectangle_is_base(self):
        self.assertIsInstance(Rectangle(10, 2), Base)

    def test_no_args(self):
        with self.assertRaises(TypeError):
            Rectangle()

    def test_one_arg(self):
        with self.assertRaises(TypeError):
            Rectangle(1)
