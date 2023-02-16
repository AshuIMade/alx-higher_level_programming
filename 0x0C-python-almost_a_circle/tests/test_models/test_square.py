#!/usr/bin/python3
"""defines unittest for Square class"""

import io
import sys
import unittest
from models.base import Base
from models.square import Square


class TestSquare_instantiation(unittest.TestCase):
    """unittests for Square class"""

    def test_is_base(self):
        self.assertIsInstance(Square(10), Base)

    def test_is_rectangle(self):
        self.assertIsInstance(Square(10), Square)

    def test_no_args(self):
        with self.assertRaises(TypeError):
            Square()

if __main__ == "__main__":
    unittest.main()
