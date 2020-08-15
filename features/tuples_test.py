import unittest
import timeit
from features.tuples import *


class TuplesTest(unittest.TestCase):
    def test_scenario1(self):
        a = Tuple(4.3, -4.2, 3.1, 1.0)
        self.assertEqual(a.x, 4.3)
        self.assertEqual(a.y, -4.2)
        self.assertEqual(a.z, 3.1)
        self.assertEqual(a.w, 1.0)
        self.assertEqual(a.is_point(), True)
        self.assertEqual(a.is_vector(), False)
        return

    def test_scenario2(self):
        a = Tuple(4.3, -4.2, 3.1, 0.0)
        self.assertEqual(a.x, 4.3)
        self.assertEqual(a.y, -4.2)
        self.assertEqual(a.z, 3.1)
        self.assertEqual(a.w, 0.0)
        self.assertEqual(a.is_point(), False)
        self.assertEqual(a.is_vector(), True)
        return

    def test_point(self):
        p = Point(4, -4, 3)
        self.assertEqual(p, Tuple(4, -4, 3, 1.0))
        return

    def test_vector(self):
        v = Vector(4, -4, 3)
        self.assertEqual(v, Tuple(4, -4, 3, 0.0))
        return

    def test_addition(self):
        a1 = Tuple(3, -2, 5, 1)
        a2 = Tuple(-2, 3, 1, 0)
        a3 = a1 + a2
        self.assertEqual(a3, Tuple(1, 1, 6, 1))
        return

    def test_sub_point_point(self):
        p1 = Point(3, 2, 1)
        p2 = Point(5, 6, 7)
        v = p1 - p2
        self.assertEqual(v, Vector(-2, -4, -6))
        return

    def test_sub_point_vector(self):
        p = Point(3, 2, 1)
        v = Vector(5, 6, 7)
        self.assertEqual(p - v, Point(-2, -4, -6))
        return

    def test_sub_vector_vector(self):
        v1 = Vector(3, 2, 1)
        v2 = Vector(5, 6, 7)
        self.assertEqual(v1 - v2, Vector(-2, -4, -6))
        return

    def test_zero_tuple(self):
        v1 = Vector(0, 0, 0)
        v2 = Vector(1, -2, 3)
        self.assertEqual(v1 - v2, Vector(-1, 2, -3))
        return

    def test_neg_tuple(self):
        a = Tuple(1, -2, 3, -4)
        self.assertEqual(-a, Tuple(-1, 2, -3, 4))
        return

    def test_multiply_tuples_by_scalar(self):
        a = Tuple(1, -2, 3, -4)
        self.assertEqual(a * 3.5, Tuple(3.5, -7, 10.5, -14))
        return

    def test_multiplying_tuples_by_fraction(self):
        a = Tuple(1, -2, 3, -4)
        self.assertEqual(a * 0.5, Tuple(0.5, -1, 1.5, -2))
        return

    def test_magnitude(self):
        v1 = Vector(1, 0, 0)
        m1 = v1.magnitude()
        self.assertEqual(m1, 1)
        v2 = Vector(0, 1, 0)
        m2 = v2.magnitude()
        self.assertEqual(m2, 1)
        v3 = Vector(0, 0, 1)
        m3 = v3.magnitude()
        self.assertEqual(m3, 1)
        v4 = Vector(1, 2, 3)
        m4 = v4.magnitude()
        self.assertEqual(m4, math.sqrt(14))
        v5 = Vector(-1, -2, -3)
        m5 = v5.magnitude()
        self.assertEqual(m5, math.sqrt(14))
        return


    def test_normalizing_vector(self):
        v = Vector(4, 0, 0)
        v_norm = v.normalize()
        self.assertEqual(v_norm, Vector(1, 0, 0))
        v1 = Vector(1, 2, 3)
        v1_norm = v1.normalize()
        self.assertEqual(v1_norm, Vector(1 / math.sqrt(14), 2 / math.sqrt(14), 3 / math.sqrt(14)))
        self.assertEqual(v1_norm, Vector(0.26726, 0.53452, 0.80178))
        return

    def test_magnitude_of_normalized_vector(self):
        v = Vector(1, 2, 3)
        v_norm = v.normalize()
        m = v_norm.magnitude()
        self.assertEqual(m, 1)
        return

    def test_dot_product(self):
        a = Vector(1, 2, 3)
        b = Vector(2, 3, 4)
        self.assertEqual(dot(a, b), 20)
        return

    def test_cross_product(self):
        a = Vector(1, 2, 3)
        b = Vector(2, 3, 4)
        self.assertEqual(cross(a, b), Vector(-1, 2, -1))
        self.assertEqual(cross(b, a), Vector(1, -2, 1))
        return








if __name__ == '__main__':
    unittest.main()
