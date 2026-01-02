# Treap
class Node():
    def __init__(self, k, p):
        self.k = k
        self.p = p
        self.left = None
        self.right = None

def rightRotate(t):
    s = t.left
    t.left = s.right
    s.right = t
    return s

def leftRotate(t):
    s = t.right
    t.right = s.left
    s.left = t
    return s

def insert(t, key, pri):
    if t == None:
        return Node(key, pri)
    if key == t.k:
        return t

    if key < t.k:
        t.left = insert(t.left, key, pri)
        if t.p < t.left.p:
            t = rightRotate(t)
    else:
        t.right = insert(t.right, key, pri)
        if t.p < t.right.p:
            t = leftRotate(t)
    return t

def erase(t, key):
    if t == None:
        return None

    if key == t.k:
        if t.left == None and t.right == None:
            return None
        elif t.left == None:
            t = leftRotate(t)
        elif t.right == None:
            t = rightRotate(t)
        else:
            if t.left.p > t.right.p:
                t = rightRotate(t)
            else:
                t = leftRotate(t)
        return erase(t, key)

    if key < t.k:
        t.left = erase(t.left, key)
    else:
        t.right = erase(t.right, key)
    return t

def find(t, k):
    if t == None:
        return -1
    if t.k == k:
        return 1
    if k < t.k:
        return find(t.left, k)
    else:
        return find(t.right, k)

def inorder(t):
    if t == None:
        return 
    inorder(t.left)
    print(" " + str(t.k), end="")
    inorder(t.right)

def preorder(t):
    if t == None:
        return
    print(" " + str(t.k), end="")
    preorder(t.left)
    preorder(t.right)

def output(t):
    inorder(t)
    print()
    preorder(t)
    print()


t = None
data = []
m = int(input())
for i in range(m):
    data.append(list(input().split()))

for i in range(m):
    if data[i][0] == "insert":
        t = insert(t, int(data[i][1]), int(data[i][2]))
    elif data[i][0] == "print":
        output(t)
    elif data[i][0] == "find":
        result = find(t, int(data[i][1]))
        if result == 1:
            print("yes")
        else:
            print("no")
    else:
        t = erase(t, int(data[i][1]))
