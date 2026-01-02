import sys

class Node():
    __slots__ = ['key', 'left', 'right']
    def __init__(self, key):
        self.key = key
        self.left, self.right = None, None
        
    def __str__(self):
        return self.key

root = None
def insert(z):
    global root
    x, y = root, None
    while x:
        y = x
        if z < x.key:
            x = x.left
        else:
            x = x.right
    
    if y == None:
        root = Node(z)
    elif z < y.key:
        y.left = Node(z)
    else:
        y.right = Node(z)
        
def preorder(x):
    return f" {x.key}" + preorder(x.left) + preorder(x.right) if x else ""

def inorder(x):
    return inorder(x.left) + f" {x.key}" + inorder(x.right) if x else ""
        
input()
node = {}
for s in sys.stdin:
    if s[0] == "p":
        pass
        print(inorder(root))
        print(preorder(root))
    else:
        insert(int(s[7:]))
