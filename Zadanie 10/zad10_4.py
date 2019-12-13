#10.4
import unittest

class Queue:
    def __init__(self, size=5):
        self.n = size + 1         # faktyczny rozmiar tablicy
        self.items = self.n * [None]
        self.head = 0           # pierwszy do pobrania 
        self.tail = 0           # pierwsze wolne

    def is_empty(self):
        return self.head == self.tail

    def is_full(self):
        return (self.head + self.n-1) % self.n == self.tail

    def put(self, data):
        if (self.head + self.n-1) % self.n == self.tail:
            raise ValueError("Kolejka jest pelna!")
        self.items[self.tail] = data
        self.tail = (self.tail + 1) % self.n

    def get(self):
        if self.head == self.tail:
            raise ValueError("Kolejka jest pusta")
        data = self.items[self.head]
        self.items[self.head] = None      # usuwam referencje
        self.head = (self.head + 1) % self.n
        return data

class AllTests(unittest.TestCase):
    def setUp(self):
        self.queueEmpty = Queue()
        self.queue1 = Queue(3)
        self.queue1Full = Queue(1)
        self.queue1Full.put(1)

    def test_init(self):
        self.tmp = Queue(2)
        self.assertEqual(self.tmp.n, 3)
        self.assertEqual(self.tmp.head, 0)
        self.assertEqual(self.tmp.tail, 0)
        self.assertEqual(len(self.tmp.items), 3)

    def test_is_empty(self):
        self.assertFalse(self.queue1Full.is_empty())
        self.assertTrue(self.queue1.is_empty())
        self.assertTrue(self.queueEmpty.is_empty())
        
    def test_is_full(self):
        self.assertTrue(self.queue1Full.is_full())
        self.assertFalse(self.queue1.is_full())
        self.assertFalse(self.queueEmpty.is_full())

    def test_put(self):
        self.queue1.put(123)
        self.assertEqual(self.queue1.items[0], 123)
        with self.assertRaises(ValueError):
            self.queue1Full.put(12)

    def test_get(self):
        self.queue1.put(123)
        self.assertEqual(self.queue1.get(), 123)
        with self.assertRaises(ValueError):
            self.queue1.get()
            
    def tearDown(self): pass

if __name__ == '__main__':
    unittest.main()     
