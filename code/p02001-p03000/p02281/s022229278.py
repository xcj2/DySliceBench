NIL = -1
n = int(input())

class Node():
    def __init__(self):
        self.id = NIL
        self.left = NIL
        self.right = NIL
        self.parent = NIL
        
    def __str__(self):
        return "id : {}, left : {}, right : {}, parent : {}".format(self.id, self.left, self.right, self.parent)

tree = [Node() for i in range(n)]
for i in range(n):
    row = list(map(int,input().split()))
    tree[row[0]].id = row[0]
    tree[row[0]].left = row[1]
    tree[row[0]].right = row[2]
    
    if(row[1] != NIL):
        tree[row[1]].parent = row[0]
    if(row[2] != NIL):
        tree[row[2]].parent = row[0]


def preParse(u, res):
    if(u == NIL):
        return 
    res += [u]
    preParse(tree[u].left, res)
    preParse(tree[u].right, res)
    return res

def inParse(u, res):
    if(u == NIL):
        return
    inParse(tree[u].left, res)
    res += [u]
    inParse(tree[u].right, res)
    return res

def postParse(u, res):
    if(u == NIL):
        return
    postParse(tree[u].left, res)
    postParse(tree[u].right, res)
    res += [u]
    return res

for i in range(n):
    if(tree[i].parent == -1):
        print("Preorder")
        print(" {}".format(" ".join([str(ss) for ss in preParse(tree[i].id, [])])))
        
        print("Inorder")
        print(" {}".format(" ".join([str(ss) for ss in inParse(tree[i].id, [])])))
        
        print("Postorder")
        print(" {}".format(" ".join([str(ss) for ss in postParse(tree[i].id, [])])))
        
        break
