# -*- coding:utf-8 -*-
import sys
from collections import OrderedDict


def cleate_node_dict(children):
    node_dict = OrderedDict()
    for val in children:
        node_dict[val] = None
    return node_dict


def cleate_tree(nodes):
    tree = nodes.copy()
    for node, children in nodes.items():
        for key in children.keys():
            children[key] = nodes[key]
            del tree[key]

    return tree


def rec(current, acc, parent=-1, depth=0):
    if current == {}:
        return
    for node, children in current.items():
        cld_lst = list(children.keys())
        acc[node] = "node {0}: parent = {1}, depth = {2}, {3}, {4}".format(
                node, parent, depth, node_type(parent, children), cld_lst)
        rec(children, acc, node, depth+1)


def node_type(parent, children):
    if parent == -1:
        return "root"
    elif children != {}:
        return "internal node"
    else:
        return "leaf"


def rooted_trees(lst, n):
    nodes = {val[0]: cleate_node_dict(val[2:]) for val in lst}
    tree = cleate_tree(nodes)
    node_info = [None] * n
    rec(tree, node_info)
    print("\n".join(node_info))


if __name__ == "__main__":
    n = int(input())
    lst = [[int(n) for n in val.split()] for val in sys.stdin.readlines()]
    rooted_trees(lst, n)