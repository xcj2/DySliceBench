def preParse(u, p):
    if u == -1:
        return p
    p += [u]
    preParse(left[u], p)
    preParse(right[u], p)

def inParse(u, p):
    if u == -1:
        return p
    inParse(left[u], p)
    p += [u]
    inParse(right[u], p)

def postParse(u, p):
    if u == -1:
        return p
    postParse(left[u], p)
    postParse(right[u], p)
    p += [u]

n = int(input())
parent = [-1] * n
left   = [-1] * n
right  = [-1] * n
preo = []
ino  = []
post = []

for i in range(n):
    p, l, r = map(int, input().split())
    left[p] = l
    right[p] = r
    if l != -1:
        parent[l] = p
    if r != -1:
        parent[r] = p

root = parent.index(-1)

preParse(root, preo)
inParse(root, ino)
postParse(root, post)

for i, j in zip(['Preorder', 'Inorder', 'Postorder'], [preo, ino, post]):
    print(i)
    print(' '+' '.join(map(str, j)))
