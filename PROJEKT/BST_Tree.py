import math

NOTHING = object()

class Node:
    def __init__(self, data=None, left=None, right=None, parent=None):
        self.data = data
        self.left = left
        self.right = right
        self.parent = parent
    def __str__(self):
        return str(self.data)

class BST_Tree:
    def __init__(self, top = None):     #top - głowa drzewa kalsy node
        self.top = top

    def btree_print_indented(self, top = NOTHING, level = 0):     # funkcja rysująca drzewo
        if top is NOTHING: top = self.top
        if top is None:
            return
        self.btree_print_indented(top.right, level+1)
        print ("{}* {}".format('   '*level, top))
        self.btree_print_indented(top.left, level+1)

    def bst_insert(self, node, top = NOTHING):   # wstawia element
        if top is NOTHING: top = self.top
        if top is None:
            self.top = node
            return node
        if node.data < top.data:
            top.left = self.bst_insert(node, top.left)
            top.left.parent = top
        elif node.data > top.data:
            top.right = self.bst_insert(node, top.right)
            top.right.parent = top
        else:
            pass          # ignorujemy duplikaty
        self.top = top
        return top

    def btree_search(self, data, top = NOTHING):   # zwraca węzeł lub None
        if top is NOTHING: top = self.top
        if top is None or top.data == data:
            return top
        node = self.btree_search(data, top.left)
        if node:
            return node
        else:
            return self.btree_search(data, top.right)  

    def _btree_transplant (self, first, second):
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

    def _btree_find_min(self, top):
        if top is None:
            raise ValueError("emnty tree")
        while top.left:
            top = top.left
        return top

    def bst_delete(self, data):         #usuwa element
        node = self.btree_search(data)
        if self.top is None or node is None:
            return
        if node.left is None:
            self._btree_transplant(node, node.right)
            return
        elif node.right is None:
            self._btree_transplant(node, node.left)
            return
        else:
            y = self._btree_find_min(node.right)
            if y.parent != node:
                self._btree_transplant(y, y.right)
                y.right = node.right
            if y.right:
                y.right.parent = y
        self._btree_transplant(node, y)
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

    def _right_rotation(self, root):
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
            tmp = self._right_rotation(tmp)
            if(tmp.parent == None):
                self.top = tmp
            tmp = tmp.right
        while m > 1:
            m = math.floor(m/2)
            # wykonaj m rotacji, idąc od początku linii po prawych potomkach
            tmp = self.top
            for _ in range(m):           
                tmp = self._right_rotation(tmp)
                if(tmp.parent == None):
                    self.top = tmp
                tmp = tmp.right      
    


root = BST_Tree()         # puste drzewo        
root.bst_insert(Node(2))
root.bst_insert(Node(3))
root.bst_insert(Node(5))
root.bst_insert(Node(1))
root.bst_insert(Node(4))
root.bst_insert(Node(8))
root.bst_insert(Node(9))
root.bst_insert(Node(6))
root.bst_insert(Node(0))
root.bst_insert(Node(10))
#root.bst_insert(Node(7))

print("Drzewo ----------------------------------")
root.btree_print_indented()
root.DSW()
print("Zrównoważone ----------------------------------")
root.btree_print_indented()


root.bst_delete(6)
print("po usunięciu:  -----------------")
root.btree_print_indented()
