class Node:
    def __init__(self, id):
        self.id = id
        self.left = -1
        self.right = -1
def walk_postorder(node, order_list):
    if node == None:
        return 0
    walk_postorder(nodes.get(node.left), order_list)
    walk_postorder(nodes.get(node.right), order_list)
    order_list.append(node.id)
def build_tree(nodes, preorder, inorder, start_idx, end_idx):
    node = Node(preorder[build_tree.pre_idx])
    nodes[preorder[build_tree.pre_idx]] = node
    build_tree.pre_idx += 1
    
    if start_idx == end_idx:
        return node
    
    root_idx = inorder.index(node.id)
    if start_idx != root_idx:
        left = build_tree(nodes, preorder, inorder, start_idx, root_idx-1)
        nodes[node.id].left = left.id
    if end_idx != root_idx:
        right = build_tree(nodes, preorder, inorder, root_idx+1, end_idx)
        nodes[node.id].right = right.id
    
    return node

n = int(input())
preorder = list(map(int, input().split(' ')))
inorder = list(map(int, input().split(' ')))
nodes = {}
build_tree.pre_idx = 0
build_tree(nodes, preorder, inorder, 0, n-1)
postorder_list = []
walk_postorder(nodes[preorder[0]], postorder_list)
print(' '.join(map(str, postorder_list)))
