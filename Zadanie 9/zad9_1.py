#9.1
class Node:
    """Klasa reprezentująca węzeł listy jednokierunkowej."""

    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data)   # bardzo ogólnie


class SingleList:
    """Klasa reprezentująca całą listę jednokierunkową."""

    def __init__(self):
        self.length = 0         # nie trzeba obliczać za każdym razem
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.length == 0

    def count(self):      # tworzymy interfejs do odczytu
        return self.length

    def insert_head(self, node):
        if self.length == 0:
            self.head = self.tail = node
        else:                   # dajemy na koniec listy
            node.next = self.head
            self.head = node
        self.length += 1

    def insert_tail(self, node):   # klasy O(N)
        if self.length == 0:
            self.head = self.tail = node
        else:                   # dajemy na koniec listy
            self.tail.next = node
            self.tail = node
        self.length += 1

    def remove_head(self):          # klasy O(1)
        if self.length == 0:
            raise ValueError("pusta lista")
        node = self.head
        if self.head == self.tail:   # self.length == 1
            self.head = self.tail = None
        else:
            self.head = self.head.next
        node.next = None   # czyszczenie łącza
        self.length -= 1
        return node   # zwracamy usuwany node

    def remove_tail(self):   # klasy O(N)
        # Zwraca cały węzeł, skraca listę.
        # Dla pustej listy rzuca wyjątek ValueError.
        if self.length == 0:
            raise ValueError("Lista jest pusta")
        last = self.head
        i = 0
        while i < (self.length - 2):
            last = last.next
            i += 1
        node = last.next
        last.next = None
        self.length -= 1
        return node

    def merge(self, other):   # klasy O(1)
        # Węzły z listy other są przepinane do listy self na jej koniec.
        while other.length:
            self.insert_tail(Node(other.remove_head()))

    def clear(self):     # czyszczenie listy
        self.head = None
        self.length = 0


# Zastosowanie.
alist = SingleList()
alist.insert_head(Node(11))         # [11]
alist.insert_head(Node(22))         # [22, 11]
alist.insert_tail(Node(33))         # [22, 11, 33]
print ( "length {}".format(alist.length) ) # odczyt atrybutu
print ( "length {}".format(alist.count()) ) # wykorzystujemy interfejs

other = SingleList()
other.insert_head(Node(44))         # [44]
other.insert_head(Node(55))         # [55, 44]
other.insert_tail(Node(66))         # [55, 44, 66]

alist.merge(other)

while not alist.is_empty():   # kolejność 22, 11, 33
    print ( "remove head {}".format(alist.remove_head()) )