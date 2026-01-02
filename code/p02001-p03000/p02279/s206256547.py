# coding: utf-8
# Your code here!
class Tree:
    def __init__(self, parent, left_child, right_sib):
        self.left_child = left_child
        self.right_sib = right_sib
        self.parent = parent
    

def getDepth(T, u):
    d = 0
    while T[u].parent is not None:
        u = T[u].parent
        d += 1
    return d

def getChildren(T, u):
    Children = []
    c = T[u].left_child
    while c is not None:
        Children.append(str(c))
        c = T[c].right_sib
    if len(Children) != 0:
        return "[" + ", ".join(Children) + "]"
    else:
        return "[]"

n = int(input().rstrip())

T = []
for _ in range(n):
    T.append(Tree(None, None, None))

for _ in range(n):
    inputs = list(map(int, input().rstrip().split(" ")))
    u = inputs[0]
    k = inputs[1]
    children = inputs[2:] if k > 0 else [None]
    T[u].left_child = children[0]
    if k > 0:
        for i, child in enumerate(children):
            T[child].parent = u
            T[child].right_sib = children[i+1] if i+1 < len(children) else None

def print_info(T, u):
    parent = T[u].parent
    if parent is None:
        parent = -1
    depth = getDepth(T, u)
    children = getChildren(T, u)
    type_ = "root" if parent == -1 else "leaf" if children == "[]" else "internal node"
    
    print("node {}: parent = {}, depth = {}, {}, {}".format(u, parent, depth, type_ ,children if type_ != "leaf" else "[]"))

for u in range(n):
    print_info(T, u)
    
   
    
    

