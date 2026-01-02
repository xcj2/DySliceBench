class binarytree:
    def __init__(self, num_parts, parts):
        self.num_parts = num_parts
        self.nodes = [None]*self.num_parts
        self.root = 0
        self.pre_order = []
        self.in_order = []
        self.post_order = []
        
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

    def preorder(self,pos):
        if len(self.pre_order) == self.num_parts:
            return
        if not pos in self.pre_order:
            self.pre_order.append(pos)
        if self.nodes[pos].left != -1 and not self.nodes[pos].left in self.pre_order:
            self.preorder(self.nodes[pos].left)
        elif self.nodes[pos].right != -1 and not self.nodes[pos].right in self.pre_order:
            self.preorder(self.nodes[pos].right)
        else:
            self.preorder(self.nodes[pos].parent)

    def inorder(self,pos):
        if len(self.in_order) == self.num_parts:
            return
        if self.nodes[pos].left != -1 and not self.nodes[pos].left in self.in_order:
            self.inorder(self.nodes[pos].left)
        elif not pos in self.in_order:
            self.in_order.append(pos)
            self.inorder(pos)
        elif self.nodes[pos].right != -1 and not self.nodes[pos].right in self.in_order:
            self.inorder(self.nodes[pos].right)
        else:
            self.inorder(self.nodes[pos].parent)

    def postorder(self,pos):
        if len(self.post_order) == self.num_parts:
            return
        if self.nodes[pos].left != -1 and not self.nodes[pos].left in self.post_order:
            self.postorder(self.nodes[pos].left)
        elif self.nodes[pos].right != -1 and not self.nodes[pos].right in self.post_order:
            self.postorder(self.nodes[pos].right)
        elif not pos in self.post_order:
            self.post_order.append(pos)
            self.postorder(pos)
        else:
            self.postorder(self.nodes[pos].parent)
            
    
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

new_tree.preorder(new_tree.root)
new_tree.inorder(new_tree.root)
new_tree.postorder(new_tree.root)

str_pre = list(map(str,new_tree.pre_order))
str_in = list(map(str,new_tree.in_order))
str_post = list(map(str,new_tree.post_order))

print("Preorder")
print(" " + " ".join(str_pre))
print("Inorder")
print(" " + " ".join(str_in))
print("Postorder")
print(" " + " ".join(str_post))
