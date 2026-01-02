class Node():
    def __init__(self):
        self.parent = -1
        self.left = -1
        self.right = -1
        self.depth = 0
        self.sibling = -1
        self.degree = 0
        self.height = -1
        return

def getAncestor(t, n):
    for i in range(n):
        if t[i].parent == -1:
            return i

def preOrderWolk(t, u, load=[]):
    load.append(u)
    if t[u].left != -1:
        load = preOrderWolk(t, t[u].left, load)
    if t[u].right != -1:
        load = preOrderWolk(t, t[u].right, load)
    return load

def inOrderTreeWalk(t, u, load=[]):
    if t[u].left != -1:
        load = inOrderTreeWalk(t, t[u].left, load)
    load.append(u)
    if t[u].right != -1:
        load = inOrderTreeWalk(t, t[u].right, load)
    return load

def PostOrderTreeWalk(t, u, load=[]):
    if t[u].left != -1:
        load = PostOrderTreeWalk(t, t[u].left, load)
    if t[u].right != -1:
        load = PostOrderTreeWalk(t, t[u].right, load)
    load.append(u)
    return load
    

import sys

n = int(input())
t = []
for _ in range(n):
    t.append(Node())

for i in range(n):
    a = list(map(int, sys.stdin.readline().split()))
    m = a[0]
    t[m].left = a[1]
    t[m].right = a[2]
    if a[1] != -1:
        t[m].degree += 1
        t[a[1]].parent = m
        t[a[1]].sibling = a[2]
    if a[2] != -1:
        t[m].degree += 1
        t[a[2]].parent = m
        t[a[2]].sibling = a[1]

r = getAncestor(t,n)
ptw = preOrderWolk(t, r, [])
itw = inOrderTreeWalk(t, r, [])
post = PostOrderTreeWalk(t, r, [])

print('Preorder')
print('',*ptw)
print('Inorder')
print('',*itw)
print('Postorder')
print('',*post)

    
