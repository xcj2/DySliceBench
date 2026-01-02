"""Binary Trees."""

class Node:
    def __init__(self, num, leftChild, rightChild):
        self.id = num
        self.parent = -1
        self.sibling = -1
        self.degree = 0
        self.depth = 0
        self.height = 0
        self.type = 'leaf'
        self.leftChild = leftChild
        self.rightChild = rightChild
        
    def show_info(self):
        print('node {}:'.format(self.id), 'parent = {},'.format(self.parent),
              'sibling = {},'.format(self.sibling),
              'degree = {},'.format(self.degree),
              'depth = {},'.format(self.depth),
              'height = {},'.format(self.height),
              '{}'.format(self.type))


def set_attributes(n_i, parent, sibling, depth):
    h1 = 0
    h2 = 0
    node = T[n_i]
    lc = node.leftChild
    rc = node.rightChild
    node.parent = parent
    node.sibling = sibling
    node.depth = depth
    if lc != -1:
        node.degree += 1
        node.type = 'internal node'
        h1 = set_attributes(lc, n_i, rc, depth + 1) + 1
    if rc != -1:
        node.degree += 1
        node.type = 'internal node'
        h2 = set_attributes(rc, n_i, lc, depth + 1) + 1
    node.height = max(h1, h2)
    return node.height



import sys

n = int(sys.stdin.readline())

T = [None] * n

rt_n = int(n * (n - 1) / 2)

for x in sys.stdin.readlines():
    num, leftChild, rightChild = list(map(int, x.split()))
    node = Node(num, leftChild, rightChild)
    T[num] = node
    rt_n -= (max(0, leftChild) + max(0, rightChild))

set_attributes(rt_n, -1, -1, 0)

T[rt_n].type = 'root'

for n in T:
    n.show_info()