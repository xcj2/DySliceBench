class Node:
    def __init__(self, num, parent, children):
        self.id = num
        self.parent = -1
        self.children = children
        self.depth = 0
        
    def show_info(self):
        print('node {0}: '.format(self.id), end = '')
        print('parent = {0}, '.format(self.parent), end = '')
        print('depth = {0}, '.format(self.depth), end = '')
        if self.children and self.parent != -1:
            print('internal node, ', end = '')
        elif self.parent != -1:
            print('leaf, ', end = '')
        else:
            print('root, ', end = '')
        print(self.children)


def set_node(i_s):
    i_l = list(map(int, i_s.split()))
    num = i_l[0]
    children = i_l[2:]
    node = Node(num, -1, children)
    T[num] = node
    for n in children:
        T[-1] -= n

def set_pd(n_i, parent, depth):
    node = T[n_i]
    node.parent = parent
    node.depth = depth
    for n in node.children:
        set_pd(n, n_i, depth + 1)


import sys

n = int(sys.stdin.readline())

T = [None] * n

T.append(int(n * (n - 1) / 2))

for x in sys.stdin.readlines():
    set_node(x)

set_pd(T[-1], -1, 0)

for n in T[:-1]:
    n.show_info()