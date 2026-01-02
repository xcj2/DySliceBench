import sys
# def input():
#     return sys.stdin.readline()[:-1]

# n = int(input())
# A = [input() for i in range(n)]

class Node():
    __slots__ = ['key', 'left', 'right','parent']
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None


def insert(key):
    global root
    x = root # x is current node
    y = None  #  parent of x 
    while x:
        y = x # set parent
        if key < x.key:
            x = x.left # move to left child
        else:
            x = x.right #move to right child
    
    if root is None:
        root = Node(key)
    elif key < y.key: # set z as left child of y
        y.left = Node(key)
        y.left.parent = y
    else: 
        y.right = Node(key) # set z as right child of y
        y.right.parent = y
        
def find(key):
    global root
    x = root
    while x:
        if key==x.key:
            print('yes')
            return
        elif key < x.key:
            x = x.left
        else:
            x = x.right
    print('no')
    
    
def minimum(x):
    while x.left:
        x = x.left
    return x
    
    
def successor(x):
    if x.right:
        return minimum(x.right)
    y = x.parent
    while (y) and (x==y.right):
        x = y
        y = y.parent
    return y
    
    
    
def delete(key):
    global root
    
    # find z
    z = None
    x = root
    while x:
        if key==x.key:
            z = x
            break
        elif key < x.key:
            x = x.left
        else:
            x = x.right
    if z is None:
        return
    
    # determin y
    if (z.left==None) or (z.right==None):
        y = z
    else:
        y = successor(z)
        
    if y.left:
        x = y.left
    else:
        x = y.right
        
    if x:
        x.parent = y.parent
    
    if y.parent is None:
        root = x
    elif y==y.parent.left:
        y.parent.left = x
    else:
        y.parent.right = x
        
    if y!=z:
        z.key = y.key
    

def inorder(inorder_list, node):
    if node.left is not None:
        inorder(inorder_list, node.left)
    inorder_list.append(str(node.key))
    if node.right is not None:
        inorder(inorder_list, node.right)
    return inorder_list
        
def preorder(preorder_list, node):
    preorder_list.append(str(node.key))
    if node.left is not None:
        preorder(preorder_list, node.left)
    if node.right is not None:
        preorder(preorder_list, node.right)
    return preorder_list
        
root = None

input()
for o in sys.stdin:
    if o[0]=='i':
        insert(int(o[7:]))
    elif o[0]=='f':
        find(int(o[5:]))
    elif o[0]=='d':
        delete(int(o[7:]))
    else:
        x = root
        inorder_list = inorder([], x)
        print(' '+' '.join(inorder_list))
        preorder_list = preorder([], x)
        print(' '+' '.join(preorder_list))
