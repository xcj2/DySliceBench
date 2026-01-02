class Node:
    def __init__(self,left,right):
        self.left = left
        self.right = right
        self.parent = -1
        self.sibling = -1
        self.degree = 0
        self.depth = 0
        self.height = 0
        self.type = 'internal node'

def setParentAndTypeAndSibling(tree):
    result = -1
    for i, tmp in enumerate(tree):
        if tmp.left != -1:
            tree[tmp.left].parent = i
        if tmp.right != -1:
            tree[tmp.right].parent = i

    for i, tmp in enumerate(tree):
        if tmp.parent == -1:
            tmp.type = 'root'
            result = i
        elif tmp.left == -1 and tmp.right == -1:
            tmp.type = 'leaf'
        else:
            tmp.type = 'internal node'

        if tmp.left == -1 and tmp.right == -1:
            tmp.degree = 0
        elif tmp.left != -1 and tmp.right != -1:
            tmp.degree = 2
            tree[tmp.left].sibling = tmp.right
            tree[tmp.right].sibling = tmp.left
        else:
            tmp.degree = 1
    return result

def setdepth(tree,i,d):
    tree[i].depth = d
    if tree[i].left != -1:
        setdepth(tree,tree[i].left,d+1)
    if tree[i].right != -1:
        setdepth(tree,tree[i].right,d+1)
    return

def findParentAndsetHeight(tree,i,h):
    tree[i].height = max(h,tree[i].height)
    if tree[i].parent != -1:
        findParentAndsetHeight(tree,tree[i].parent,h+1)
    return

def setHeight(tree):
    for tmp in tree:
        if tmp.type == 'leaf':
            tmp.height = 0
            findParentAndsetHeight(tree,tmp.parent,1)

if __name__ == '__main__':
    n = int(input())
    tree = [None]*n

    for i in range(0,n):
        tmp = list(map(int,input().split()))
        tree[tmp[0]] = Node(tmp[1],tmp[2])
    
    root = setParentAndTypeAndSibling(tree)
    setdepth(tree,root,0)
    setHeight(tree)
    for i, tmp in enumerate(tree):
        print("node {}: parent = {}, sibling = {}, degree = {}, depth = {}, height = {}, {}".format(i,tmp.parent,tmp.sibling,tmp.degree,tmp.depth,tmp.height,tmp.type))