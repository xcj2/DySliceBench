class Node():
    def __init__(self, key):
        self.key = key
        self.parent = None
        self.left = None
        self.right = None

class Tree():
    def __init__(self):
        self.root = None
        self.list = []

    def insert(self, node):
        y = None                 # x's parent    
        x = self.root
        while x is not None:
            y = x                # set parent
            if node.key < x.key:
                x = x.left
            else:
                x = x.right
        node.parent = y

        if y is None:
            self.root = node
        elif node.key < y.key:
            y.left = node
        else:
            y.right = node

    def parse_inorder(self, node):
        if node is None:
            return 
        self.parse_inorder(node.left)
        self.list.append(node.key)
        self.parse_inorder(node.right)

    def parse_preorder(self, node):
        if node is None:
            return
        self.list.append(node.key)
        self.parse_preorder(node.left)
        self.parse_preorder(node.right)

N = int(input())
T = Tree()
for i in range(N):
    order, *key = input().split()
    if order == "print":
        T.list = []
        T.parse_inorder(T.root)
        print(" " + " ".join(map(str, T.list)))
        T.list = []
        T.parse_preorder(T.root)
        print(" " + " ".join(map(str, T.list)))
    else:
        node = Node(int(key[0]))
        T.insert(node)

