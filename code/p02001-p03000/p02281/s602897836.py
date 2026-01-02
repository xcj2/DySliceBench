import sys
sys.setrecursionlimit(10**7)

class Node:
    def __init__(self, parent, left, right):
        self.parent = parent
        self.left = left  
        self.right = right

def preParse(T, u, pre):
    if u == -1:
        return
    pre.append(u)
    preParse(T, T[u].left, pre)
    preParse(T, T[u].right, pre)

def inParse(T, u, inl):
    if u == -1:
        return
    inParse(T, T[u].left, inl)
    inl.append(u)
    inParse(T, T[u].right, inl)

def postParse(T, u, post):
    if u == -1:
        return
    postParse(T, T[u].left, post)
    postParse(T, T[u].right, post)
    post.append(u)

n = int(input())
T = {k: Node(-1, -1, -1) for k in range(n)}  

for _ in range(n):
    tmp = list(map(int, input().split()))
    T[tmp[0]].left = tmp[1]  
    T[tmp[0]].right = tmp[2] 
    if tmp[1] != -1:
        T[tmp[1]].parent = tmp[0]  
    if tmp[2] != -1:
        T[tmp[2]].parent = tmp[0]

for id, node in T.items():
    if node.parent == -1:
        ROOT = id

pre, inl, post = [], [], []
preParse(T, ROOT, pre)
inParse(T, ROOT, inl)
postParse(T, ROOT, post)

print('Preorder')
print('', *pre)
print('Inorder')
print('', *inl)
print('Postorder')
print('', *post)
