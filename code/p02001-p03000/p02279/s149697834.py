import sys
sys.setrecursionlimit(1000000)

class Node:
    def __init__(self, parent = -1, left = -1, right = -1, depth = 0):
        self.parent = parent
        self.left = left
        self.right = right
        self.depth = depth
    
def print_node(i):
    global node
    print("node " + str(i) + ": ", end = "")
    print("parent = " + str(node[i].parent) +", ", end = "")
    print("depth = " + str(node[i].depth) + ", ", end = "")
    if node[i].parent == -1:
        print("root, [", end = "")
    elif node[i].left != -1:
        print("internal node, [", end = "")
    else:
        print("leaf, [", end = "")
    if node[i].left != -1:
        print(str(node[i].left), end = "")
        j = node[i].left
        while node[j].right != -1:
            j = node[j].right
            print(", " + str(j), end = "")
    print("]")
            

n = int(input())
node = [Node() for i in range(n)]
def input_depth(i, n):
    global node
    node[i].depth = n
    if node[i].right != -1:
        input_depth(node[i].right, n)
    if node[i].left != -1:
        input_depth(node[i].left, n + 1)

for i in range(n):
    p, k, *c = list(map(int, input().split()))
    if k > 0:
        node[p].left = c[0]
    for j in range(k):
        node[c[j]].parent = p
        if j != k - 1:
            node[c[j]].right = c[j + 1]

for i in range(n):
    if node[i].parent == -1:
        input_depth(i, 0)
        break

for i in range(n):
    print_node(i)

    
