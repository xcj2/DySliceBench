# copy
class Tree():
    def __init__(self):
        self.nodes = {}

    def add_node(self, id):
        if id not in self.nodes:
            self.nodes[id] = Node(id)

    def add_child(self, parent_id, child_id):
        self.add_node(parent_id)
        self.add_node(child_id)
        self.nodes[parent_id].add_child(self.nodes[child_id])


class Node():
    def __init__(self, id):
        self.id = id
        self.parent = None
        self.children = []
        self.depth = 0
        self.nodetype = 'root'

    def add_child(self, child):
        self.children.append(child)
        child.parent = self
        child.update_depth()
        child.update_nodetype()
        self.update_nodetype()
        if self.parent:
            self.parent.update_nodetype()

    def update_depth(self):
        depth = self.depth
        if self.parent:
            self.depth = self.parent.depth + 1
        if depth != self.depth:
            for child in self.children:
                child.update_depth()

    def update_nodetype(self):
        if self.parent:
            if len(self.children):
                self.nodetype = 'internal node'
            else:
                self.nodetype = 'leaf'
        else:
            self.nodetype = 'root'

    def walk(self):
        yield self
        for child in self.children:
            for node in child.walk():
                yield node

    def __str__(self):
        parent = self.parent.id if self.parent else -1
        children = ', '.join([str(node.id) for node in self.children])
        return 'node {}: parent = {}, depth = {}, {}, [{}]'.format(self.id,
                                                                   parent,
                                                                   self.depth,
                                                                   self.nodetype,
                                                                   children)


tree = Tree()

n = int(input())
for i in range(n):
    line = input().split()
    id = int(line[0])
    tree.add_node(id)
    for ci in map(int, line[2:]):
        tree.add_child(id, ci)

for id in sorted(tree.nodes):
    print(tree.nodes[id])
