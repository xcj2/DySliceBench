class Node:
    def __init__(self, key, parent=None, left=None, right=None):
        self.key = key
        self.parent = parent
        self.left = left
        self.right = right
         
 
def get_minimum(node):
    x = node
    while x.left is not None:
        x = x.left
    return x
 
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
            x = x.left if (k < x.key) else x.right            
        return x
 
    def delete_node(self, z):
        # determine y, the node to be deleted
        y = z if ((z.left is None) or (z.right is None)) else get_minimum(z.right)
        # determine x, the child of y (note that y has at most one child)
        x = y.left if (y.left is not None) else y.right
        # set the parent of x (if x is not None)
        if x is not None:
            x.parent = y.parent
         
        if y.parent is None:
            self.root_node = x
        elif y is y.parent.left:
            y.parent.left = x
        else:
            y.parent.right = x
         
        if y is not z:
            z.key = y.key
    
 
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
    elif command[0] == 'delete':
        x = tree.find(int(command[1]))
        tree.delete_node(x)
    else:
        key = int(command[1])
        new_node = Node(key)
        tree.insert(new_node)


