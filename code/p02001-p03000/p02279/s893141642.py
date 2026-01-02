import sys
def input():
    return sys.stdin.readline()[:-1]
    
class Node:
    def __init__(self):
        self.parent = -1
        self.left = -1
        self.right = -1
        self.depth = -1
        self.c = []
        
T = [Node() for _ in range(100_000)]
n = int(input())
A = [list(map(int, input().split())) for _ in range(n)]

for i,a in enumerate(A):
    idx, k = a[:2]
    for j in range(k):
        c = a[2+j]
        T[idx].c.append(c)
        if j==0:
            T[idx].left = c
        else:
            T[left].right = c
        left = c
        T[c].parent = idx

for idx in range(n):
    if T[idx].parent == -1:
        root = idx
   
def set_depth(u,d):
    T[u].depth = d
    for c in T[u].c:
        set_depth(c,d+1)
        
set_depth(root, 0)
    
for idx in range(n):
    print('node {}: parent = {}, depth = {}, {}, {}'.format(idx, T[idx].parent, T[idx].depth, ('root' if T[idx].parent==-1 else 'leaf' if T[idx].left==-1 else 'internal node'), T[idx].c))
