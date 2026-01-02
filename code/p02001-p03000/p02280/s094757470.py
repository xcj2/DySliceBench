# coding: utf-8
# Your code here!
class BinaryTree:
    def __init__(self, parent, left, right):
        self.parent = parent
        self.left = left
        self.right = right
        self.sibling = -1
    

T = []
n = int(input().rstrip())
 
for _ in range(n):
    T.append(BinaryTree(-1, -1, -1))

for i in range(n):
    input_line = list(map(int, input().rstrip().split(" ")))
    u, left, right = input_line
    T[u].left = left
    T[u].right = right
    if left != -1:
        T[left].parent = u
    if right != -1:
        T[right].parent = u
    if (left != -1) and (right != -1):
        T[left].sibling = right
        T[right].sibling = left

def get_degree(T, u):
    return int(T[u].left != -1) + int(T[u].right != -1)

def get_depth(T, u):
    d = 0
    while T[u].parent != -1:
        u = T[u].parent
        d += 1
    return d

for i, t in enumerate(T):
    if t.parent == -1:
        root = i
        break
H = [0] * n

def set_height(u):
    global H
    h1 = 0
    h2 = 0
    if T[u].left != -1:
        h1 = set_height(T[u].left) + 1
    if T[u].right != -1:
        h2 = set_height(T[u].right) + 1
    H[u] = max(h1, h2)
    return H[u]

set_height(root)

def print_info(T, u):
    node = u
    parent = T[u].parent
    sibling = T[u].sibling
    degree = get_degree(T, u)
    depth = get_depth(T, u)
    height = H[u]
    type_ = "root" if parent == -1 else "leaf" if degree == 0 else "internal node"
    print("node {}: parent = {}, sibling = {}, degree = {}, depth = {}, height = {}, {}".format(node, parent, sibling, degree, depth, height, type_))
    
for i in range(n):
    print_info(T, i)

