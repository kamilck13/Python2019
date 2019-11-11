#5.2
import unittest

def add_frac(frac1, frac2):       
   if frac1[1] == frac2[1]:
       return [frac1[0] + frac2[0], frac1[1]]
   return [(frac1[0] * frac2[1]) + (frac2[0] * frac1[1]) , frac1[1] * frac2[1]]

def sub_frac(frac1, frac2):        
    if frac1[1] == frac2[1]:
       return [frac1[0] - frac2[0], frac1[1]]
    return [(frac1[0] * frac2[1]) - (frac2[0] * frac1[1]) , frac1[1] * frac2[1]]

def mul_frac(frac1, frac2):        
    return [frac1[0] * frac2[0], frac1[1] * frac2[1]]

def div_frac(frac1, frac2):        
    return [(frac1[0] * frac2[1]), (frac1[1] * frac2[0])]

def is_positive(frac):             
    if (frac[0] > 0 and frac[1] > 0) or (frac[0] < 0 and frac[1] < 0):
       return True
    return False

def is_zero(frac):               
    if frac[0] == 0:
       return True
    return False

def cmp_frac(frac1, frac2):        
    tmp1 = frac2float(frac1)
    tmp2 = frac2float(frac2)
    if tmp1 == tmp2:
       return 0
    elif tmp1 > tmp2:
       return 1
    return -1

def frac2float(frac):               
    return (frac[0] / frac[1])


class TestFractions(unittest.TestCase):

    def setUp(self):
        self.zero = [0, 1]

    def test_add_frac(self):
        self.assertEqual(add_frac([1, 2], [1, 3]), [5, 6])
        self.assertEqual(add_frac([2, 5], [7, 2]), [39, 10])
        self.assertIs(cmp_frac(add_frac([1,2], [1,3]), [5,6]), 0)

    def test_sub_frac(self): 
        self.assertEqual(sub_frac([5, 3], [1, 3]), [4, 3])
        self.assertEqual(sub_frac([3, 8], [1, 5]), [7, 40])
        self.assertIs(cmp_frac(sub_frac([1,2], [1,-2]), [1,1]), 0)

    def test_mul_frac(self): 
        self.assertEqual(mul_frac([1, 3], [1, 2]), [1, 6])
        self.assertEqual(mul_frac([1, 3], [7, 2]), [7, 6])
        self.assertIs(cmp_frac(mul_frac([1,2], [1,-2]), [1,-4]), 0)

    def test_div_frac(self): 
        self.assertEqual(div_frac([4, 3], [4, 3]), [12, 12])
        self.assertEqual(div_frac([1, 3], [10, 5]), [5, 30])
        self.assertIs(cmp_frac(div_frac([1,1], [1,1]), [1,1]), 0)

    def test_is_positive(self):
       self.assertTrue(is_positive([2,1]))
       self.assertFalse(is_positive([0,2]))
       self.assertFalse(is_positive([1,-2])) 

    def test_is_zero(self): 
       self.assertTrue(is_zero([0,1]))
       self.assertTrue(is_zero([0,0]))
       self.assertFalse(is_zero([2,0]))

    def test_cmp_frac(self):
       self.assertIs(cmp_frac([4,2], [1,2]), 1) 
       self.assertIs(cmp_frac([1,2], [2,4]), 0)
       self.assertIs(cmp_frac([0,2], [1,1]), -1)
      
    def test_frac2float(self): 
        self.assertIsInstance(frac2float([1,2]), float)
        self.assertIsInstance(frac2float([0,2]), float)

if __name__ == "__main__":
  unittest.main()