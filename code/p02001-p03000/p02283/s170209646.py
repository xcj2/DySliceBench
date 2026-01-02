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
    # while x: x, y = x.left if key < x.key else x.right, x
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

def inorder(node):
    return   inorder(node.left) + " "+ str(node.key) + inorder(node.right) if node else ''
def preorder(node):
    return   " " + str(node.key) + preorder(node.left) + preorder(node.right) if node else ''
input()
for e in sys.stdin:
    if e[0] == "i":
        insert(int(e[7:]))
    else:
        print(inorder(root))
        print(preorder(root))

