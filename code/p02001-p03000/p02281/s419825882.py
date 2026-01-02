n = int(input())
class Node(object):
    def __init__(self, p, l, r):
        self.p = p
        self.l = l
        self.r = r

nodes = [Node(None, None, None) for i in range(n)]

for i in range(n):
    id, left, right = map(int, input().split())
    nodes[id].l = left
    nodes[id].r = right
    if left != -1:
        nodes[left].p = i
    if right != -1:
        nodes[right].p = i

def pre(node,path):
    path.append(node)
    if nodes[node].l != -1:
        pre(nodes[node].l,path)
    if nodes[node].r != -1:
        pre(nodes[node].r,path)

def ino(node,path):
    if nodes[node].l != -1:
        ino(nodes[node].l,path)
    path.append(node)
    if nodes[node].r != -1:
        ino(nodes[node].r,path)

def post(node,path):
    if nodes[node].l != -1:
        post(nodes[node].l,path)
    if nodes[node].r != -1:
        post(nodes[node].r,path)
    path.append(node)

for ind, n in enumerate(nodes):
    if n.p == None:
        root = ind
        break
print('Preorder')
l = []
pre(root, l)
print(' ' +  ' '.join(map(str, l)))
print('Inorder')
l = []
ino(root, l)
print(' ' +  ' '.join(map(str, l)))
print('Postorder')
l = []
post(root,l)
print(' ' + ' '.join(map(str, l)))