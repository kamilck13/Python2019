#8.4
import math
import unittest

def spr(a, b, c):
    tmp = [a, b, c]
    tmp.sort()
    if tmp[0] + tmp[1] >= tmp[-1]:
        return True
    return False

def heron(a, b, c):
    if(spr(a, b, c) == False):
        raise ValueError ("Warunek trojkata nie jest spelniony")
    polObw = (a + b + c)/2
    return math.sqrt(polObw * (polObw - a)*(polObw-b)*(polObw-c))

class AllTests(unittest.TestCase):
    def test1_heron(self):
        self.assertEqual(heron(3,4,5), 6.0)
    def test2_heron(self):
        self.assertEqual(heron(3,7,9), 8.78564169540279)
    def test3_heron(self):
        self.assertEqual(heron(5,7,9), 17.41228014936585)


if __name__ == '__main__':
    unittest.main()  
    #a = int(input("Podaj a: "))
    #b = int(input("Podaj b: "))
    #c = int(input("Podaj c: "))
    #print(heron(a, b, c))   
