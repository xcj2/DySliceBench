class binarytree:
    def __init__(self, num_parts, parts):
        self.num_parts = num_parts
        self.nodes = [None]*self.num_parts
        self.root = 0
        for i in range(self.num_parts):
            self.nodes[parts[i][0]] = binarynode(parts[i][0],parts[i][1],parts[i][2])

    def set_families(self):
        for i in range(self.num_parts):
            if self.nodes[i].left != -1:
                self.nodes[self.nodes[i].left].set_parent(i)
                self.nodes[self.nodes[i].left].set_sibling(self.nodes[i].right)
            if self.nodes[i].right != -1:
                self.nodes[self.nodes[i].right].set_parent(i)
                self.nodes[self.nodes[i].right].set_sibling(self.nodes[i].left)
        for i in range(self.num_parts):
            if self.nodes[i].parent == -1:
                self.root = i
            
    def set_type(self):
        for i in range(self.num_parts):
            self.nodes[i].check_type()

    def set_depth(self, pos, depth):
        self.nodes[pos].set_depth(depth)
        if self.nodes[pos].left != -1:
            self.set_depth(self.nodes[pos].left, depth+1)
        if self.nodes[pos].right != -1:
            self.set_depth(self.nodes[pos].right, depth+1)

    def set_height(self, pos, height):
        self.nodes[pos].set_height(height)
        if self.nodes[pos].parent != -1:
            self.set_height(self.nodes[pos].parent, height+1)
        return
            
class binarynode:
    def __init__(self, id, left, right):
        self.id = id
        self.parent = -1
        self.left = left
        self.right = right
        self.sibling = -1
        self.degree = 2
        self.depth = 0
        self.height = 0
        self.type = "internal node"

        if self.left == -1:
            self.degree -= 1
        if self.right == -1:
            self.degree -= 1
        
    def set_parent(self,parent):
        self.parent = parent
        return
    def set_sibling(self,sibling):
        self.sibling = sibling
        return
        
    def check_type(self):
        if self.parent == -1:
            self.type = "root"
        elif self.left == -1 and self.right == -1:
            self.type = "leaf"
        else:
            self.type = "internal node"
        return
            
    def set_depth(self,depth):
        self.depth = depth
        return
    def set_height(self,height):
        self.height = max(self.height, height)
        return
        
n = int(input())
obj = []
for i in range(n):
    obj.append(list(map(int, input().split())))

new_tree = binarytree(n, obj)
new_tree.set_families()
new_tree.set_type()
new_tree.set_depth(new_tree.root, 0)
for i in range(n):
    if new_tree.nodes[i].type == "leaf":
        new_tree.set_height(i, 0)

for i in range(n):
    print("node {}: parent = {}, sibling = {}, degree = {}, depth = {}, height = {}, {}".format(i, new_tree.nodes[i].parent, new_tree.nodes[i].sibling, new_tree.nodes[i].degree, new_tree.nodes[i].depth, new_tree.nodes[i].height, new_tree.nodes[i].type))
