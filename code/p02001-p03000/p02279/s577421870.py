n = int(input())

class Node():
    def __init__(self):
        self.parent = None
        self.left_child = None
        self.right_sibling = None
        self.type = None

tree = []
for _ in range(n):
    tree.append(Node())

for _ in range(n):
    tmp = list(map(int, input().split()))
    id = tmp[0]
    degree = tmp[1]
    children = tmp[2:]
    if degree > 0:
        tree[id].left_child = children[0]
        for (cnt, child) in enumerate(children):
            tree[child].parent = id
            if cnt < degree - 1:
                tree[child].right_sibling = children[cnt + 1]
    
    
def get_depth(id):
    out = 0
    node = tree[id]
    while node.parent is not None:
        out += 1
        node = tree[node.parent]
    return out

def get_children(id):
    left_child_id = tree[id].left_child
    if left_child_id is None:
        return []
    node = tree[left_child_id]
    out = [left_child_id]
    while node.right_sibling is not None:
        out.append(node.right_sibling)
        node = tree[node.right_sibling]
    return out

def get_type(id):
    node = tree[id]
    if node.parent is None:
        return 'root'
    elif node.left_child is not None:
        return 'internal node'
    else:
        return 'leaf'
    
for id in range(n):
    print(f"node {id}: parent = {-1 if tree[id].parent is None else tree[id].parent}, depth = {get_depth(id)}, {get_type(id)}, {get_children(id)}")

