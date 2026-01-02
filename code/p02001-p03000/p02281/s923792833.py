class Node:
    def __init__(self, id):
        self.id = id
        self.left = -1
        self.right = -1
def walk_preorder(node, order_list):
    if node == None:
        return 0
    order_list.append(node.id)
    walk_preorder(nodes.get(node.left), order_list)
    walk_preorder(nodes.get(node.right), order_list)
def walk_inorder(node, order_list):
    if node == None:
        return 0
    walk_inorder(nodes.get(node.left), order_list)
    order_list.append(node.id)
    walk_inorder(nodes.get(node.right), order_list)
def walk_postorder(node, order_list):
    if node == None:
        return 0
    walk_postorder(nodes.get(node.left), order_list)
    walk_postorder(nodes.get(node.right), order_list)
    order_list.append(node.id)

n = int(input())
nodes = {}
for _ in range(n):
    id, left, right = [int(x) for x in input().split(' ')]
    node = Node(id)
    node.left = left
    node.right = right
    nodes[id] = node
is_child_table = {node_id:False for node_id in range(n)}
for id in nodes:
    if nodes[id].left > -1:
        is_child_table[nodes[id].left] = True
    if nodes[id].right > -1:
        is_child_table[nodes[id].right] = True
root_id = [node_id for node_id in is_child_table.keys() if is_child_table[node_id] == False][0]
root_node = nodes[root_id]

preorder_list = []
inorder_list = []
postorder_list = []
walk_preorder(root_node, preorder_list)
walk_inorder(root_node, inorder_list)
walk_postorder(root_node, postorder_list)
print('Preorder')
preorder_str = ' '.join(map(str, preorder_list))
print(' {}'.format(preorder_str))
print('Inorder')
inorder_str = ' '.join(map(str, inorder_list))
print(' {}'.format(inorder_str))
print('Postorder')
postorder_str = ' '.join(map(str, postorder_list))
print(' {}'.format(postorder_str))
