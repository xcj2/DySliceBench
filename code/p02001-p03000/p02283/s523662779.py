import sys
# def input():
#     return sys.stdin.readline()[:-1]

# n = int(input())
# A = [input().split() for i in range(n)]

class Node():
    __slots__ = ['key', 'left', 'right']
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


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
    else: 
        y.right = Node(key) # set z as right child of y
        

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
    else:
        x = root
        inorder_list = inorder([], x)
        print(' '+' '.join(inorder_list))
        preorder_list = preorder([], x)
        print(' '+' '.join(preorder_list))
