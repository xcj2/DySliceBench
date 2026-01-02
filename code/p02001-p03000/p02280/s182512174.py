class Node:
    def __init__(self, parent, left, right):
        self.parent = parent
        self.left = left
        self.right = right


n = int(input())
node = {key: Node(-1, -1, -1) for key in range(n)} 
for i in range(n):
    tmp = list(map(int, input().split()))
    if tmp[1] != -1:
        node[tmp[0]].left = tmp[1]
        node[tmp[1]].parent = tmp[0]
    if tmp[2] != -1:
        node[tmp[0]].right = tmp[2]
        node[tmp[2]].parent = tmp[0]

def get_depth(node, D, u, d):
    D[u] = d
    if node[u].left != -1:
        get_depth(node, D, node[u].left, d+1)
    if node[u].right != -1:
        get_depth(node, D, node[u].right, d+1)


def get_height(node, H, u):
    h_l = 0   
    h_r = 0
    if node[u].left != -1:
        h_l = get_height(node, H, node[u].left) + 1
    if node[u].right != -1:
        h_r = get_height(node, H, node[u].right) + 1
    ans = max(h_l, h_r)
    H[u] = ans
    return ans

def get_sibling(node, u):
    parent = node[u].parent
    if parent is -1:
        return -1
    if node[parent].left != -1 and node[parent].left != u:
        ans = node[parent].left
    elif node[parent].right != -1 and node[parent].right != u:
        ans = node[parent].right
    else :
        ans = -1
    return ans

def get_degree(node, u):
    deg = 0
    if node[u].left != -1:
        deg +=1
    if node[u].right != -1:
        deg +=1
    return deg

for k, v in node.items():
    if v.parent is -1:
        root = k

D = {}
get_depth(node, D, root, 0)
H = {}
get_height(node, H, root)

def print_for_a_node(u):
    parent = node[u].parent
    sib = get_sibling(node, u)
    deg = get_degree(node, u)

    node_type = 'internal node' if deg != 0 else 'leaf'
    if parent == -1:
        node_type = 'root'

    print(f'node {u}: parent = {parent}, sibling = {sib}, degree = {deg}, depth = {D[u]}, height = {H[u]}, {node_type}')


for i in range(n):
    print_for_a_node(i)

