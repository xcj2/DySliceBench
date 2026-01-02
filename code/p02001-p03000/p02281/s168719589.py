NIL = -1

class Node:
    def __init__(self, parent=NIL, left=NIL, right=NIL):
        self.parent = parent
        self.left = left
        self.right = right


def preParse(tree, u):
    if u == NIL:
        return
    print(' %d' % u, end='')
    preParse(tree, tree[u].left)
    preParse(tree, tree[u].right)


def inParse(tree, u):
    if u == NIL:
        return
    inParse(tree, tree[u].left)
    print(' %d' % u, end='') 
    inParse(tree, tree[u].right)


def postParse(tree, u):
    if u == NIL:
        return
    postParse(tree, tree[u].left)
    postParse(tree, tree[u].right)
    print(' %d' % u, end='') 


n = int(input())
tree = [Node() for i in range(n)]

for i in range(n):
    value, left, right = [int(v) for v in input().split()]
    tree[value].left = left
    tree[value].right = right
    if left != NIL:
        tree[left].parent = value
    if right != NIL:
        tree[right].parent = value

root = 0
for i in range(n):
    if tree[i].parent == NIL:
        root = i
        break

print('Preorder')
preParse(tree, root)
print()
print('Inorder')
inParse(tree, root)
print()
print('Postorder')
postParse(tree, root)
print()
