class Node:
    def __init__(self, num, parent, children):
        self.id = num
        self.parent = -1
        self.depth = 0
        self.type = None
        self.children = children
        
    def show_info(self):
        print('node {0}: parent = {1}, depth = {2}, {3}, {4}'.format(self.id,
                                                                     self.parent,
                                                                     self.depth,
                                                                     self.type,
                                                                     self.children))


def set_node(i_s):
    i_l = list(map(int, i_s.split()))
    num = i_l[0]
    children = i_l[2:]
    node = Node(num, -1, children)
    T[num] = node
    for n in children:
        T[-1] -= n

def set_pdt(n_i, parent, depth):
    node = T[n_i]
    node.parent = parent
    node.depth = depth
    if node.children:
        node.type = 'internal node'
        for n in node.children:
            set_pdt(n, n_i, depth + 1)
    else:
        node.type = 'leaf'


import sys

n = int(sys.stdin.readline())

T = [None] * n

T.append(int(n * (n - 1) / 2))

for x in sys.stdin.readlines():
    set_node(x)

set_pdt(T[-1], -1, 0)

T[T[-1]].type ='root'

for n in T[:-1]:
    n.show_info()