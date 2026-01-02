class Node:
    def __init__(self):
        self.key, self.left, self.right, self.parent = 0, None, None, None

class BST:
    def __init__(self):
        self.root = None
    
    def insert(self, key):
        x, y = self.root, None
        z = Node()
        z.key = key
        while x != None:
            y = x
            if z.key < x.key:
                x = x.left
            else:
                x = x.right
        z.parent = y
        if y == None:
            self.root = z
        elif z.key < y.key:
            y.left = z
        else:
            y.right = z
    
    def find(self, key):
        r = self.root
        while r != None:
            if key == r.key:
                break
            elif key < r.key:
                r = r.left
            else:
                r = r.right
        return r
    
    def preOrder(self, r = -1):
        if r == -1: r = self.root
        if r == None:   return
        print("", r.key, end = '')
        self.preOrder(r.left)
        self.preOrder(r.right)
    
    def inOrder(self, r = -1):
        if r == -1: r = self.root
        if r == None:   return
        self.inOrder(r.left)
        print("", r.key, end = '')
        self.inOrder(r.right)

tree = BST()
for _ in range(int(input())):
    s = input()
    if s[0] == 'i':
        tree.insert(int(s[7:]))
    elif s[0] == 'p':
        tree.inOrder()
        print("")
        tree.preOrder()
        print("")
    else:
        print(['no', 'yes'][tree.find(int(s[5:])) != None])
