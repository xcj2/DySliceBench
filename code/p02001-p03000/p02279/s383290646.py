

class Node:
    def __init__(self, num, children):
        self.num = num
        self.children = children
        self.parents = -1
        self.type = None
        self.depth = 0

    def output(self):
        print('node {0}: parent = {1}, depth = {2}, {3}, {4}'.format(self.num,
                                                                      self.parents,
                                                                      self.depth,
                                                                      self.type,
                                                                      self.children))


def set_node(num, children):
    node = Node(num, children)
    T[num] = node
    for n in children:
        T[-1] -= n  # ?????£???T[-1]???root???????????????????????????


def set_pdt(n_i, parent, depth):
    node = T[n_i]
    node.parents = parent
    node.depth = depth
    if node.children:
        node.type = 'internal node'
        for n in node.children:
            set_pdt(n, n_i, depth + 1)
    else:
        node.type = 'leaf'


n = int(input())
tree = [list(map(int, input().split())) for i in range(n)]
T = [None] * n
T += [n * (n - 1) // 2]
for j in tree:
    set_node(j[0], j[2:])

set_pdt(T[-1], -1, 0)

T[T[-1]].type = 'root'

for n in T[:-1]:
    n.output()