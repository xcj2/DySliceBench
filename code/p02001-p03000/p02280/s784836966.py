#ALDS1_7_B
N = int(input())
answer1= []

def get_parent(node):
    parent = -1
    if "parent" in node:
        return node["parent"]
    return parent

def get_depth(node):
    depth = 0
    while "parent" in node:
        depth += 1
        parent = node["parent"]
        node = rooted_tree[parent]
    return depth

def get_node_type(node):
    if "parent" not in node:
        return "root"
    if node["left"] == -1 and node["right"] == -1:
        return "leaf"
    return "internal node"

def get_sibling(id, node):
    sibling = -1
    if "parent" not in node:
        return sibling
    parent_rchild= rooted_tree[node["parent"]]["right"]
    parent_lchild= rooted_tree[node["parent"]]["left"]
    if id == parent_rchild:
        sibling = parent_lchild
    else:
        sibling = parent_rchild
    return sibling

def get_degree(node):
    degree = 0
    if node["left"] > -1:
        degree += 1
    if node["right"] > -1:
        degree += 1        
    return degree

def get_height(node):
    h1 = h2 = 0
    if node["right"] > -1:
        h1 = get_height(rooted_tree[node["right"]]) + 1
    if node["left"] > -1:
        h2 = get_height(rooted_tree[node["left"]]) + 1
    h =  max(h1, h2)
    return h

rooted_tree = [{} for i in range(N)]
for _ in range(N):
    row = input()
    id, left, right = list(map(int, row.split()))
    rooted_tree[id]["right"] = right
    rooted_tree[id]["left"] = left
    #子供のparentを左右で設定する。
    if left > -1:
        left_child_id = left
        rooted_tree[left_child_id]["parent"] = id
    if right > -1:
        right_child_id = right
        rooted_tree[right_child_id]["parent"] = id

for id in range(N):
    node = rooted_tree[id]
    parent = get_parent(node)
    sibling = get_sibling(id, node)
    degree = get_degree(node)
    depth = get_depth(node)
    height = get_height(node)
    node_type = get_node_type(node)
    print("node {}: parent = {}, sibling = {}, degree = {}, depth = {}, height = {}, {}".format(id, parent, sibling, degree, depth, height, node_type))
