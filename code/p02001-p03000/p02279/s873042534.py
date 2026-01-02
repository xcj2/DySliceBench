#!/usr/bin/env python
# -*- coding: utf-8 -*-


import sys


class Node(object):
    __slots__ = ('parent', 'depth', 'type', 'children')

    def __init__(self):
        self.parent = -1
        self.type = ''
        self.depth = 0
        self.children = []


def dfs(node_idx, node_list, depth=0):
    node_list[node_idx].depth = depth
    for child in node_list[node_idx].children:
        dfs(child, node_list, depth=depth + 1)
    return None


def print_result(_node):
    print('parent = ' + str(_node.parent) + ',', end=' ')
    print('depth = ' + str(_node.depth) + ',', end=' ')
    print(_node.type + ',', end=' ')
    print(_node.children)
    return None


def generate_tree(_array, node_list):
    for each in _array:
        idx, k, *children = [int(x) for x in each]
        node_list[idx].children = children
        if k:
            node_list[idx].type = 'internal node'
        else:
            node_list[idx].type = 'leaf'
        for child_idx in children:
            node_list[child_idx].parent = idx
    root_idx = [i for i, x in enumerate(node_list) if x.parent == -1][0]
    node_list[root_idx].type = 'root'
    dfs(node_idx=root_idx, node_list=node_list)
    return node_list


if __name__ == '__main__':
    _input = sys.stdin.readlines()
    array_length = int(_input[0])
    array = list(map(lambda x: x.split(), _input[1:]))
    # assert len(array) == array_length

    init_node_list = [Node() for _ in range(array_length)]
    ans = generate_tree(_array=array, node_list=init_node_list)
    for key, node in enumerate(ans):
        print('node ' + str(key) + ':', end=' ')
        print_result(_node=node)