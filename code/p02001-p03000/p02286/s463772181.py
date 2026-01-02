class Node():
    def __init__(self, key, priority, parent, left, right):
        self.key = key
        self.priority = priority
        self.parent = None
        self.left = None
        self.right = None

def RightRotate(t):
    s = t.left
    t.left = s.right
    s.right = t
    return s

def LeftRotate(t):
    s = t.right
    t.right = s.left
    s.left = t
    return s

def insert(t, key, priority):
    if t == None:
        return Node(key, priority, None, None, None)
    
    if key == t.key:
        return t
    
    if key < t.key:
        t.left = insert(t.left, key, priority)
        if t.priority < t.left.priority :
            t = RightRotate(t)
    
    if key > t.key:
        t.right = insert(t.right, key, priority)
        if t.priority < t.right.priority:
            t = LeftRotate(t)

    return t

def delete(t, key):
    if t == None:
        return None
    if key < t.key:
        t.left = delete(t.left, key)
    elif key > t.key:
        t.right = delete(t.right, key)
    else:
        return _delete(t, key)
    
    return t

def _delete(t, key):
    if t.left == None and t.right == None:
        return None
    elif t.left == None:
        t = LeftRotate(t)
    elif t.right == None:
        t = RightRotate(t)
    else:
        if t.left.priority > t.right.priority:
            t = RightRotate(t)
        else:
            t = LeftRotate(t)
    return delete(t, key)

def find(t, key):
    if t == None:
        print("no")
        return 

    if key == t.key:
        print("yes")
    elif key < t.key:
        find(t.left, key)
    elif key > t.key:
        find(t.right, key)

def print_inorder(t):
    if t == None:
        return
    
    print_inorder(t.left)
    print(" "+str(t.key), end = "")
    print_inorder(t.right)

def print_preorder(t):
    if t == None:
        return 
    print(" "+str(t.key), end = "")
    print_preorder(t.left)
    print_preorder(t.right)

def Main():
    N = int(input())
    t = None

    for i in range(N):
        ope, *arg = input().split()

        if ope == "insert":
            key, priority = map(int, arg)
            t = insert(t, key, priority)

        elif ope == "delete":
            key = int(arg[0])
            t = delete(t, key)

        elif ope == "find":
            key = int(arg[0])
            find(t, key)

        elif ope == "print":
            print_inorder(t)
            print()
            print_preorder(t)
            print()

Main()
