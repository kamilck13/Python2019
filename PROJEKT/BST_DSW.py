import math

class Node:
    def __init__(self, data=None, left=None, right=None, parent=None):
        self.data = data
        self.left = left
        self.right = right
    def __str__(self):
        return str(self.data)

def btree_print_indented(top, level=0):     # funkcja rysująca drzewo
    if top is None:
        return
    btree_print_indented(top.right, level+1)
    print ("{}* {}".format('   '*level, top))
    btree_print_indented(top.left, level+1)

def bst_insert(top, node):   # wstawia element i zwraca korzeń
    if top is None:
        return node
    if node.data < top.data:
        top.left = bst_insert(top.left, node)
        top.left.parent = top
    elif node.data > top.data:
        top.right = bst_insert(top.right, node)
        top.right.parent = top
    else:
        pass          # ignorujemy duplikaty
    return top        # bez zmian

# algorytm DSW -----------------------------------------------------
def DSW(root):
    print("Drzewo ----------------------------------")
    btree_print_indented(root)
    print("Kręgosłup -------------------------------")
    root = createSpine(root)
    btree_print_indented(root)
    root = CreateWeightedTree(root)
    print("Zrównoważone drzewo ---------------------")
    btree_print_indented(root)
    return root

def Spine_height(top):
    if top is None:
        return 0
    return 1 + Spine_height(top.right)

def right_rotation(root):
    parent = root.parent
    right = root.right
    if root.parent != None:
        root.parent.right = root.right
    root.right = right.left
    right.left = root
    root.parent = right
    right.parent = parent
    return right

# 1) Tworzenie kręgosłupa
def createSpine(root):
    tmp = root #tmp to zmienna tymczasowa
    while tmp != None:
        if tmp.left != None: #jeśli posiada lewego potomka
            if tmp.parent !=None:
                tmp.parent.right = tmp.left
            else:
                root = tmp.left
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
    return root

#2) tworzenie idealnie wyważonego drzewa
def CreateWeightedTree (root):
    n = Spine_height(root)
    m = pow(2, math.floor(math.log(n + 1, 2))) - 1
    #wykonaj n-m rotacji, idąc od początku linii po prawych potomkach
    tmp = root
    for _ in range(n-m):
        tmp = right_rotation(tmp)
        if(tmp.parent == None):
            root = tmp
        tmp = tmp.right
    while m > 1:
        m = math.floor(m/2)
        # wykonaj m rotacji, idąc od początku linii po prawych potomkach
        tmp = root
        for _ in range(m):           
            tmp = right_rotation(tmp)
            if(tmp.parent == None):
                 root = tmp
            tmp = tmp.right      
    return root
    


root = None             # puste drzewo        
root = bst_insert(root, Node(2))
root = bst_insert(root, Node(3))
root = bst_insert(root, Node(5))
root = bst_insert(root, Node(1))
root = bst_insert(root, Node(4))
root = bst_insert(root, Node(8))
root = bst_insert(root, Node(9))
root = bst_insert(root, Node(6))
root = bst_insert(root, Node(0))
root = bst_insert(root, Node(10))

root = DSW(root)