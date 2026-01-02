n = int(input())

nodes = []
for _ in range(n):
    x = list(map(int, input().split()))
    nodes.append(x)
    
class Tree:
    def __init__(self, n):
        # n : ノード数
        # sibling : 兄弟
        self.nodes = {node: {'parent': None, 'children': [], 'depth': None, 'height': None, 'sibling': None} for node in range(n)}
        self.root = None
        
    def get_root(self):
        if self.root != None:
            return self.root
        else:
            for k, v in self.nodes.items():
                if v['parent'] == None:
                    self.root = k
                    return self.root
        
    def add_node_with_child(self, node, childlen):
        for c in childlen:
            self.nodes[node]['children'].append(c)
            if c == -1:
                continue
            self.nodes[c]['parent'] = node
    
    def get_parent(self, node):
        return self.nodes[node]['parent']
    
    def get_children(self, node):
        return self.nodes[node]['children']
        
    def get_depth(self, node):
        if self.nodes[node]['depth'] != None:
            return self.nodes[node]['depth']
        elif self.nodes[node]['parent'] == None:
            self.nodes[node]['depth'] = 0
            return 0
        else:
            depth = self.get_depth(self.nodes[node]['parent']) + 1
            self.nodes[node]['depth'] = depth
            return depth
        
    def get_height(self, node):
        if self.nodes[node]['height'] != None:
            return self.nodes[node]['height']
        elif len(self.nodes[node]['children']) == 0:
            self.nodes[node]['height'] = 0
            return 0
        elif self.nodes[node]['height'] == None:
            children = self.nodes[node]['children']
            children_h = [self.get_height(c)+1 for c in children]
            self.nodes[node]['height'] = max(children_h)
            return self.nodes[node]['height']
        
    def get_sibling(self, node):
        if self.nodes[node]['sibling'] != None:
            return self.nodes[node]['sibling']
        elif self.nodes[node]['parent'] == None:
            self.nodes[node]['sibling'] = []
            return self.nodes[node]['sibling']
        else:
            p = self.nodes[node]['parent']
            sibling = set(self.get_children(p))
            sibling.remove(node)
            self.nodes[node]['sibling'] = list(sibling)
            return self.nodes[node]['sibling']
        
RootedTree = Tree(n)
for t in nodes:
    node = t[0]
    childlen = []
    #if t[1] != -1:
    childlen.append(t[1])
    #if t[2] != -1:
    childlen.append(t[2])
    RootedTree.add_node_with_child(node, childlen)
    
root = RootedTree.get_root()

def Preorder(node):
    print('', node, end="")
    for c in RootedTree.get_children(node):
        if c == -1:
            continue
        Preorder(c)

print('Preorder')
Preorder(root)


def Inorder(node):
    c = RootedTree.get_children(node)
    if c[0] != -1:
        Inorder(c[0])
    print('', node, end="")
    
    if c[1] != -1:
        Inorder(c[1])
    
print()    
print('Inorder')
Inorder(root)


def Postorder(node):
    for c in RootedTree.get_children(node):
        if c == -1:
            continue
        Postorder(c)
    print('', node, end="")
print()    
print('Postorder')
Postorder(root)
print()    
