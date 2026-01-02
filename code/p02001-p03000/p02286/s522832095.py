class Node():
    def __init__(self, key, pri):
        self.key = key
        self.pri = pri
        self.left = self.right = None
        

def insert(t, key, pri):
    if t == None:
        return Node(key, pri) 
    if key == t.key:
        return t                             

    if key < t.key:
        t.left = insert(t.left, key, pri)
        if t.pri < t.left.pri:
            t = rightRotate(t)
    else:
        t.right = insert(t.right, key, pri)
        if t.pri < t.right.pri:
            t = leftRotate(t)

    return t
        
def rightRotate(node):
    global root
    a = node.left
    node.left = a.right
    a.right = node
    if node == root:
        root = a
    return a

def leftRotate(node):
    global root
    a = node.right
    node.right = a.left
    a.left = node
    if node == root:
        root = a
    return a
    
        
def pre(node):
    if node == None:return
    print('',node.key, end = '');pre(node.left);pre(node.right)
    
def ino(node):
    if node == None:return
    ino(node.left);print('',node.key,end='');ino(node.right)

def find(node, key):
    if node == None:
        print('no');return
    if node.key == key:
        print('yes');return
    elif node.key > key:
        find(node.left, key)
    else:
        find(node.right, key)

def delete(t, key):
    global root
    if t == None:
        return None
    if key < t.key:
        t.left = delete(t.left, key)
    elif key > t.key:
        t.right = delete(t.right, key)
    elif key == t.key:
        if t.left == None and t.right == None:
            return None
        elif t.left == None:
            t = leftRotate(t)
        elif t.right == None:
            t = rightRotate(t)
        else:
            if t.left.pri > t.right.pri:
                t = rightRotate(t)
            else:
                t = leftRotate(t)
        return delete(t, key)
    return t

    

n = int(input())
root = None
for j in range(n):
    s, *i = input().split()
    if s[0] == 'i':root = insert(root,int(i[0]), int(i[1]))
    elif s[0] == 'f':
        find(root, int(i[0]))
    elif s[0] == 'd':
        delete(root, int(i[0]))
    else:
        ino(root);print();pre(root);print()
        
    
