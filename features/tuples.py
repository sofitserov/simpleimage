import math
from floatingpoint import *


class Tuple:

    def __init__(self, x, y, z, w):
        self.x = x
        self.y = y
        self.z = z
        self.w = w
        return

    def is_point(self):
        if self.w == 0.0:
            return False
        else:
            return True

    def is_vector(self):
        if self.w == 0.0:
            return True
        else:
            return False

    def __eq__(self, other):
        if floateq(self.x, other.x) \
                and floateq(self.y, other.y) \
                and floateq(self.z, other.z) \
                and floateq(self.w, other.w):
            return True
        else:
            return False

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        z = self.z + other.z
        w = self.w + other.w
        return Tuple(x, y, z, w)

    def __sub__(self, other):
        x = self.x - other.x
        y = self.y - other.y
        z = self.z - other.z
        w = self.w - other.w
        return Tuple(x, y, z, w)

    def __neg__(self):
        return Tuple(-self.x, -self.y, -self.z, -self.w)

    def __mul__(self, other):
        x = self.x * other
        y = self.y * other
        z = self.z * other
        w = self.w * other
        return Tuple(x, y, z, w)

    def magnitude(self):
        mm = self.x * self.x + self.y * self.y + self.z * self.z + self.w * self.w
        return math.sqrt(mm)

    def normalize(self):
        x = self.x / self.magnitude()
        y = self.y / self.magnitude()
        z = self.z / self.magnitude()
        w = self.w / self.magnitude()
        return Tuple(x, y, z, w)

    def __repr__(self):
        s = "(x=%.3f, y=%.3f, z=%.3f, w=%.3f)" % (self.x, self.y, self.z, self.w)
        return s


class Point(Tuple):
    def __init__(self, x, y, z):
        Tuple.__init__(self, x, y, z, 1.0)
        return


class Vector(Tuple):
    def __init__(self, x, y, z):
        Tuple.__init__(self, x, y, z, 0.0)
        return


def dot(a, b):
    return float(a.x * b.x + a.y * b.y + a.z * b.z + a.w * b.w)


def cross(a, b):
    return Vector(a.y * b.z - a.z * b.y,
                  a.z * b.x - a.x * b.z,
                  a.x * b.y - a.y * b.x)
