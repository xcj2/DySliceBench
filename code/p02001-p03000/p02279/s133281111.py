class Node:
    def __init__(self, num, parent, *children):
        self.id = num
        self.parent = parent
        self.children = list(children)
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


def set_node(i_p):
    i_p = list(map(int, i_p.split()))
    num = i_p[0]
    children = i_p[2:]
    if children:
        T[num].children = children
        for n in children:
            T[n].parent = num

def find_root(node):
    while node.parent != -1:
        node = T[node.parent]
    return node

def set_depth(node, depth):
    node.depth = depth
    for n in node.children:
        set_depth(T[n], depth + 1)



import sys

n = int(sys.stdin.readline())

T = [Node(i, -1) for i in range(n)]

for x in sys.stdin.readlines():
    set_node(x)

r_n = find_root(T[0])

set_depth(r_n, 0)

for n in T:
    n.show_info()