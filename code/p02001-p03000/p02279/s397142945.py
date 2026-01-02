class tree:
    def __init__(self, parts):
        self.num_parts = len(parts)
        self.nodes = []
        for i in range(self.num_parts):
            self.nodes.append(node(parts[i][0],parts[i][1],parts[i][2]))

    def set_parents(self):
        for i in range(self.num_parts):
            for child_id in self.nodes[i].children_id:
                self.nodes[child_id].set_parent(i)

    def set_type(self):
        for i in range(self.num_parts):
            self.nodes[i].check_type()
    def set_depth(self):
        for i in range(self.num_parts):
            if self.nodes[i].type == "root":
                parents = [self.nodes[i]]
                depth = 0
                self.nodes[i].set_depth(depth)
                for j in range(20):
                    depth += 1
                    children = []
                    for parent in parents:
                        for child_id in parent.children_id:
                            self.nodes[child_id].set_depth(depth)
                            children.append(self.nodes[child_id])
                    parents = children
                        
class node:
    def __init__(self, id, k, children):
        self.id = id
        self.k = k
        self.children_id = children
        self.depth = -1
        self.parent_id = -1
        self.type = "leaf"
        
    def set_parent(self,parent_id):
        self.parent_id = parent_id

    def check_type(self):
        if self.parent_id == -1:
            self.type = "root"
        elif self.children_id == []:
            self.type = "leaf"
        else:
            self.type = "internal node"
            
    def set_depth(self,depth):
        self.depth = depth
        
n = int(input())
obj = [[0,0,[]] for i in range(n)]
for i in range(n):
    inp = list(map(int, input().split()))
    obj[inp[0]][0] = inp[0]
    obj[inp[0]][1] = inp[1]
    if inp[1]>0:
        obj[inp[0]][2] = inp[2:]

new_tree = tree(obj)
new_tree.set_parents()
new_tree.set_type()
new_tree.set_depth()

for i in range(n):
    print("node {}: parent = {}, depth = {}, {}, {}".format(i, new_tree.nodes[i].parent_id, new_tree.nodes[i].depth, new_tree.nodes[i].type, new_tree.nodes[i].children_id))
