
null = -1

class Node:
    def __init__(self):
        self.parent = null
        self.left = null
        self.right = null
        self.id = null
        self.depth = null
        self.height = null
        self.sibling = null
        self.type = null
        self.degree = 0
        
    
def setDepth(u, d):
    if u == null:
        return  
    Tree[u].depth = d
    setDepth(Tree[u].left, d + 1)
    setDepth(Tree[u].right, d + 1)
    
def setHeight(u):
    h1 = 0
    h2 = 0
    if Tree[u].left != null:
        h1 = setHeight(Tree[u].left) + 1
    if Tree[u].right != null:
        h2 = setHeight(Tree[u].right) + 1
    Tree[u].height = max(h1, h2)
    return Tree[u].height

def setType():
    global root
    for i in range(n):
        if Tree[i].parent == null:
            Tree[i].type = "root"
            root = i
        elif Tree[i].left == null and Tree[i].right == null:
            Tree[i].type = "leaf"
        else:
            Tree[i].type = "internal node"
            
def getSibling(i):
    if Tree[i].parent == null:
        return null
    elif Tree[Tree[i].parent].left != i and Tree[Tree[i].parent].left != null:
        return Tree[Tree[i].parent].left
    elif Tree[Tree[i].parent].right != i and Tree[Tree[i].parent].right != null:
        return Tree[Tree[i].parent].right
    return null
        
Tree = []
root = 0

n = int(input())
for i in range(n):
    Tree.append(Node())
    
for i in range(n):
    tmp = list(map(int, input().split()))
    
    Tree[tmp[0]].id = tmp[0]
    
    if tmp[1] != -1:
        Tree[tmp[0]].left = tmp[1]
        Tree[tmp[1]].parent = tmp[0]
        Tree[tmp[0]].degree += 1
    if tmp[2] != -1:
        Tree[tmp[0]].right = tmp[2]
        Tree[tmp[2]].parent = tmp[0]
        Tree[tmp[0]].degree += 1

setType()
setDepth(root, 0)
setHeight(root)

for i in range(n):
    #print(Tree[i].depth, Tree[i].height)
    print("node", Tree[i].id, end = "")
    print(": parent =", Tree[i].parent, end = "")
    print(", sibling =",getSibling(i), end = "")
    print(", degree =",Tree[i].degree, end = "")
    print(", depth =",Tree[i].depth, end = "")
    print(", height =",Tree[i].height, end = "")
    print(",", Tree[i].type)
    











