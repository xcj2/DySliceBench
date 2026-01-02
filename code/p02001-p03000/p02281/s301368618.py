class Trees():
    def __init__(self):
        self.nodes = {}
    def add_nodes(self, id):
        if id not in self.nodes:
            self.nodes[id] = Node(id)
    def add_child(self, id, child_id1, child_id2):
        for child_id in [child_id1, child_id2]:
            if child_id != -1:
                self.add_nodes(child_id)
                self.nodes[id].add_child_id(self.nodes[child_id])
        if child_id1 != -1:
            self.nodes[child_id1].sibling = child_id2
        if child_id2 != -1:            
            self.nodes[child_id2].sibling = child_id1
        self.nodes[id].left = child_id1
        self.nodes[id].right = child_id2
    def setheight(self, id):
        h1, h2 = 0, 0
        if self.nodes[id].right != -1:
            h1 = self.setheight(self.nodes[id].right) + 1
        if self.nodes[id].left != -1:
            h2 = self.setheight(self.nodes[id].left) + 1
        self.nodes[id].height = max(h1, h2)
        return max(h1, h2)
    def preorder(self,u):
        if u == -1:
            return
        print(f' {u}', end='')
        self.preorder(self.nodes[u].left)
        self.preorder(self.nodes[u].right)

    def inorder(self,u):
        if u == -1:
            return
        self.inorder(self.nodes[u].left)
        print(f' {u}', end='')
        self.inorder(self.nodes[u].right)
    def postorder(self,u):
        if u == -1:
            return
        self.postorder(self.nodes[u].left)
        self.postorder(self.nodes[u].right)
        print(f' {u}', end='')
    
        

         
class Node():
    def __init__(self, id):
        self.node = id
        self.parent = None
        self.depth = 0
        self.nodetype = 'root'
        self.children = []
        self.sibling = -1
        self.degree = 0
        self.height = 0
        self.left = -1
        self.right = -1
     
    def add_child_id(self, child):
        child.parent = self
        self.children.append(child)
        child.update_depth()
        self.update_nodetype()
        child.update_nodetype()
        self.degree += 1
        
     
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
        return 'node {}: parent = {}, sibling = {}, degree = {}, depth = {}, height = {}, {}'.format(
            self.node, parent, self.sibling, self.degree, self.depth, self.height, self.nodetype)
     
 
tree = Trees()
 
n = int(input())
top = [0 for _ in range(n)]
for i in range(n):
    a = list(map(int,input().split()))
    tree.add_nodes(a[0])
    tree.add_child(id=a[0], child_id1=a[1], child_id2=a[2])
    if a[1] != -1:
        top[a[1]] += 1
    if a[2] != -1:
        top[a[2]] += 1

for id in range(n):
    tree.setheight(id)
    
for i in range(n):
    if top[i] == 0:
        b = i
        break
        

print('Preorder')
tree.preorder(b)
print()
print('Inorder')
tree.inorder(b)
print()
print('Postorder')
tree.postorder(b)
print()
