class Node():
    def __init__(self, key):
        self.key = key
        self.left = self.right = None
        
def insert(key):
    global root

    x = root
    y = None
    while x:x, y = x.left if key < x.key else x.right , x
    if y == None:root = Node(key)
    elif y.key < key:y.right = Node(key)
    else:y.left = Node(key)
        
        
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

def delete(node, key):
    x = node
    while x.key != key and x:
        x, y = node.left if key < x.key else x.right, x
    if x == None:
        return
    else:
        if x.left == None and x.right == None:
            if key < y.key:y.left = None
            else:y.right = None
        elif x.right == None:
            if key < y.key:y.left = x.left
            else:y.right = x.left
        elif x.left == None:
            if key > y.key:y.right = x.right
            else:y.left = x.right
        else:
            a = x.right
            c = 0
            b = 1
            while a:a, b, c = a.left if a.left != None and a.right != None else a.left if a.left != None else None  , a, b
            if c == 1:
                b.left = x.left
                if key < y.key:y.left = b
                else:y.right = b
            else:
                c.left = b.right
                x.key = b.key
                
                
            
        
        
    

n = int(input())
root = None
for j in range(n):
    s, *i = input().split()
    if s[0] == 'i':insert(int(i[0]))
    elif s[0] == 'f':
        find(root, int(i[0]))
    elif s[0] == 'd':
        delete(root, int(i[0]))
    else:
        ino(root);print();pre(root);print()
        
    
