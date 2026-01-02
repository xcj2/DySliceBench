class Trees():
    def __init__(self):
        self.nodes = {}
    def add_nodes(self, id):
        if id not in self.nodes:
            self.nodes[id] = Node(id)
    def add_child(self, id, child_id):
        self.add_nodes(child_id)
        self.nodes[id].add_child_id(self.nodes[child_id])
        
class Node():
    def __init__(self, id):
        self.node = id
        self.parent = None
        self.depth = 0
        self.nodetype = 'root'
        self.children = []
    
    def add_child_id(self, child):
        child.parent = self
        self.children.append(child)
        child.update_depth()
        self.update_nodetype()
        child.update_nodetype()
    
    def update_depth(self):
        depth = self.depth
        if self.parent:
            self.depth = self.parent.depth + 1
        if depth != self.depth:
            for child in self.children:
                child.update_depth()

    
    def update_nodetype(self):
        if self.depth == 0:
            self.nodetype = 'root'
        elif len(self.children) > 0:
            self.nodetype = 'internal node'
        else:
            self.nodetype = 'leaf'
    
    def __str__(self):
        parent = self.parent.node if self.parent else -1
        children = ', '.join([str(node.node) for node in self.children])
        return 'node {}: parent = {}, depth = {}, {}, [{}]'.format(self.node, parent, 
                                                                   self.depth, self.nodetype, children)
    

tree = Trees()

n = int(input())

for i in range(n):
    a = list(map(int,input().split()))
    tree.add_nodes(a[0])
    for child in a[2:]:
        tree.add_child(id=a[0], child_id=child)

for id in range(n):
    print(f"{tree.nodes[id]}")
