#12.2
import unittest

def binarne_rek(L, left, right, y):
    mid = int((left + right) / 2)
    if L[mid] == y:
        return mid
    elif (L[mid] < y and mid != right):
        return binarne_rek(L, mid + 1, right, y)
    elif (L[mid] > y and mid != left):
        return binarne_rek(L, left, mid - 1, y)
    else:
        return None


class AllTests(unittest.TestCase):
    def test1(self):
        L = (1, 2, 3, 4, 5, 6, 7)
        self.assertEqual(binarne_rek(L, 0, 6, 0), None)

    def test2(self):
        L = (1, 2, 3, 4, 5, 6, 7)
        self.assertEqual(binarne_rek(L, 0, 6, 1), 0)

    def test3(self):
        L = (1, 2, 3, 4, 5, 6, 7)
        self.assertEqual(binarne_rek(L, 0, 6, 2), 1)

    def test4(self):
        L = (1, 2, 3, 4, 5, 6, 7)
        self.assertEqual(binarne_rek(L, 0, 6, 3), 2)

    def test5(self):
        L = (1, 2, 3, 4, 5, 6, 7)
        self.assertEqual(binarne_rek(L, 0, 6, 4), 3)

    def test6(self):
        L = (1, 2, 3, 4, 5, 6, 7)
        self.assertEqual(binarne_rek(L, 0, 6, 5), 4)

    def test7(self):
        L = (1, 2, 3, 4, 5, 6, 7)
        self.assertEqual(binarne_rek(L, 0, 6, 6), 5)

    def test8(self):
        L = (1, 2, 3, 4, 5, 6, 7)
        self.assertEqual(binarne_rek(L, 0, 6, 7), 6)

    def test9(self):
        L = (1, 2, 3, 4, 5, 6, 7)
        self.assertEqual(binarne_rek(L, 0, 6, 8), None)


if __name__ == "__main__":
    unittest.main()
