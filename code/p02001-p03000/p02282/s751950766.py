class Tree():
    def __init__(self):
        self.nodes = {}
        self.nodes[-1] = None
    def add_node(self, id):
        if id not in self.nodes:
            self.nodes[id] = Node(id)        
    def add_child(self, parent_id, left_id, right_id):
        self.add_node(parent_id)
        self.add_node(left_id)
        self.add_node(right_id)
        self.nodes[parent_id].add_child(self.nodes[left_id], self.nodes[right_id])
    def root(self):
        for node in self.nodes.values():
            if node and node.nodetype() == 'root':
                return node
    
class Node():
    def __init__(self, id):
        self.id = id
        self.parent = self.left = self.right = None
        self.depth = self.height = 0

    def add_child(self, left, right):
        self.left = left
        self.right = right
        
        self.update_height()
        
        for child in self.children():
            child.parent = self
            child.update_depth()
    def update_height(self):
        if self.degree():
            self.height = max([child.height + 1 for child in self.children()])
            if self.parent:
                self.parent.update_height()
            
    def update_depth(self):
        self.depth = self.parent.depth + 1
        for child in self.children():
            child.update_depth()
                
    def nodetype(self):
        if self.parent:
            if self.degree():
                return 'internal node'
            else:
                return 'leaf'
        else:
            return 'root'
    def degree(self):
        return len(self.children())
    
    def children(self):
        return [child for child in [self.left, self.right] if child]
    
    def sibling(self):
        if self.parent and self.parent.degree() == 2:
            if self.parent.left == self:
                return self.parent.right.id
            else:
                return self.parent.left.id
        else:
            return -1

    def __str__(self):
        return 'node {}: parent = {}, sibling = {}, degree = {}, depth = {}, height = {}, {}'.format(
            self.id,
            self.parent.id if self.parent else - 1,
            self.sibling(),
            self.degree(),
            self.depth,
            self.height,
            self.nodetype())
    def walk(self, order):
        orders = {'Preorder':[self, self.left, self.right], 'Inorder':[self.left, self, self.right], 'Postorder':[self.left, self.right, self]}
        
        for node in orders[order]:
            if node == self:
                yield node
            elif node:
                for childnode in node.walk(order):
                    yield childnode

def make_tree(tree, preorder, inorder):
    if len(preorder) == 0:
        return -1
    root_id = preorder[0]    
    root_index = inorder.index(root_id)
    left_id = make_tree(tree, preorder[1:root_index + 1], inorder[:root_index])
    right_id = make_tree(tree, preorder[root_index + 1:], inorder[root_index + 1:])
    tree.add_child(root_id, left_id, right_id)
    return root_id
    
n = int(input())
preorder = list(map(int, input().split()))
inorder = list(map(int, input().split()))

tree = Tree()
root_id = make_tree(tree, preorder, inorder)

print(*[node.id for node in tree.nodes[root_id].walk('Postorder')])