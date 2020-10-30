from features.tuples import *
class Color:

    def __init__(self, r, g, b):
        self.red = r
        self.green = g
        self.blue = b
        return

    def __eq__(self, other):
        if floateq(self.red, other.red) \
                and floateq(self.green, other.green) \
                and floateq(self.blue, other.blue) :
            return True
        else:
            return False

    def __add__(self, other):
        r = self.red + other.red
        g = self.green + other.green
        b = self.blue + other.blue
        return Color(r, g, b)

    def __sub__(self, other):
        r = self.red - other.red
        g = self. green - other.green
        b = self.blue - other.blue
        return Color(r, g, b)

    def __mul__(self, scaler):
        r = self.red * scaler
        g = self.green * scaler
        b = self.blue * scaler
        return Color(r, g, b)
