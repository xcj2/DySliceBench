class Node():
    def __init__(self, parent = -1, left = -1, right = -1, depth = 0, height = -1, degree = 0):
        self.parent = parent
        self.left = left
        self.right = right
        self.depth = depth
        self.height = height
        self.degree = degree

def input_depth(node, i, n):
    node[i].depth = n
    if node[i].left != -1:
        input_depth(node, node[i].left, n + 1)
    if node[i].right != -1:
        input_depth(node, node[i].right, n + 1)

def input_height(node, i):
    hl = 0
    hr = 0
    if node[i].left != -1:
        input_height(node, node[i].left)
        hl = node[node[i].left].height + 1
    if node[i].right != -1:
        input_height(node, node[i].right)
        hr = node[node[i].right].height + 1
    node[i].height = max(hl, hr)

def print_node(node, i):
    print("node " + str(i) + ": ", end = "")
    print("parent = " + str(node[i].parent) + ", ", end = "")
    if node[i].parent == -1:
        print("sibling = -1, ", end = "")
    elif i == node[node[i].parent].left:
        print("sibling = " + str(node[node[i].parent].right) + ", ", end = "")
    else:
        print("sibling = " + str(node[node[i].parent].left) + ", ", end = "")
    print("degree = " + str(node[i].degree) + ", ", end = "")
    print("depth = " + str(node[i].depth) + ", ", end = "")
    print("height = " + str(node[i].height) + ", ", end = "")
    if node[i].parent == -1:
        print("root")
    elif node[i].degree == 0:
        print("leaf")
    else:
        print("internal node")
        
n = int(input())
ns = [Node() for i in range(n)]
for i in range(n):
    p, l, r = map(int, input().split())
    if l != -1:
        ns[p].left = l
        ns[p].degree += 1
        ns[l].parent = p
    if r != -1:
        ns[p].right = r
        ns[p].degree += 1
        ns[r].parent = p

for i in range(n):
    if ns[i].parent == -1:
        input_depth(ns, i, 0)
        input_height(ns, i)
        break

for i in range(n):
    print_node(ns, i)



