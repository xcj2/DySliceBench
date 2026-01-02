class Node:
    def __init__(self, key):
        self.key = key
        self.left = self.right = self.parent = None
    
class BST:
    def __init__(self):
        self.root = None

    def insert(self, key):
        new = Node(key)
        parent = None
        current = self.root
        while current != None:
            parent = current
            if key < current.key:
                current = current.left
            else:
                current = current.right
        if parent == None:
            self.root = new
        elif key < parent.key:
            parent.left = new
        else:
            parent.right = new

    def find(self, k):
        x = self.root
        while x != None and k != x.key:
            if k < x.key:
                x = x.left
            else:
                x = x.right
        if x != None:
            print('yes')
        else:
            print('no')
        
    def print(self):
        self.print_in_order(self.root)
        print()
        self.print_pre_order(self.root)
        print()

    def print_in_order(self, node):
        if node != None:
            self.print_in_order(node.left)
            print(' ' + str(node.key), end = '')
            self.print_in_order(node.right)
    
    def print_pre_order(self, node):
        if node != None:
            print(' ' + str(node.key), end = '')
            self.print_pre_order(node.left)
            self.print_pre_order(node.right)
        
n = int(input())
bst = BST()
for i in range(n):
    cmd = list(map(str, input().split()))
    if cmd[0] == 'print':
        bst.print()
    elif cmd[0] == 'find':
        bst.find(int(cmd[1]))
    else:
        key = int(cmd[1])
        if cmd[0] == 'insert':
            bst.insert(int(cmd[1]))
