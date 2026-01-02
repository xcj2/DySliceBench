class Tree(object):
    def __init__(self):
        self.nodes = {}
        self.root = None

    def add_node(self, id):
        if id not in self.nodes:
            self.nodes[id] = Node(id)

    def add_child(self, parent_id, child_id):
        self.add_node(parent_id)
        self.add_node(child_id)
        self.nodes[parent_id].add_child(self.nodes[child_id])

    def set_depth(self):
        for node in self.nodes.values():
            if node.type == 'root':
                self.root = node
                break
        self.root._set_depth(0)

    def set_height(self):
        # メモ化して再帰する
        self.root._set_height()


class Node(object):
    def __init__(self, id):
        self.id = id
        self.parent = None
        self.children = []
        self.depth = None
        self.height = None
        self.type = 'root'
        self.bro = None

    def add_child(self, child):
        child.bro = len(self.children)
        self.children.append(child)
        child.parent = self
        child.update_nodetype()
        if self.parent:
            self.update_nodetype()

    def update_nodetype(self):
        if self.parent:
            if self.children:
                self.type = 'internal node'
            else:
                self.type = 'leaf'
        else:
            self.type = 'root'

    def _set_depth(self, depth):
        self.depth = depth
        for child in self.children:
            child._set_depth(depth+1)

    def _set_height(self):
        # メモ化再帰
        if not self.children:
            self.height = 0
        else:
            if self.height:
                pass
            else:
                height = 0
                for child in self.children:
                    child._set_height()
                    height = max(child.height, height)
                self.height = height + 1

    def get_sib(self):
        if not self.parent:
            return -1
        else:
            bros = self.parent.children
            if len(bros) == 1:
                return -1
            else:
                if self.bro == 0:
                    return bros[1].id
                else:
                    return bros[0].id

    def __str__(self):
        parent = self.parent.id if self.parent else -1
        sib = self.get_sib()
        deg = len(self.children)
        dep = self.depth
        h = self.height
        str = 'node {}: parent = {}, sibling = {}, degree = {}, depth = {}, height = {}, {}'.format(id, parent, sib, deg, dep, h, self.type)
        return str


tree = Tree()
n = int(input())
for i in range(n):
    tmp = list(map(int, input().split()))
    id = tmp[0]
    children = tmp[1:]
    tree.add_node(id)
    for c in children:
        if c != -1:
            tree.add_child(id, c)
tree.set_depth()
tree.set_height()
for id in range(n):
    print(tree.nodes[id])

