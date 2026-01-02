from enum import IntEnum


class Attrs(IntEnum):
    LEFT = 0
    RIGHT = 1
    PARENT = 2
    SIBLING = 3
    DEPTH = 4
    HEIGHT = 5


def parents(nodes):
    for i, node in enumerate(nodes):
        if node[Attrs.LEFT] != -1:
            nodes[node[Attrs.LEFT]][Attrs.PARENT] = i
            nodes[node[Attrs.LEFT]][Attrs.SIBLING] = node[Attrs.RIGHT]
        if node[Attrs.RIGHT] != -1:
            nodes[node[Attrs.RIGHT]][Attrs.PARENT] = i
            nodes[node[Attrs.RIGHT]][Attrs.SIBLING] = node[Attrs.LEFT]


def depth_and_heights(nodes):
    def depth(n):
        if nodetype(n) != "root" and n[Attrs.DEPTH] == 0:
            n[Attrs.DEPTH] = depth(nodes[n[Attrs.PARENT]]) + 1
        return n[Attrs.DEPTH]

    def height(n):
        if nodetype(n) != "leaf" and n[Attrs.HEIGHT] == 0:
            if n[Attrs.LEFT] != -1:
                lh = height(nodes[n[Attrs.LEFT]])
            else:
                lh = -1

            if n[Attrs.RIGHT] != -1:
                rh = height(nodes[n[Attrs.RIGHT]])
            else:
                rh = -1
            n[Attrs.HEIGHT] = max(lh, rh) + 1
        return n[Attrs.HEIGHT]

    for node in nodes:
        node[Attrs.DEPTH] = depth(node)
        node[Attrs.HEIGHT] = height(node)


def degree(node):
    if node[Attrs.LEFT] != -1 and node[Attrs.RIGHT] != -1:
        return 2
    elif node[Attrs.LEFT] != -1:
        return 1
    elif node[Attrs.RIGHT] != -1:
        return 1
    else:
        return 0


def nodetype(node):
    if node[Attrs.PARENT] == -1:
        return "root"
    elif node[Attrs.LEFT] == -1 and node[Attrs.RIGHT] == -1:
        return "leaf"
    else:
        return "internal node"


def print_tree(ns):
    parents(ns)
    depth_and_heights(ns)

    for nid, n in enumerate(ns):
        print(("node {}: parent = {}, sibling = {}, degree = {}, " +
               "depth = {}, height = {}, {}").format(nid,
                                                     n[Attrs.PARENT],
                                                     n[Attrs.SIBLING],
                                                     degree(n),
                                                     n[Attrs.DEPTH],
                                                     n[Attrs.HEIGHT],
                                                     nodetype(n)))


def run():
    n = int(input())
    nodes = [None] * n

    for i in range(n):
        nodeid, *attrs = [int(i) for i in input().split()]
        attrs.extend([-1, -1, 0, 0])
        nodes[nodeid] = attrs

    print_tree(nodes)


if __name__ == '__main__':
    run()

