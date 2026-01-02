class Tree:
    def __init__(self, n):
        self.n = n
        self.nodes = [Node(i) for i in range(n)]
        self.root = -1

    def set_tree(self):
        for _ in range(self.n):
            i_str = [int(i) for i in input().split()]
            for i in range(2):
                if i_str[i+1] != -1:
                    self.nodes[i_str[0]].degree += 1
                    self.nodes[i_str[i+1]].parent = i_str[0]
                    if self.nodes[i_str[i+1]].type != "internal node":
                        self.nodes[i_str[i+1]].type = "leaf"
            if self.nodes[i_str[0]].degree == 2:
                self.nodes[i_str[1]].sibling = i_str[2]
                self.nodes[i_str[2]].sibling = i_str[1]
            if self.nodes[i_str[0]].degree > 0:
                self.nodes[i_str[0]].type = "internal node"

    def set_depth_height(self):
        self.set_root()
        self.set_depth(self.root)

        for node in self.nodes:
            if node.type == "leaf":
                self.set_height(node.id)

    def set_depth(self, parent, depth = -1):
        self.nodes[parent].depth = depth + 1
        for node in self.nodes:
            if node.parent == parent:
                self.set_depth(node.id, depth + 1)

    def set_height(self, child, height = -1):
        if self.nodes[child].height <= height + 1:
            self.nodes[child].height = height + 1
            if self.nodes[child].parent != -1:
                self.set_height(self.nodes[child].parent, height + 1)

    def set_root(self):
        for tn in self.nodes:
            if tn.parent == -1:
                self.root = tn.id
                tn.type = "root"
                break

    def show_tree_info(self):
        for node in self.nodes:
            node.show_node_info()

class Node:
    def __init__(self, id):
        self.id = id
        self.parent = -1
        self.sibling = -1
        self.degree = 0
        self.depth = 0
        self.height = 0
        self.type = "root"

    def show_node_info(self):
        print("node {0}: parent = {1}, sibling = {2}, degree = {3}, depth = {4}, height = {5}, {6}"\
        .format(self.id, self.parent, self.sibling, self.degree, self.depth, self.height, self.type))

if __name__ == '__main__':
    tree = Tree(int(input()))
    tree.set_tree()
    tree.set_depth_height()
    tree.show_tree_info()