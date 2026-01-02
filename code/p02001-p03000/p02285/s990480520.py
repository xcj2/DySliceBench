class Node():
    def __init__(self, key):
        self.parent = None
        self.left = None
        self.right = None
        self.key = key

class Tree():
    def __init__(self):
        self.root = None
    
    def insert(self, key):
        z = Node(key)
        y = None
        x = self.root
        
        while x:
            y = x
            if z.key < x.key:
                x = x.left
            else:
                x = x.right
        z.parent = y
        
        if y == None:
            self.root = z
        elif z.key < y.key:
            y.left = z
        else:
            y.right = z
            
    def find(self, key):
        node = self.root
        
        while node:
            if node.key == key:
                return node
            elif node.key > key:
                node = node.left
            else:
                node = node.right
        
        return None
    
    def delete(self, key):
        node = self.find(key)
        
        if node.left and node.right:
            right_min = node.right
            while right_min.left:
                right_min = right_min.left
            node.key = right_min.key
            node = right_min
        
        if node.left or node.right:
            child = node.left if node.left else node.right
            if node.parent.left == node:
                node.parent.left = child
                child.parent = node.parent
            else:
                node.parent.right = child
                child.parent = node.parent
        else:
            if node.parent.left == node:
                node.parent.left = None
            else:
                node.parent.right = None
                
    def preorder(self, node):
        print(" {}".format(node.key), end = "")
        
        if node.left:
            self.preorder(node.left)
        if node.right:
            self.preorder(node.right)
    
    def inorder(self, node):
        if node.left:
            self.inorder(node.left)
            
        print(" {}".format(node.key), end = "")
        
        if node.right:
            self.inorder(node.right)
            
    def out(self):
        self.inorder(self.root)
        print('')
        self.preorder(self.root)
        print('')

tree = Tree()
N = int(input())
for _ in range(N):
    order = input().split()
    if order[0] == 'insert':
        tree.insert(int(order[1]))
    elif order[0] == 'find':
        print('yes' if tree.find(int(order[1])) else 'no')
    elif order[0] == 'delete':
        tree.delete(int(order[1]))
    else:
        tree.out()