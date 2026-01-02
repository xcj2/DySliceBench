# coding=utf-8

class Node:
    def __init__(self, ID, left, right):
        ### output information ###
        self.id = ID
        self.parent = -1 #initialize
        self.sibling = -1 #initialize
        self.degree = -1 #initialize
        self.depth = -1 #initialize
        self.height = -1 #initialize
        self.type = None #initialize

        ### other information ###
        self.left = left
        self.right = right

def calc_depth(i):
    global node_list

    if node_list[i].depth != -1:
        return node_list[i].depth

    depth = 0
    if node_list[i].parent != -1:
        depth = calc_depth(node_list[i].parent) + 1

    node_list[i].depth = depth
    return depth


def calc_height(i):
    global node_list

    if node_list[i].height != -1:
        return node_list[i].height

    h1 = h2 = 0
    if node_list[i].right != -1:
        h1 = calc_height(node_list[i].right) + 1
    if node_list[i].left != -1:
        h2 = calc_height(node_list[i].left) + 1

    height = max(h1, h2)
    node_list[i].height = height
    return height

def pre_order(node):
    global node_list
    global pre_ordered_node_list

    if node == -1:
        return None
    pre_ordered_node_list.append(node)
    pre_order(node_list[node].left)
    pre_order(node_list[node].right)

def in_order(node):
    global node_list
    global in_ordered_node_list

    if node == -1:
        return None
    in_order(node_list[node].left)
    in_ordered_node_list.append(node)
    in_order(node_list[node].right)

def post_order(node):
    global node_list
    global post_ordered_node_list

    if node == -1:
        return None
    post_order(node_list[node].left)
    post_order(node_list[node].right)
    post_ordered_node_list.append(node)

n = int(input())
data = [tuple(map(int, input().split())) for x in range(n)]
node_list = []
root_node = None
pre_ordered_node_list = []
in_ordered_node_list = []
post_ordered_node_list = []

for data_row in data:
    ID, left, right = data_row
    node = Node(ID, left, right)
    node_list.append(node)

node_list.sort(key = lambda node: node.id)

for i, node in enumerate(node_list):
    left = node.left
    right = node.right
    degree = 0

    ### child information ###
    if left != -1:
        degree += 1
        node_list[left].parent = i
        node_list[left].sibling = right

    if right != -1:
        degree += 1
        node_list[right].parent = i
        node_list[right].sibling = left

    ### self information ###
    node.degree = degree

for i in range(n):
    calc_depth(i)
    calc_height(i)

    node = node_list[i]

    if node.depth == 0:
        node.type = 'root'
        root_node = node.id
    elif node.height == 0:
        node.type = 'leaf'
    else:
        node.type = 'internal node'

    #print("node {}: parent = {}, sibling = {}, degree = {}, depth = {}, height = {}, {}".format(node.id, node.parent, node.sibling, node.degree, node.depth, node.height, node.type))

### Tree Walk ###
pre_order(root_node)
in_order(root_node)
post_order(root_node)

print("Preorder")
print("", *pre_ordered_node_list)
print("Inorder")
print("", *in_ordered_node_list)
print("Postorder")
print("", *post_ordered_node_list)