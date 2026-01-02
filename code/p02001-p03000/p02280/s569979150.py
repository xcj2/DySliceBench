class Node():
    def __init__(self):
        self.parent = None
        self.left = None
        self.right = None
        self.depth = None
        self.height = None
        self.type = None

n = int(input())

# preparing the tree
tree = []
for _ in range(n):
    tree.append(Node())
for _ in range(n):
    id, left, right = map(int, input().split())
    if left > -1:
        tree[id].left = left
        tree[left].parent = id
    if right > -1:
        tree[id].right = right
        tree[right].parent = id
        
        
def get_type(id):
    if tree[id].parent is None:
        return 'root'
    elif (tree[id].left is None) and (tree[id].right is None):
        return 'leaf'
    else:
        return 'internal node'

# recursively set the depth of each node    
def set_depth(id, d):
    tree[id].depth = d
    if tree[id].left is not None:
        set_depth(tree[id].left, d+1)
    if tree[id].right is not None:
        set_depth(tree[id].right, d+1)

# recursively set the height of each node
def set_height(id):
    if id is None:
        pass
    elif tree[id].type == 'leaf':
        tree[id].height = 0
    else:
        left_id = tree[id].left
        right_id = tree[id].right
        set_height(left_id)
        set_height(right_id)
        
        
        tree[id].height = max(
                0 if left_id is None else tree[left_id].height + 1,  
                0 if right_id is None else tree[right_id].height + 1 
            )
         

def get_num_child(id):
    return (tree[id].left is not None)  + (tree[id].right is not None)

def get_sibling(id):
    if tree[id].type == 'root':
        out = None
    else:
        parent_node = tree[tree[id].parent]
        out = (parent_node.right if (parent_node.left == id) else parent_node.left)
    return (-1 if out is None else out)

# ==========

for id in range(n):
    tree[id].type = get_type(id)
    if tree[id].type == 'root':
        root_id = id
set_depth(root_id, 0)
set_height(root_id)

for id in range(n):
    print(f"node {id}: parent = {-1 if tree[id].parent is None else tree[id].parent}, sibling = {get_sibling(id)}, degree = {get_num_child(id)}, depth = {tree[id].depth}, height = {tree[id].height}, {tree[id].type}")

