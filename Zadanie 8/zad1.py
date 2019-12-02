#8.1
import unittest

def solve1(a, b, c):
    if a == 0 and b!=0:
        return 'y = '+str(-c/b)+'\nx = 0'
    if a!= 0 and b == 0:
        return 'x = '+str(-c/a)+'\ny = 0'
    if a == 0 and b == 0 and c == 0:
        return "Uklad rownan posiada nieskonczenie wiele rozwiazan"
    if a == 0 and b == 0 and (not c == 0):
    	return "Uklad nie posiada rozwiazania"
    return 'x = ('+str(-c)+'-'+str(b)+'y)/'+str(a)+'\ny = ('+str(-c)+str(-a)+'x)/'+str(b)


class AllTests(unittest.TestCase):
    def test1_solve1(self):
        wynik = "x = (-2-1y)/3" + "\n" + "y = (-2-3x)/1"
        self.assertEqual(solve1(3,1,2), wynik)
    def test2_solve1(self):
        wynik = "x = (-10-8y)/4" + "\n" + "y = (-10-4x)/8"
        self.assertEqual(solve1(4,8,10), wynik)
    def test3_solve1(self):
        wynik = "x = (-1-18y)/2" + "\n" + "y = (-1-2x)/18"
        self.assertEqual(solve1(2,18,1), wynik)
    def test4_solve1(self):
        wynik = "Uklad rownan posiada nieskonczenie wiele rozwiazan"
        self.assertEqual(solve1(0,0,0), wynik)
    def test5_solve1(self):
        wynik = "Uklad nie posiada rozwiazania"
        self.assertEqual(solve1(0,0,5), wynik)

if __name__ == '__main__':
    unittest.main()     
