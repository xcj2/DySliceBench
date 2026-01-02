class Node:
    def __init__(self, idnum):
        self.id = idnum
        self.parent = -1
        self.left = -1
        self.right = -1
        self.sibling = -1
        self.degree = 0
        self.depth = 0
        self.height = 0
        self.type = "root"
#input
n = int(input())
T = [Node(i) for i in range(n)]
for ni in range(n):
    idnum, left, right = [int(i) for i in input().split()]
    T[idnum].left = left
    T[idnum].right = right
    T[idnum].degree = 2 - [left, right].count(-1)
    if left != -1:
        T[left].parent = idnum
        T[left].sibling = right
    if right != -1:
        T[right].parent = idnum
        T[right].sibling = left


#teach node type
leaf_id = []
for ni in range(n):
    if T[ni].parent == -1:
        T[ni].type = "root"
        root_id = ni
    elif T[ni].degree == 0:
        T[ni].type = "leaf"
        leaf_id.append(ni)
    else:
        T[ni].type = "internal node"

def setDepth(p, d):
    T[p].depth = d
    if T[p].left != -1:
        setDepth(T[p].left, d+1)
    if T[p].right != -1:
        setDepth(T[p].right, d+1)
setDepth(root_id,0)

def setHeight(p, h):
    if T[p].height < h:
        T[p].height = h
    if T[p].parent != -1:
        setHeight(T[p].parent, h+1)

for l in leaf_id:
    setHeight(l, 0)

#output
for ni in range(n):
    print("node "+str(T[ni].id)+\
        ": parent = "+str(T[ni].parent)+\
            ", sibling = "+str(T[ni].sibling)+\
                ", degree = "+str(T[ni].degree)+\
                    ", depth = "+str(T[ni].depth)+\
                        ", height = "+str(T[ni].height)+\
                            ", "+T[ni].type)
