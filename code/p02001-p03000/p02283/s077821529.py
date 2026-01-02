class BinaryTree():
    def __init__(self):
        self.key = None
        self.parent = None
        self.left = None
        self.right = None

def insert(z):
    global root
    y = None
    x = root
    while x != None:
        y = x
        if z.key < x.key:
            x = x.left
        else:
            x = x.right
    z.parent = y
    if y == None:
        root = z
    elif z.key < y.key:
        y.left = z
    else:
        y.right = z

def inoder(x):
    if x == None: return []
    else:
        r = []
        r.extend(inoder(x.left))
        r.append(str(x.key))
        r.extend(inoder(x.right))
    return r

def preoder(x):
    if x == None: return []
    else:
        r = []
        r.append(str(x.key))
        r.extend(preoder(x.left))
        r.extend(preoder(x.right))
    return r

def show(x):
    print(" " + " ".join(inoder(x)))
    print(" " + " ".join(preoder(x)))


root = None
n = int(input())
for i in range(n):
    L = input().split()
    if L[0] == "insert":
        T = BinaryTree()
        T.key = int(L[1])
        insert(T)
    else:
        show(root)