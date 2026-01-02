
class TreeNode:
    def __init__(self, nodeid):
        self.nodeid = nodeid
        self.parent = None
        self.sibling = None
        self.child = None
        self.depth = 0

    def node_type(self):
        if self.parent is None:
            return 'root'
        elif self.child is None:
            return 'leaf'
        else:
            return 'internal node'

    def parent_nodeid(self):
        if self.parent is None:
            return -1
        else:
            return self.parent.nodeid

    def child_nodeids(self):
        if self.child is not None:
            yield self.child.nodeid
            yield from self.child.sibling_nodeids()

    def sibling_nodeids(self):
        s = self.sibling
        stack = []
        while s is not None:
            stack.append(s.nodeid)
            s = s.sibling
        while len(stack) > 0:
            yield stack.pop()

    def get_depth(self):
        if self.node_type() != 'root' and self.depth == 0:
            self.depth = self.parent.get_depth() + 1

        return self.depth

    def add_child(self, node):
        if self.child is None:
            self.child = node
            self.child.parent = self
        else:
            self.child.add_sibling(node)

    def add_sibling(self, node):
        node.parent = self.parent
        node.sibling = self.sibling
        self.sibling = node

    def __str__(self):
        return ('node {}: parent = {}, depth = {}, {}, [{}]'.format(
                self.nodeid, self.parent_nodeid(), self.get_depth(),
                self.node_type(),
                ", ".join([str(i) for i in self.child_nodeids()])))


class Tree:
    def __init__(self):
        self.nodes = {}

    def node(self, nodeid):
        if nodeid not in self.nodes:
            self.nodes[nodeid] = TreeNode(nodeid)

        return self.nodes[nodeid]

    def sorted_nodes(self):
        for nodeid in sorted(self.nodes.keys()):
            yield self.nodes[nodeid]


def run():
    c = int(input())
    tree = Tree()

    for _ in range(c):
        nodeid, deg, *cs = [int(i) for i in input().split()]
        node = tree.node(nodeid)
        for c in cs:
            node.add_child(tree.node(c))

    for node in tree.sorted_nodes():
        print(node)


if __name__ == '__main__':
    run()

