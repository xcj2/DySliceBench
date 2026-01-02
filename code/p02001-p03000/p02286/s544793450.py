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
"""
def find(t, k):
    if t == None:
        return -1
    if t.k == k:
        return 1
    if find(t.left, k) == 1:
        return 1
    if find(t.right, k) == 1:
        return 1
"""
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
dict = {}
m = int(input())
for i in range(m):
    data.append(list(input().split()))

for i in range(m):
    if data[i][0] == "insert":
        if (data[i][1] in dict) == False:
            t = insert(t, int(data[i][1]), int(data[i][2]))
            dict[data[i][1]] = True
    elif data[i][0] == "print":
        output(t)
    elif data[i][0] == "find":
        #result = find(t, int(data[i][1]))
        #if result == 1:
        #print(dict)
        #result = data[i][1] in dict
        #print("result", result)
        #print("2", result == True)
        #print(data[i][1] in dict, data[i][1])
        if (data[i][1] in dict) == True:
            #print("12345")
            print("yes")
        else:
            print("no")
    else:
        t = erase(t, int(data[i][1]))
        if (data[i][1] in dict) == True:
            del dict[data[i][1]]
        #print(dict)
