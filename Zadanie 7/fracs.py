#7.1
import unittest

class Frac:
    """Klasa reprezentująca ułamek."""

    def __init__(self, x=0, y=1):
        if isinstance(x, int) == False and isinstance(x, float) == False:
            raise ValueError("x nie jest typu numerycznego")
        if isinstance(y, int) == False and isinstance(y, float) == False:
            raise ValueError("y nie jest typu numerycznego")
        if y == 0:
            raise ValueError ("Mianownik ulamka nie moze byc 0")

        self.x = x
        self.y = y

    def __str__(self):       
        if self.y == 1:
            return str(self.x)
        return str(self.x)+'/'+str(self.y)

    def __repr__(self):      
        return str("Frac(" + str(self.x) + ","+str(self.y) + ")")

    def __cmp__(self, other):
        tmp1 = float(self)
        tmp2 = float(other)
        if tmp1 == tmp2:
            return 0
        elif tmp1 > tmp2:
            return 1
        return -1

    def __add__(self, other):
        if isinstance(other, int):
            return Frac(self.x + (self.y * other), self.y)
        if self.y == other.y:
            return Frac(self.x + other.x, self.y)
        return Frac((self.x * other.y) + (other.x * self.y) , self.y * other.y)

    __radd__ = __add__ 

    def __sub__(self, other):
        if isinstance(other, int):
            return Frac(self.x - (self.y * other), self.y)
        if self.y == other.y:
            return Frac(self.x - other.x, self.y)
        return Frac((self.x * other.y) - (other.x * self.y) , self.y * other.y)

    def __rsub__(self, other):      
        return Frac(self.y * other - self.x, self.y) 

    def __mul__(self, other): 
        if isinstance(other, int):
            return Frac(self.x * other, self.y)
        return Frac(self.x * other.x, self.y * other.y)

    __rmul__ = __mul__

    def __div__(self, other):
        if other == 0:
            raise ValueError ("Nie mozna dzielic przez 0")
        if isinstance(other, int):
            return Frac(self.x, self.y* other)
        return Frac(self.x * other.y, self.y * other.x)

    def __rdiv__(self, other):
        if self == 0:
            raise ValueError ("Nie mozna dzielic przez 0")
        return Frac(self.y * other, self.x)

    def __pos__(self):
        return self

    def __neg__(self):
        return Frac(-self.x, self.y)

    def __invert__(self):
        return Frac(self.y, self.x)

    def __float__(self): 
        return float(self.x)/float(self.y)

class TestFractions(unittest.TestCase):

    def setUp(self):
        self.tmp = Frac(1,2)
        self.tmp2 = Frac(2,2)
        self.tmp3 = Frac(-1, 2)
        self.tmp4 = Frac(2, 1)
        self.fracZero = Frac(0,1)
    
    def test_init(self):
        with self.assertRaises(ValueError):
            Frac('ala', 1)
        with self.assertRaises(ValueError):
            Frac('ala', 'ala')
        with self.assertRaises(ValueError):
            Frac(1, 'ala')
        with self.assertRaises(ValueError):
            Frac(1, 0)
        self.assertEqual(self.tmp.x, 1)
        self.assertEqual(self.tmp.y, 2)

    def test_div(self):
        self.assertEqual(Frac.__div__(self.tmp, self.tmp), self.tmp2)
        self.assertEqual(Frac.__div__(self.tmp, self.tmp3), Frac(-2,2))
        with self.assertRaises(ValueError):
            Frac.__div__(self.tmp, 0)

    def test_cmp(self):
    	self.assertEqual(Frac.__cmp__(self.tmp, self.tmp), 0)
    	self.assertEqual(Frac.__cmp__(self.tmp, self.tmp2), -1)
    	self.assertEqual(Frac.__cmp__(self.tmp, self.fracZero), 1)

    def test_pos(self):
    	self.assertEqual(Frac.__pos__(self.tmp), self.tmp)
    	self.assertEqual(Frac.__pos__(self.tmp3), self.tmp3)
    	self.assertEqual(Frac.__pos__(self.fracZero), self.fracZero)

    def test_neg(self):
        self.assertEqual(Frac.__neg__(self.tmp), Frac(-1,2))
        self.assertEqual(Frac.__neg__(self.tmp), self.tmp3)
        self.assertEqual(Frac.__neg__(self.tmp3), self.tmp)
        self.assertEqual(Frac.__neg__(-self.fracZero), self.fracZero)

    def test_invert(self):
    	self.assertEqual(Frac.__invert__(-self.tmp), self.tmp4)
    	self.assertEqual(Frac.__invert__(-(-self.tmp3)), self.tmp4)

    def test_float(self):
        self.assertIsInstance(float(self.tmp), float)
        self.assertIsInstance(float(self.fracZero), float)

    def test_repr(self):
        self.assertIsInstance(repr(self.tmp), str)
        self.assertEqual(Frac.__repr__(self.tmp), "Frac(1,2)")

    def test_str(self):
        self.assertIsInstance(str(self.tmp), str)

    def test_add_frac(self):
        self.assertEqual(Frac.__add__(self.tmp, self.tmp), self.tmp2)
        self.assertEqual(Frac.__add__(self.tmp, -self.tmp), self.fracZero)
        self.assertEqual(Frac.__add__(self.tmp2, -self.tmp), self.tmp)

    def test_mul(self):
        self.assertEqual(Frac.__mul__(self.tmp, self.tmp), Frac(1,4))
        self.assertEqual(Frac.__mul__(self.tmp,-self.tmp), Frac(-1,4))
        self.assertEqual(Frac.__mul__(self.tmp, self.fracZero), Frac(0,1))

    def test_sub(self):
        self.assertEqual(Frac.__sub__(self.tmp, self.tmp), Frac(0,2))
        self.assertEqual(Frac.__sub__(self.tmp, -self.tmp), self.tmp2)
        self.assertEqual(Frac.__sub__(self.tmp2, -self.tmp), self.tmp)

    def tearDown(self): pass

if __name__ == '__main__':
    unittest.main()   