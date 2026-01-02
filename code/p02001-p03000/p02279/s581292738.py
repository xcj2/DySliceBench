import sys
sys.setrecursionlimit(10**6)

class Node:
    def __init__(self):
        self.parent = -1
        self.left_child = None
        self.right_sibling = None

def get_children(node):
    c = node.left_child
    cs = []
    if c is not None:
        cs.append(c)
        c = nodes[int(node.left_child)]
        while c.right_sibling:
            c = c.right_sibling
            cs.append(c)
            c = nodes[int(c)]
    return cs

# def get_depth(index):
#     depth = 0
#     index = int(index)
#     while index:
#         index = int(nodes[index].parent)
#         depth += 1
#     return depth

def set_depth(i, depth):
    if depths[i] or i >= n:
        return
    depths[i] = depth
    node = nodes[i]
    if node.right_sibling:
        set_depth(int(node.right_sibling), depth)
    if node.left_child:
        set_depth(int(node.left_child), depth+1)

def get_root_index():
    for i, node in enumerate(nodes):
        if node.parent == -1:
            return i
            
def get_kind_of_tree(node):
    if node.parent == -1:
        return "root"
    if node.left_child:
        return "internal node"
    return "leaf"

if __name__ == "__main__":
    n = int(input())
    nodes = [Node() for _ in range(n)]
    depths = [None for _ in range(n)]
    for _ in range(n):
        data, number_of_children, *children = input().split()
        node = nodes[int(data)]
        for i, child_data in enumerate(children):
            if i == 0:
                node.left_child = child_data
            else:
                child.right_sibling = child_data
            child = nodes[int(child_data)]
            child.parent = int(data)
    root_node_index = get_root_index()
    set_depth(root_node_index, 0)
    for i, node in enumerate(nodes):
        children = get_children(node)
        print("node {}: parent = {}, depth = {}, {}, [{}]".format(i, node.parent, depths[i], get_kind_of_tree(node), ', '.join(children)))
        
