import sys
class Node:
    __slots__ = ['key', 'left', 'right']
    def __init__(self, key):
        self.key = key
        self.left = self.right = None

root = None
def delete(target):
    def remove_node(p, c, a):
        if p.left == c:
            p.left = a
        else:
            p.right = a
    p, c = None, root
    while c.key != target:
        p, c = c, c.left if target < c.key else c.right
    if c.left is None:
        remove_node(p, c, c.right)
    elif c.right is None:
        remove_node(p, c, c.left)
    elif c.right.left is None:
        c.right.left = c.left
        remove_node(p, c, c.right)
    else:
        g = c.right
        while g.left.left:
            g = g.left
        c.key = g.left.key
        g.left = g.left.right

def find(target):
    result = root
    while result and target != result.key:
        result = result.left if target < result.key else result.right
    if result is None:
        return False
    else:
        return True

def insert(key):
    global root
    y = None  # xの親
    x = root
    while x:
        y = x
        x = x.left if key < x.key else x.right
    if y is None:  # Tが空の場合
        root = Node(key)
    elif key < y.key:
        y.left = Node(key)
    else:
        y.right = Node(key)

def in_order(node):
    if node is None:
        return ''
    return in_order(node.left) + f' {node.key}' + in_order(node.right)
def pre_order(node):
    if node is None:
        return ''
    return f' {node.key}' + pre_order(node.left) + pre_order(node.right)
input()
for e in sys.stdin:
    if e[0] == 'i':
        insert(int(e[7:]))
    elif e[0] == 'd':
        delete(int(e[7:]))
    elif e[0] == 'f':
        print('yes' if find(int(e[5:])) else 'no')
    else:
        print(in_order(root))
        print(pre_order(root))
