from enum import Enum, auto
import sys

class NodeType(Enum):
    LEAF = auto()
    INTERNAL_NODE = auto()
    ROOT = auto()

class BinaryTreeNode():
    def __init__(self, parent=None, left=None, right=None):
        self.parent = parent
        self.left = left
        self.right = right
        self.sibling = None
        self.degree = None
        self.depth = None
        self.height = None
        self.type = None

n = int(input())
nodes = [BinaryTreeNode() for i in range(n)]
for i in range(n):
    id, left, right = list(map(int, input().split(' ')))
    degree = 0
    if left != -1:
        degree += 1
        nodes[id].left = left
        nodes[left].parent = id
        nodes[left].sibling = right
    if right != -1:
        degree += 1
        nodes[id].right = right
        nodes[right].parent = id
        nodes[right].sibling = left
    nodes[id].degree = degree
    if degree == 0:
        nodes[id].type = NodeType.LEAF
    else:
        nodes[id].type = NodeType.INTERNAL_NODE

root = 0
for i in range(n):
    if nodes[i].parent == None:
        root = i
        nodes[i].type = NodeType.ROOT

def set_depth(u, d):
    nodes[u].depth = d
    if nodes[u].left != None: set_depth(nodes[u].left, d+1)
    if nodes[u].right != None: set_depth(nodes[u].right, d+1)

def set_height(u):
    h1, h2 = 0, 0
    if nodes[u].left != None:
        h1 = set_height(nodes[u].left) + 1
    if nodes[u].right != None:
        h2 = set_height(nodes[u].right) + 1
    nodes[u].height = h1 if h1 > h2 else h2
    return nodes[u].height

set_depth(root, 0)
set_height(root)

for i in range(n):
    parent = -1 if nodes[i].parent == None else nodes[i].parent
    sibling = -1 if nodes[i].sibling == None else nodes[i].sibling
    type = ''
    if nodes[i].type == NodeType.INTERNAL_NODE:
        type = 'internal node'
    elif nodes[i].type == NodeType.LEAF:
        type = 'leaf'
    elif nodes[i].type == NodeType.ROOT:
        type = 'root'
    print('node %d: parent = %d, sibling = %d, degree = %d, depth = %d, height = %d,'%(i, parent, sibling, nodes[i].degree, nodes[i].depth, nodes[i].height), type)

