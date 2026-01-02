def lrotate(t):
    s = t.right
    t.right = s.left
    s.left = t
    return s

def rrotate(t):
    s = t.left
    t.left = s.right
    s.right = t
    return s

def insert(t, key, pri):
    if t == None:
        return Treap(key, pri)
    if key == t.key:
        return t

    if key < t.key:
        t.left = insert(t.left, key, pri)
        if t.pri < t.left.pri:
            t = rrotate(t)
    else:
        t.right = insert(t.right, key, pri)
        if t.pri < t.right.pri:
            t = lrotate(t)
    return t

def delete(t, key):
    if t == None:
        return None

    if key == t.key:
        if t.left == None and t.right == None:
            return None
        elif t.left == None:
            t = lrotate(t)
        elif t.right == None:
            t = rrotate(t)
        else:
            if t.left.pri > t.right.pri:
                t = rrotate(t)
            else:
                t = lrotate(t)
        return delete(t, key)

    if key < t.key:
        t.left = delete(t.left, key)
    else:
        t.right = delete(t.right, key)
    return t

def find(t, key):
    if t == None:
        return -1
    if t.key == key:
        return 1
    if key < t.key:
        return find(t.left, key)
    else:
        return find(t.right, key)
    
def inorder(t):
    if t == None:
        return 
    inorder(t.left)
    print(" " + str(t.key), end="")
    inorder(t.right)

def preorder(t):
    if t == None:
        return
    print(" " + str(t.key), end="")
    preorder(t.left)
    preorder(t.right)



class Treap():
    def __init__(self, key, pri):
        self.key = key
        self.pri = pri
        self.left = None
        self.right = None
        
t = None
data = []
m = int(input())
for i in range(m):
    data.append(list(input().split()))

for i in range(m):
    if data[i][0] == "insert":
        t = insert(t, int(data[i][1]), int(data[i][2]))
    elif data[i][0] == "delete":
        t = delete(t, int(data[i][1]))
    elif data[i][0] == "find":
        result = find(t, int(data[i][1]))
        if result == 1:
            print("yes")
        else:
            print("no")
    else:
        inorder(t)
        print()
        preorder(t)
        print()


