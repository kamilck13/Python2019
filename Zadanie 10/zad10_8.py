#10.8
import random

class RandomQueue:
    def __init__(self, size=5):
        self.n = size+1       # faktyczny rozmiar tablicy
        self.items = self.n * [None]
        self.end = -1           #ostatni element

    def insert(self, item):
        if self.is_full():
            raise ValueError("Kolejka jest pelna")
        self.end = self.end + 1
        self.items[self.end] = item

    def remove(self):           # zwraca losowy element
        output = None
        if self.is_empty():
            raise ValueError("Kolejka jest pusta")
        elif self.end == 0:
            output = self.items[0]
            self.items[0] = None
        else:
            tmp = random.randint(0, self.end)
            output = self.items[tmp]
            self.items[tmp] = self.items[self.end]
            self.items[self.end] = None
        self.end = self.end - 1
        return output

    def is_empty(self):
        return self.end < 0

    def is_full(self):
        return self.n <= self.end+1

    def clear(self):        # czyszczenie listy
        self.end = -1
