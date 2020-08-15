import unittest
from floatingpoint import *

class TestFloatingPoint(unittest.TestCase):
    def test_floateq(self):
        self.assertEqual(floateq(5, 10), False)
        self.assertEqual(floateq(5, 5), True)
        self.assertEqual(floateq(5.55, 5.54), False)
        self.assertEqual(floateq(5.5555554, 5.5555555), True)
        return


if __name__ == '__main__':
    unittest.main()
