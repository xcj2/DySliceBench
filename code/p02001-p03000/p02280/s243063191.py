class Node:
    def __init__(self, parent, left, right):
        self.parent = parent
        self.left = left
        self.right = right

d = {}
def get_all_depth(t, u, p):
    d[u] = p
    if t[u].right is not None:
        get_all_depth(t, t[u].right, p+1)
    if t[u].left is not None:
        get_all_depth(t, t[u].left, p+1)

h = {}
def get_all_height(t, u):
    left, right = 0, 0
    if t[u].left is not None:
        left = get_all_height(t, t[u].left) + 1
    if t[u].right is not None:
        right = get_all_height(t, t[u].right) + 1
    tmp = max(left, right)
    h[u] = tmp
    return tmp

def get_sibling(t, u):
    par = t[u].parent
    if par is None:
        return -1
    left, right = t[par].left, t[par].right
    if left == u:
        if right is not None:
            return right
    elif left is not None:
        return left
    return -1

n = int(input())
t = {k: Node(None, None, None) for k in range(n)}
for _ in range(n):
    tmp = list(map(int, input().split()))
    if tmp[1] != -1:
        t[tmp[1]].parent = tmp[0] # 親
        t[tmp[0]].left = tmp[1] # 左の子
    if tmp[2] != -1:
        t[tmp[2]].parent = tmp[0] # 親
        t[tmp[0]].right = tmp[2] # 右の子

for node in range(n):
    if t[node].parent is None:
        get_all_depth(t, node, 0)
        get_all_height(t, node)
        break

for node in range(n):
    node_type = "internal node" if t[node].left is not None or t[node].right is not None else "leaf"
    if t[node].parent is None:
        node_type = "root"
        parent = -1
    else:
        parent = t[node].parent
    sibling = get_sibling(t, node)
    deg = 0
    if t[node].left is not None:
        deg += 1
    if t[node].right is not None:
        deg += 1
    print(  f"node {node}: parent = {parent}, sibling = {sibling}, "
            f"degree = {deg}, depth = {d[node]}, height = {h[node]}, {node_type}")
