class Node():
    def __init__(self, parent = -1, left = -1, right = -1):
        self.parent = parent
        self.left = left
        self.right = right

def postorder(ns, i, post):
    if ns[i].left != -1:
        postorder(ns, ns[i].left, post)
    if ns[i].right != -1:
        postorder(ns, ns[i].right, post)
    post.append(str(i + 1))

def poio_node(ns, po, io):
    p = po[0]
    i = io.index(p)
    if i != 0:
        ns[p].left = po[1]
        ns[po[1]].parent = p
        poio_node(ns, po[1:i + 1], io[:i])
    if i != len(io) -1:
        ns[p].right = po[i + 1]
        ns[po[1 + i]].parent = p
        poio_node(ns, po[i + 1:], io[i + 1:])

def min1(n):
    return n - 1
    
n = int(input())
po = list(map(int, input().split()))
io = list(map(int, input().split()))
po = list(map(min1, po))
io = list(map(min1, io))
ns = [Node() for i in range(n)]

poio_node(ns, po, io)

post = []
postorder(ns, po[0], post)
print(" ".join(post))
