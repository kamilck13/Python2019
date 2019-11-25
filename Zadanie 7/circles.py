#7.5
from points import Point
import math
import unittest

class Circle:

    def __init__(self, x, y, radius):
        if radius < 0:
            raise ValueError("promien ujemny")
        self.pt = Point(x, y)
        self.radius = radius

    def __repr__(self):
        return ("Circle("+ str(self.pt.x) + ", " + str(self.pt.y) + ", " + str(self.radius) + ")")

    def __eq__(self, other):
        return self.pt == other.pt and self.radius == other.radius

    def __ne__(self, other):
        return not self == other

    def area(self):
        return (math.pi * self.radius * self.radius)

    def move(self, x, y):
        self.pt.x += x
        self.pt.y += y

    def cover(self, other):
        odlSrodk = math.sqrt(math.pow(other.pt.x - self.pt.x, 2) + math.pow(other.pt.y - self.pt.y, 2))
        if odlSrodk <= math.fabs(self.radius - other.radius): #jeden w drugim
            if self.radius > other.radius:
                return self
            return other
        else:
            tmpX = (self.pt.x + other.pt.x)/2. #wyznaczam srodek na prostej laczacej srodki okregow
            tmpY = (self.pt.y + other.pt.y)/2.
            tmp = math.sqrt(math.pow(other.pt.x - self.pt.x, 2) + math.pow(other.pt.y - self.pt.y, 2)) #dlugosc odcinka laczacego srodki
            tmpR = 0
            if self.radius > other.radius:
                tmpR = self.radius + (tmp/2.) #promien okregu
            else:
                tmpR = other.radius + (tmp/2.)
            return Circle(tmpX, tmpY, tmpR)

class TestCircle(unittest.TestCase):

    def setUp(self):
    	self.tmp = Circle(1,2,3) 
    	self.tmp2 = Circle(0,0,0)

    def test_init(self):
        self.assertEqual(self.tmp.pt, Point(1,2))
        self.assertEqual(self.tmp.pt.x, 1)
        self.assertEqual(self.tmp.pt.y, 2)
        self.assertEqual(self.tmp.radius, 3)
        with self.assertRaises(ValueError):
            Circle(0,0,-1)

    def test_repr(self):
        self.assertEqual(repr(self.tmp), "Circle(1, 2, 3)")

    def test_eq(self):
        self.assertFalse(self.tmp == Circle(1,2,4))
        self.assertTrue(self.tmp == Circle(1.0,2.0,3.0))
        self.assertTrue(self.tmp == Circle(1,2,3))

    def test_ne(self):
   	    self.assertTrue(self.tmp != Circle(1,2,4))
   	    self.assertFalse(self.tmp != Circle(1.0,2.0,3.0))
   	    self.assertFalse(self.tmp != Circle(1,2,3))

    def test_area(self):
   	    self.assertEqual(self.tmp.area(), math.pi * pow(3, 2))
   	    self.assertEqual(self.tmp2.area(), 0)

    def test_move(self):
        self.tmp.move(1,2)
        self.assertEqual(self.tmp, Circle(2,4,3))
        self.tmp2.move(1, 2)
        self.assertEqual(self.tmp2, Circle(1,2,0))

    def test_cover(self):
        self.assertEqual(self.tmp.cover(self.tmp2), Circle(1,2,3))
        self.assertEqual(self.tmp2.cover(self.tmp), Circle(1,2,3))
        self.assertEqual(Circle(0,0,2).cover(Circle(4,0,2)), Circle(2, 0, 4))

    def tearDown(self): pass

if __name__ == '__main__':
    unittest.main()     