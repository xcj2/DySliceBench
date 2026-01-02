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
        rn_check_list.remove(n)

def set_pd(node, parent, depth):
    node.parent = parent
    node.depth = depth
    for n in node.children:
        set_pd(T[n], node.id, depth + 1)


import sys

n = int(sys.stdin.readline())

T = [None for i in range(n)]

rn_check_list = [i for i in range(n)]

for x in sys.stdin.readlines():
    set_node(x)

rn_i = rn_check_list[0]

set_pd(T[rn_i], -1, 0)

for n in T:
    n.show_info()