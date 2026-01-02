# Binary Search Tree
class Node:
    def __init__(self, v):
        self.value = v
        self.parent = None
        self.left = None
        self.right = None

# 再帰を使わないパターンの方が早い
def insert(node):
    global root
    y = None
    x = root
    while x is not None:
        y = x
        if node.value < x.value:
            x = x.left
        else:
            x = x.right
    node.parent = y
    if y is None:
        root = node
    elif node.value < y.value:
        y.left = node
    else:
        y.right = node

def find(num):
    global root
    x = root
    while x is not None:
        if num == x.value:
            return True
        elif num < x.value:
            x = x.left
        else:
            x = x.right
    return False

def preorder_walk(node):
    if node:
        yield node.value
        for x in preorder_walk(node.left):
            yield x
        for x in preorder_walk(node.right):
            yield x

def inorder_walk(node):
    if node:
        for x in inorder_walk(node.left):
            yield x
        yield node.value
        for x in inorder_walk(node.right):
            yield x

root = None
n = int(input())
for i in range(n):
    cmd, *val = input().split()
    if cmd == "insert":
        #root = insert(root, int(val[0]))
        insert(Node(int(val[0])))
    elif cmd == "print":
        print("", *inorder_walk(root))
        print("", *preorder_walk(root))
    elif cmd == "find":
        if find(int(val[0])):
            print("yes")
        else:
            print("no")
