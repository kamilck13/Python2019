#6.2
import math
import unittest

class Point:
    """Klasa reprezentujaca punkty na plaszczyznie."""

    def __init__(self, x, y): 
        self.x = x
        self.y = y

    def __str__(self):        
        return str("(" + str(self.x) + ", " + str(self.y) + ")")

    def __repr__(self):       
        return str("Point(" + str(self.x) + ", " + str(self.y) + ")")

    def __eq__(self, other):   
        if(self.x == other.x and self.y == other.y):
            return True
        return False

    def __ne__(self, other):       
        return not self == other
    
    def __add__(self, other):  
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):  
        return Point(self.x - other.x, self.y - other.y)

    def __mul__(self, other): 
        return ((self.x * other.x) +  (self.y*other.y))

    def cross(self, other):         
        return self.x * other.y - self.y * other.x

    def length(self):        
        return math.sqrt(math.pow(self.x, 2) + math.pow(self.y, 2))


class TestPoint(unittest.TestCase):

    def setUp(self): pass

    def test_init(self):
        tmp = Point(1,2)
        self.assertIsInstance(tmp, Point)
        self.assertIs(tmp.x, 1)
        self.assertIs(tmp.y, 2)

    def test_str(self):
        tmp = Point(1,2)
        self.assertIsInstance(str(tmp), str)
        self.assertEqual(Point.__str__(tmp), "(1, 2)")

    def test_repr(self):
        tmp = Point(1,2)
        self.assertIsInstance(Point.__repr__(tmp), str)
        self.assertEqual(Point.__repr__(tmp), "Point(1, 2)")

    def test_eq(self):
        tmp = Point(1,2)
        self.assertEqual(Point.__eq__(tmp, Point(1,2)), True)
        self.assertEqual(Point.__eq__(tmp, Point(2,3)), False)
        self.assertEqual(Point.__eq__(tmp, Point(0, 4)), False)

    def test_ne(self):
        tmp = Point(1,2)
        self.assertFalse(tmp != Point(1,2))
        self.assertTrue(tmp != Point(2,2))
        self.assertTrue(tmp != Point(0,0))

    def test_add(self):
        tmp = Point(1,2)
        self.assertEqual(Point.__add__(tmp, tmp), Point(2,4))
        self.assertEqual(Point.__add__(tmp, Point(-1,-2)), Point(0,0))
        self.assertEqual(Point.__add__(tmp, Point(0,0)), tmp)
    
    def test_sub(self):
        tmp = Point(1,2)
        self.assertEqual(Point.__sub__(tmp, tmp), Point(0,0))
        self.assertEqual(Point.__sub__(tmp, Point(-1,-2)), Point(2,4))
        self.assertEqual(Point.__sub__(tmp,Point(0,0)), tmp)

    def test_mul(self):
        tmp = Point(1,2)
        self.assertEqual(Point.__mul__(tmp, Point(3,4)), 11)
        self.assertEqual(Point.__mul__(tmp, Point(0,0)), 0)
        self.assertEqual(Point.__mul__(tmp, tmp), 5)

    def test_cross(self):
        tmp = Point(1,2)
        self.assertEqual(tmp.cross(tmp), 0)
        self.assertEqual(tmp.cross(Point(0,0)), 0)
        self.assertEqual(tmp.cross(Point(3,4)), -2)

    def test_length(self):
        self.assertEqual(Point(2,0).length(), 2)
        self.assertEqual(Point(0,0).length(), 0)
        self.assertEqual(Point(3,4).length(), 5)

    def tearDown(self): pass

if __name__ == '__main__':
    unittest.main()     