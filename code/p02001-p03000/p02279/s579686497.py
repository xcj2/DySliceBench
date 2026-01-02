class Node:
    def __init__(self, parent, left, right):
        self.parent = parent
        self.left = left
        self.right = right


n = int(input())

node = {k: Node(-1, -1, -1) for k in range(n)}

for u in range(n):
    tmp = list(map(int, input().split()))
    if tmp[1] == 0:
        continue
    node[tmp[0]].left = tmp[2]
    node[tmp[2]].parent = tmp[0]
    prev_sibling = tmp[2] 
    for sib in tmp[3:]:
        node[prev_sibling].right = sib
        node[sib].parent = tmp[0]
        prev_sibling = sib

def get_depth(node, u):
    d = 0
    while node[u].parent is not -1:
        u = node[u].parent
        d += 1
    return d


def list_children(node, u):
    chilren = []
    c = node[u].left
    while c is not -1:
        chilren.append(c)
        c = node[c].right
    return chilren


for i in range(n):
    node_id = i
    node_parent = node[i].parent
    node_depth = get_depth(node, i)
    node_children = list_children(node, i)
 
    if node_parent == -1:
        node_type = "root"
    elif len(node_children) > 0 :
        node_type = "internal node"
    else:
        node_type = "leaf"

    print("node {}: parent = {}, depth = {}, {}, {}".format(node_id, node_parent, node_depth, node_type, node_children))

