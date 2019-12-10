class Node:
    """Klasa reprezentująca węzeł drzewa binarnego."""

    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.data) 

    def count_leafs(top):
        a = 0
        if top.data == None:
            return 1
        if top.left != None:
            a += top.left.count_leafs()
        if top.right != None:
            a += top.right.count_leafs()
        if top.left == None and top.right == None:
            return 1 + a
        return a

    def count_total(top):
        a = 0
        if top.left != None:
            a += top.left.count_total()
        if top.right != None:
            a += top.right.count_total()
        return a + top.data

root = None           # puste drzewo
# Ręczne budowanie większego drzewa.
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

print(root.count_leafs())
print(root.count_total())