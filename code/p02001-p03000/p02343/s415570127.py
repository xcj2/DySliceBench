# -*- coding: utf-8 -*-

"""Disjoint Set"""

import sys
import os
import pprint


class Node:
    def __init__(self, key):
        self.parent = self
        self.key = key
        self.rank = 0  # ???????????????????????¨????????¨????????¨?????????

    def get_root(self):
        """
        :rtype: Node
        :return:
        """
        n = self
        while n.parent is not n:
            n = n.parent
        return n


# ????????????????????????
def unite(x, y):
    node_x = nodes[x]
    node_y = nodes[y]

    root_x = node_x.get_root()
    root_y = node_y.get_root()

    if root_x.rank > root_y.rank:
        # root x???????????????
        root_y.parent = root_x
    elif node_x.rank == node_y.rank:
        # root x???????????????
        root_y.parent = root_x
        # root x?????????????????´
        root_x.rank += 1
    else:
        # node y?????????????????????
        root_x.parent = root_y

# ??£??¨??????????????????
def find_set(x):
    node = nodes[x]
    return node.get_root().key


#fd = os.open('DSL_1_A.txt', os.O_RDONLY)
#os.dup2(fd, sys.stdin.fileno())

lis = list(map(int, input().split()))
n = lis[0]
q = lis[1]

nodes = []
for i in range(n):
    nodes.append(Node(i))

for _ in range(q):
    com, x, y = list(map(int, input().split()))
    if com == 0:
        # unite
        unite(x, y)
    else:
        # same
        id0 = find_set(x)
        id1 = find_set(y)
        if id0 == id1:
            print(1)
        else:
            print(0)



def node_test():
    node0 = Node(0)
    node1 = Node(1)
    node1.parent = node0
    node2 = Node(2)
    node2.parent = node1
    n = node2.get_root()
    print(n.key)
    print(node2.key)

if __name__ == '__main__':
    #node_test()
    pass