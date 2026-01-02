class Tree:
    def __init__(self,parent,left,right):
        self.parent = parent
        self.left = left
        self.right = right
        self.sibling = -1
        self.degree = 0
        self.depth = -1
        self.height = -1

def getdepth(u):
    for i in range(N):
        depth = 0
        j = i
        while trees[j].parent != -1:
            j = trees[j].parent
            depth += 1
        trees[i].depth = depth

def getheight(u):
    hleft = hright = 0
    if trees[u].left != -1:
        hleft = getheight(trees[u].left) + 1
    if trees[u].right != -1:
        hright = getheight(trees[u].right) + 1

    trees[u].height = hleft if hleft > hright else hright
    return trees[u].height


N = int(input())
# ?????????
trees = [Tree(-1,-1,-1) for i in range(N)]
for i in range(N):
    l = list(map(int, input().split()))
    no = l[0]
    left = l[1]
    right = l[2]
    trees[no].left = left
    trees[no].right = right
    if left != -1:
        trees[left].parent = no
        trees[left].sibling = right
        trees[no].degree += 1
    if right != -1:
        trees[right].parent = no
        trees[right].sibling = left
        trees[no].degree += 1

r = 0
for i in range(N):
    if trees[i].parent == -1:
        r = i

getdepth(r)
getheight(r)

for i in range(N):
    type = ""
    if trees[i].parent == -1: type = "root"
    elif trees[i].left == -1 and trees[i].right == -1: type = "leaf"
    else: type = "internal node"

    print("node {0}: parent = {1}, sibling = {2}, degree = {3}, depth = {4}, height = {5}, {6}".format(
        i,
        trees[i].parent,
        trees[i].sibling,
        trees[i].degree,
        trees[i].depth,
        trees[i].height,
        type))