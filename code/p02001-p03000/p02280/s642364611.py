#coding:utf-8

n = int(input())
T = [list(map(int, input().split())) for i in range(n)]
A = [False for i in range(n)]

class binaryTree:
    def __init__(self, node, x=-1):
        self.node = node
        self.p = x
    
    def partialTree(self,tree,left, right):
        node = tree.node
        if left != -1:
            if A[left]:
                A[left].p = tree
                tree.l = A[left]
            else:
                tree.l = binaryTree(left, node)
                A[left] = tree.l
                tree.l.p = tree
        else:
            tree.l = binaryTree(left, node)
            tree.l.node = -1
            
        if right != -1:
            if A[right]:
                A[right].p = tree
                tree.r = A[right]
            else:
                tree.r = binaryTree(right, node)
                A[right] = tree.r
                tree.r.p = tree
        else:
            tree.r = binaryTree(right, node)
            tree.r.node = -1
            
def searchParent():
    p_tree = A[0]
    while p_tree.p != -1:
        p_tree = p_tree.p
    return p_tree

     
def setHeight(tree):
    h1 = h2 = 0
    if tree.l.node != -1:
        h1 = setHeight(tree.l) + 1
    if tree.r.node != -1:
        h2 = setHeight(tree.r) + 1
    if tree.l.node == -1 and tree.r.node == -1:
        tree.hei = 0
        return 0
    tree.hei = max(h1,h2)
    return max(h1, h2)

def setDepth(tree,depth):
    tree.dep = depth
    depth += 1
    if tree.l.node != -1:
        setDepth(tree.l,depth)

    if tree.r.node != -1:
        setDepth(tree.r,depth)

def getSibling(tree):
    if tree.p == -1:
        return -1
    if tree.p.l.node != -1 and tree.p.l.node != tree.node:
        return tree.p.l.node
    if tree.p.r.node != -1 and tree.p.r.node != tree.node:
        return tree.p.r.node
    return -1

        
def makeTree():
    for i in range(n):
        t = T[i]
        node = t[0]
        left = t[1]
        right = t[2]
        if A[node]:
            tree = A[node]
        else:
            tree = binaryTree(node)
            A[node] = tree
        binaryTree.partialTree(binaryTree, tree,left,right)

makeTree()
p_tree = searchParent()
setHeight(p_tree)
depth = 0
setDepth(p_tree,depth)


for i in range(n):
    tree = A[i]
    tree.sib = getSibling(tree)
    deg = 0
    if tree.r.node != -1:
        deg += 1

    if tree.l.node != -1:
        deg += 1

    if tree.p == -1:
        kind = "root"
    else:
        if deg == 0:
            kind = "leaf"
        else:
            kind = "internal node"

    ID = i
    if tree.p == -1:
        parent = -1
    else:
        parent = tree.p.node
    sibling = tree.sib
    degree = deg
    depth = tree.dep
    height = tree.hei

    print("node {}: parent = {}, sibling = {}, degree = {}, depth = {}, height = {}, {}"\
          .format(ID, parent, sibling, degree, depth, height, kind))
