#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
input:
9
0 1 4
1 2 3
2 -1 -1
3 -1 -1
4 5 8
5 6 7
6 -1 -1
7 -1 -1
8 -1 -1

output:
node 0: parent = -1, sibling = -1, degree = 2, depth = 0, height = 3, root
node 1: parent = 0, sibling = 4, degree = 2, depth = 1, height = 1, internal node
node 2: parent = 1, sibling = 3, degree = 0, depth = 2, height = 0, leaf
node 3: parent = 1, sibling = 2, degree = 0, depth = 2, height = 0, leaf
node 4: parent = 0, sibling = 1, degree = 2, depth = 1, height = 2, internal node
node 5: parent = 4, sibling = 8, degree = 2, depth = 2, height = 1, internal node
node 6: parent = 5, sibling = 7, degree = 0, depth = 3, height = 0, leaf
node 7: parent = 5, sibling = 6, degree = 0, depth = 3, height = 0, leaf
node 8: parent = 4, sibling = 5, degree = 0, depth = 2, height = 0, leaf
"""

import sys


class Node(object):
    def __init__(self):
        # init node as a single leaf node.
        self.parent = -1
        self.type = 'leaf'
        self.depth = 0
        self.children = []
        self.degree = 0
        self.sibling = -1
        self.height = 0


def get_depth(v, depth=0):
    if not v.children:
        # set leaf's depth
        v.depth = depth
        return v.depth

    v.depth = depth

    left_child_idx = v.children[0]
    right_child_idx = v.children[1]
    if left_child_idx != -1:
        get_depth(node_list[left_child_idx], depth + 1)

    if right_child_idx != -1:
        get_depth(node_list[right_child_idx], depth + 1)
    return v.depth


def get_height(v):
    h1, h2 = 0, 0
    # leaf's height is always 0, children: []
    if not v.children:
        return 0

    left_child_idx = v.children[0]
    right_child_idx = v.children[1]
    if left_child_idx != -1:
        h1 = get_height(node_list[left_child_idx]) + 1

    if right_child_idx != -1:
        h2 = get_height(node_list[right_child_idx]) + 1

    v.height = max(h1, h2)
    return v.height


def generate_tree(_array):
    # add info of each node of a ordered tree
    for each in _array:
        idx, *children = [int(x) for x in each]
        # assert len(children) == 2
        if children != [-1, -1]:
            node_list[idx].type = 'internal node'
            node_list[idx].children = children
            node_list[idx].degree = 1 if (-1 in children) else 2
        else:
            # node is leaf as default, children: []
            continue

        for child_idx in children:
            # non-existent node: no parent or sibling
            if child_idx == -1:
                continue
            node_list[child_idx].parent = idx
            node_list[child_idx].sibling = sum(children) - child_idx

    root_idx = [i for i, x in enumerate(node_list) if x.parent == -1][0]
    root_node = node_list[root_idx]
    root_node.type = 'root'

    # add node depth and height info -- using DFS
    get_depth(root_node)
    get_height(root_node)

    return node_list


def print_result(_node):
    print('parent = ' + str(_node.parent) + ',', end=' ')
    print('sibling = ' + str(_node.sibling) + ',', end=' ')
    print('degree = ' + str(_node.degree) + ',', end=' ')
    print('depth = ' + str(_node.depth) + ',', end=' ')
    print('height = ' + str(_node.height) + ',', end=' ')
    print(_node.type)
    return None


if __name__ == '__main__':
    _input = sys.stdin.readlines()
    array_length = int(_input[0])
    array = list(map(lambda x: x.split(), _input[1:]))
    # assert len(array) == array_length

    node_list = [Node() for _ in range(array_length)]
    ans = generate_tree(_array=array)
    for key, node in enumerate(ans):
        print('node ' + str(key) + ':', end=' ')
        print_result(_node=node)