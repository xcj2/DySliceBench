class Node:
    def __init__(self, key, parent=None, left=None, right=None):
        self.key = key
        self.parent = parent
        self.left = left
        self.right = right
        

class Tree:
    def __init__(self):
        self.root_node = None
        
    def insert(self, z):
        y = None # y stands for the parent of x
        x = self.root_node # root node
        # First, we ascend the tree until the point where we insert the new node
        while x is not None:
            y = x # set parent
            if z.key < x.key:
                x = x.left # move to the left child
            else:
                x = x.right # move to the right child
        # insert z under y
        z.parent = y
        
        if y is None:
            # when the tree is empty
            self.root_node = z
        elif z.key < y.key:
            y.left = z
        else:
            y.right = z
    
    def find(self, k):
        x = self.root_node
        while (x is not None) and (x.key != k):
            if k < x.key:
                x = x.left
            else:
                x = x.right
        return x
        
    
    def print_preorder(self, node):
        print(f" {node.key}", end="")
        if node.left is not None:
            self.print_preorder(node.left)
        if node.right is not None:
            self.print_preorder(node.right)

    def print_inorder(self, node):
        if node.left is not None:
            self.print_inorder(node.left)
        print(f" {node.key}", end="")
        if node.right is not None:
            self.print_inorder(node.right)

    def print_nodes(self):
        if self.root_node is None:
            pass
        else:
            self.print_inorder(self.root_node)
            print("")
            self.print_preorder(self.root_node)
            print("")

        
tree = Tree()

m = int(input())

for _ in range(m):
    command = input().split()
    if command[0] == 'print':
        tree.print_nodes()
    elif command[0] == 'find':
        node = tree.find(int(command[1]))
        print("no") if (node is None) else print("yes")
    else:
        key = int(command[1])
        new_node = Node(key)
        tree.insert(new_node)
