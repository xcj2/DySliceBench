# -*- coding:utf-8 -*-
import sys


def bin_tree(lst, n):
    """
        tree[0]: node
        tree[1]: parent
        tree[2]: sibling
        tree[3]: degree
        tree[4]: depth
        tree[5]: height
    """
    info = [[-1, -1, -1, -1, -1, -1] for n in range(0, n)]
    degree = 0
    for node, left, right in lst:
        if left >= 0:
            info[left][1] = node
            info[left][2] = right
            degree += 1

        if right >= 0:
            info[right][1] = node
            info[right][2] = left
            degree += 1

        info[node][0] = node
        info[node][3] = degree

        degree = 0

    root = -1
    for node in info:
        root = node[0]
        if node[1] == -1:
            break

    get_depth(lst, root, info)
    get_height(lst, root, info)
    print_info(info)


def get_height(tree, root, info):
    def _get_height(node, depth):
        if node == -1:
            return 0

        left_height = _get_height(tree[node][1], depth + 1)
        right_height = _get_height(tree[node][2], depth + 1)

        if left_height > right_height:
            info[node][5] = left_height
        else:
            info[node][5] = right_height

        return info[node][5] + 1

    _get_height(root, 0)


def get_depth(tree, root, info):
    def _get_depth(node, depth):
        if node == -1:
            return

        info[node][4] = depth
        _get_depth(tree[node][1], depth + 1)
        _get_depth(tree[node][2], depth + 1)

    _get_depth(root, 0)


def print_info(info):
    for node, parent, sibling, degree, depth, height in info:
        if parent == -1:
            _type = "root"
        elif degree != 0:
            _type = "internal node"
        else:
            _type = "leaf"

        print("node {0}: parent = {1}, sibling = {2}, degree = {3}, depth = {4}, height = {5}, {6}".format(node, parent, sibling, degree, depth, height, _type))


if __name__ == "__main__":
    n = int(input())
    lst = [[int(n) for n in val.split()] for val in sys.stdin.readlines()]
    lst.sort(key=lambda x: x[0])
    bin_tree(lst, n)