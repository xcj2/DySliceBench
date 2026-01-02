from collections import deque
import sys
readline = sys.stdin.readline
write = sys.stdout.write

class Node:
    __slots__ = ['key', 'left', 'right']
    def __init__(self, key):
        self.key = key
        self.left = self.right = None


root = None

def insert(key):
    global root
    x = root #Tの根
    y = None #親を設定
    while x is not None:
        y = x
        if key < x.key:
            x = x.left #左の子へ移動
        else:
            x = x.right  #右の子へ移動

    if y is None: #Tが空の場合
        root = Node(key)
    elif key < y.key:
        y.left = Node(key) #keyをyの左の子にする
    else:
        y.right = Node(key) #keyをyの右の子にする

def delete(target):
    def remove_node(p,c,a):
        if p.left == c: p.left = a
        else: p.right = a
    p,c = None,root
    while c.key != target: p,c = c,c.left if target < c.key else c.right
    if c.left is None:
        remove_node(p, c, c.right)
    elif c.right is None:
        remove_node(p, c, c.left)
    elif c.right.left is None:
        c.right.left = c.left
        remove_node(p, c, c.right)
    else:
        g = c.right
        while g.left.left: g = g.left
        c.key = g.left.key
        g.left = g.left.right

# def find(key):
#     x = root
#     while x and key != x.key:
#         x = x.left if key < x.key else x.right
#     return x is None

def find(target):
    result = root
    while result and target != result.key:
        result = result.left if target < result.key else result.right
    return result is None # result が None ⇒ false

def inorder(node):
    return   inorder(node.left) + " "+ str(node.key) + inorder(node.right) if node else ''
def preorder(node):
    return   " " + str(node.key) + preorder(node.left) + preorder(node.right) if node else ''
input()
for e in sys.stdin:
    if e[0] == "i":
        insert(int(e[7:]))
    elif e[0] == 'f':
        if find(int(e[5:])):
            print("no")
        else:
            print("yes")
        # print(['yes','no'][find(int(e[5:]))])

    elif e[0] == 'd':
        delete(int(e[7:]))

    else:
        print(inorder(root))
        print(preorder(root))

