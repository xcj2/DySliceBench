class Node:
    def __init__(self, num, parent, leftmostChild, rightSibling):
        self.id = num
        self.parent = parent
        self.leftmostChild = leftmostChild
        self.rightSibling = rightSibling
        self.depth = 0
        
    def show_info(self):
        print('node {0}: '.format(self.id), end = '')
        print('parent = {0}, '.format(self.parent.id), end = '')
        print('depth = {0}, '.format(self.depth), end = '')
        if self.leftmostChild and self.parent.id != -1:
            print('internal node, ', end = '')
        elif self.parent.id != -1:
            print('leaf, ', end = '')
        else:
            print('root, ', end = '')
        print('[', end = '')
        t_n = self.leftmostChild
        if t_n:
            print(t_n.id, end = '')
            t_n = t_n.rightSibling
        while t_n:
            print(', {0}'.format(t_n.id), end = '')
            t_n = t_n.rightSibling
        print(']')


class RootedTree():
    def __init__(self, n):
        self.base_node = Node(-1, None, None, None)
        self.nodes = [Node(i, self.base_node, None, None) for i in range(n)]
    
    def set_node(self, num, k, *children):
        if children:
            self.nodes[num].leftmostChild = self.nodes[children[0]]
            for i, x in enumerate(children[:-1]):
                self.nodes[x].parent = self.nodes[num]
                self.nodes[x].rightSibling = self.nodes[children[i + 1]]
            self.nodes[children[-1]].parent = self.nodes[num]

    def set_depth(self):
        for n in self.nodes:
            t_n = n
            while t_n.parent.id != -1:
                n.depth += 1
                t_n = t_n.parent

    def show_nodes_info(self):
        for n in self.nodes:
            n.show_info()



import sys

n = int(sys.stdin.readline())

T = RootedTree(n)

for x in sys.stdin.readlines():
    T.set_node(*list(map(int, x.split())))

T.set_depth()

T.show_nodes_info()