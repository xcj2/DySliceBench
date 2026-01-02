class Node():
    def __init__(self):
        self.left = -1
        self.right = -1
        self.parent = -1
        self.sibling = -1
        self.degree = -1
        self.depth = -1
        self.height = -1
        self.type = None
        
n = int(input())
A = [list(map(int, input().split())) for _ in range(n)]

T = [Node() for i in range(25)]

for (idx, left, right) in A:
    T[idx].left = left
    T[idx].right = right
    T[idx].degree = ((left!=-1) + (right!=-1))
    if left != -1:
        T[left].parent = idx
    if right != -1:
        T[right].parent = idx
    if (left!=-1) & (right!=-1):
        T[left].sibling = right
        T[right].sibling = left
        
for idx in range(n):
    if T[idx].parent == -1:
        T[idx].type = 'root'
        root = idx
    elif T[idx].degree == 0:
        T[idx].type = 'leaf'
    else:
        T[idx].type = 'internal node'
        

def set_depth(u, d):
    T[u].depth = d
    if T[u].left != -1:
        set_depth(T[u].left, d+1)
    if T[u].right != -1:
        set_depth(T[u].right, d+1)
        
def set_height(u):
    hl = hr = 0
    if T[u].left != -1:
        hl = set_height(T[u].left) + 1
    if T[u].right != -1:
        hr = set_height(T[u].right) + 1
    h = max(hl, hr)
    T[u].height = h
    return h

set_depth(root, 0)
_ = set_height(root)

for idx in range(n):
    print('node {}: parent = {}, sibling = {}, degree = {}, depth = {}, height = {}, {}'.format(idx, T[idx].parent, T[idx].sibling, T[idx].degree, T[idx].depth, T[idx].height, T[idx].type))
