import sys
sys.setrecursionlimit(10000)


class Node:

    def __init__(self, _id):
        self.id = _id
        self.children = []
        self.parent = None
        self.__depth = 0
    
    def add(self, node):
        node.parent = self
        self.children.append(node)

    def parent_id(self):
        if self.parent is None:
            return -1
        else:
            return self.parent.id

    def node_type(self):
        if self.parent is None:
            return 'root'
        elif len(self.children) == 0:
            return 'leaf'
        else:
            return 'internal node'

    def children_ids(self):
        return list(map(lambda n: n.id, self.children))

    def depth(self):
        if self.parent is None:
            return 0
        else:
            return self.parent.depth() + 1

    def __repr__(self):
        return 'node {}: parent = {}, depth = {}, {}, {}'.format(
            self.id, self.parent_id(), self.depth(), self.node_type(), self.children_ids())


def main():
    n = int(input())
    nodes = [Node(i) for i in range(n)]
    for _ in range(n):
        ID, _, *c_s = map(int, input().split(' '))
        for c in c_s:
            nodes[ID].add(nodes[c])
    for n in nodes:
        print(n)


if __name__ == '__main__':
    main()

