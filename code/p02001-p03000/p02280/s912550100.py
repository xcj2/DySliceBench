# coding=utf-8

class Node:
    def __init__(self, ID, left, right):
        ### ?????¬?????± ###
        self.id = ID
        self.parent = -1 #??????
        self.sibling = -1 #??????
        self.degree = -1 #??????
        self.depth = 0 #??????
        self.height = 0 #??????
        self.type = None #??????

        ### ?£??¶??????± ###
        self.left_child = left
        self.right_child = right

def calc_depth(i):
    global node_list

    if node_list[i].depth != 0:
        return node_list[i].depth

    depth = 0
    if node_list[i].parent != -1:
        depth = calc_depth(node_list[i].parent) + 1

    node_list[i].depth = depth
    return depth


def calc_height(i):
    global node_list

    if node_list[i].height != 0:
        return node_list[i].height

    h1 = h2 = 0
    if node_list[i].right_child != -1:
        h1 = calc_height(node_list[i].right_child) + 1
    if node_list[i].left_child != -1:
        h2 = calc_height(node_list[i].left_child) + 1

    height = max(h1, h2)
    node_list[i].height = height
    return height

n = int(input())
data = [tuple(map(int, input().split())) for x in range(n)]
node_list = []

for data_row in data:
    ID, left, right = data_row
    node = Node(ID, left, right)
    node_list.append(node)

node_list.sort(key = lambda node: node.id)

for i, node in enumerate(node_list):
    left = node.left_child
    right = node.right_child
    degree = 0

    ### ???????????± ###
    if left != -1:
        degree += 1
        node_list[left].parent = i
        node_list[left].sibling = right

    if right != -1:
        degree += 1
        node_list[right].parent = i
        node_list[right].sibling = left

    ### ??????????????± ###
    node.degree = degree

for i in range(n):
    calc_depth(i)
    calc_height(i)

    node = node_list[i]

    if node.depth == 0:
        node.type = 'root'
    elif node.height == 0:
        node.type = 'leaf'
    else:
        node.type = 'internal node'

    print("node {}: parent = {}, sibling = {}, degree = {}, depth = {}, height = {}, {}".format(node.id, node.parent, node.sibling, node.degree, node.depth, node.height, node.type))