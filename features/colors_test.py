import unittest
from features.colors import *


class ColorsTest(unittest.TestCase):
    def test_scenario1(self):
        c = Color(-0.5, 0.4, 1.7)
        self.assertEqual(c.red, -0.5)
        self.assertEqual(c.green, 0.4)
        self.assertEqual(c.blue, 1.7)
        return

    def test_adding(self):
        c1 = Color(0.9, 0.6, 0.75)
        c2 = Color(0.7, 0.1, 0.25)
        c3 = c1 + c2
        self.assertEqual(c3, Color(1.6, 0.7, 1.0))
        return

    def test_subtracting(self):
        c1 = Color(0.9, 0.6, 0.75)
        c2 = Color(0.7, 0.1, 0.25)
        c3 = c1 - c2
        self.assertEqual(c3, Color(0.2, 0.5, 0.5))
        return

    def test_multiplying(self):
        c1 = Color(0.2, 0.3, 0.4)
        c2 = c1 * 2
        self.assertEqual(c2, Color(0.4, 0.6, 0.8))
        return

