import math
import unittest

NOTHING = object()

class Node:
    def __init__(self, data=None, left=None, right=None, parent=None):
        self.data = data
        self.left = left
        self.right = right
        self.parent = parent
    def __str__(self):
        return str(self.data)

class  BinarySearchTree:
    def __init__(self, top = None):     #top - głowa drzewa kalsy node
        self.top = top

    def print_indented(self, top = NOTHING):     # funkcja wypisujaca elementy drzewa
        if top is NOTHING: top = self.top
        if top is None:
            return ""
        left = self.print_indented(top.left)
        right = self.print_indented(top.right)
        if(left != "" and right != ""):
            return str(top.data) + "+[" + left + "]+[" + right + "]"
        elif(left != ""):
            return str(top.data) + "+[" + left + "]"
        elif(right != ""):
            return str(top.data) + "+[" + right + "]"
        else:
            return str(top.data)

    def insert(self, node, top = NOTHING):   # wstawia element
        if top is NOTHING: top = self.top
        if top is None:
            self.top = node
            return node
        if node.data < top.data:
            top.left = self.insert(node, top.left)
            top.left.parent = top
        elif node.data > top.data:
            top.right = self.insert(node, top.right)
            top.right.parent = top
        else:
            pass          # ignorujemy duplikaty
        self.top = top
        return top

    def search(self, data, top = NOTHING):   # zwraca węzeł lub None
        if top is NOTHING: top = self.top
        if top is None or top.data == data:
            return top
        node = self.search(data, top.left)
        if node:
            return node
        else:
            return self.search(data, top.right)  

    def _transplant (self, first, second):
        if first.parent is None:
            self.top = second
            if self.top:
                self.top.parent = None
            return
        elif first == first.parent.left:
            first.parent.left = second
        else:
            first.parent.right = second
        if second:
            second.parent = first.parent
        return

    def _find_min(self, top):
        if top is None:
            raise ValueError("emnty tree")
        while top.left:
            top = top.left
        return top

    def delete(self, node):         #usuwa element
        if self.top is None or node is None:
            return
        if node.left is None:
            self._transplant(node, node.right)
            return
        elif node.right is None:
            self._transplant(node, node.left)
            return
        else:
            y = self._find_min(node.right)
            if y.parent != node:
                self._transplant(y, y.right)
                y.right = node.right
            if y.right:
                y.right.parent = y
        self._transplant(node, y)
        y.left = node.left
        y.left.parent = y
        return

    # algorytm DSW -----------------------------------------------------
    def DSW(self):
        self._createSpine()
        self._createWeightedTree()        

    def _spine_height(self, top = NOTHING):
        if top is NOTHING: top = self.top
        if top is None:
            return 0
        return 1 + self._spine_height(top.right)

    def _left_rotation(self, root):
        parent = root.parent
        right = root.right
        if right.left != None:
            right.left.parent = root
        if root.parent != None:
            root.parent.right = root.right
        root.right = right.left
        right.left = root
        root.parent = right
        right.parent = parent
        return right

    # 1) Tworzenie kręgosłupa
    def _createSpine(self):
        tmp = self.top #tmp to zmienna tymczasowa
        while tmp != None:
            if tmp.left != None: #jeśli posiada lewego potomka
                if tmp.parent !=None:
                    tmp.parent.right = tmp.left
                else:
                    self.top = tmp.left
                #rotacja w prawo
                left = tmp.left
                parent = tmp.parent
                tmp.left = tmp.left.right     
                tmp.parent = left
                left.right = tmp
                left.parent = parent
                #tmp zostaje przesunięty do nowo powstałego rodzica
                tmp = left
            else:
                #tmp zostaje przesunięty w miejsce swojego prawego potomka;
                tmp = tmp.right

    #2) tworzenie idealnie wyważonego drzewa
    def _createWeightedTree(self):
        n = self._spine_height()
        m = pow(2, math.floor(math.log(n + 1, 2))) - 1
        #wykonaj n-m rotacji, idąc od początku linii po prawych potomkach
        tmp = self.top
        for _ in range(n-m):
            tmp = self._left_rotation(tmp)
            if(tmp.parent == None):
                self.top = tmp
            tmp = tmp.right
        while m > 1:
            m = m//2
            # wykonaj m rotacji, idąc od początku linii po prawych potomkach
            tmp = self.top
            for _ in range(m):           
                tmp = self._left_rotation(tmp)
                if(tmp.parent == None):
                    self.top = tmp
                tmp = tmp.right      
    

class AllTests(unittest.TestCase):
    def setUp(self):
        self.root =  BinarySearchTree()         # puste drzewo        
        self.root.insert(Node(2))
        self.root.insert(Node(3))
        self.root.insert(Node(5))
        self.root.insert(Node(1))
        self.root.insert(Node(4))
        self.root.insert(Node(8))
        self.root.insert(Node(9))
        self.root.insert(Node(6))
        self.root.insert(Node(0))
        self.root.insert(Node(10))
        self.root.insert(Node(7))
        #self.root.print_indented()

    def test1_solve1(self):
        wynik = "2+[1+[0]]+[3+[5+[4]+[8+[6+[7]]+[9+[10]]]]]"
        self.assertEqual(self.root.print_indented(), wynik)

    def test2_solve1(self):
        self.root.DSW()
        wynik = "7+[3+[1+[0]+[2]]+[5+[4]+[6]]]+[9+[8]+[10]]"
        self.assertEqual(self.root.print_indented(), wynik)

    def test3_solve1(self):
        self.root.delete(self.root.search(7))
        wynik = "2+[1+[0]]+[3+[5+[4]+[8+[6]+[9+[10]]]]]"
        self.assertEqual(self.root.print_indented(), wynik)

    def test3_solve2(self):
        self.root.delete(self.root.search(8))
        wynik = "2+[1+[0]]+[3+[5+[4]+[9+[6+[7]]+[10]]]]"
        self.assertEqual(self.root.print_indented(), wynik)

    def test3_solve3(self):
        wynik = "2+[1+[0]]+[3+[5+[4]+[8+[6+[7]]+[9+[10]]]]]"
        self.assertEqual(self.root.print_indented(), wynik)

if __name__ == '__main__':
    unittest.main() 