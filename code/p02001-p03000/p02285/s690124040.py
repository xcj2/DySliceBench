class Node:
    def __init__(self, key, parent=None, left=None, right=None):
        self.key = key
        self.parent = parent
        self.left = left
        self.right = right

class Tree:
    root = None
    preorder_list = []
    inorder_list = []
    def __init__(self):
        pass
    def insert(self, node):
        y = None
        x = self.root

        while x is not None:
            y = x
            if node.key < x.key:
                x = x.left
            else:
                x = x.right
        node.parent = y

        if y == None:
            self.root = node
        elif node.key < y.key:
            y.left = node
        else:
            y.right = node

    def find(self, node):
        y = None
        x = self.root
        while x is not None:
            if node.key == x.key:
                return x
            elif node.key < x.key:
                x = x.left
            else:
                x = x.right
        return None

    def delete(self, node):
        y = None
        x = self.root

        while x is not None:
            y = x
            if node.key < x.key:
                x = x.left
            elif node.key > x.key:
                x = x.right
            else:
                break
        if y.left is None and y.right is None:
            if y.parent.left == y:
                y.parent.left = None
            if y.parent.right == y:
                y.parent.right = None
        elif y.left is None or y.right is None:
            tmp = y.left or y.right
            tmp.parent = y.parent
            if tmp.parent.left == y:
                tmp.parent.left = tmp
            if tmp.parent.right == y:
                tmp.parent.right = tmp
        else:
            tmp = self.successor(y)
            y.key = tmp.key
            if tmp.parent.left == tmp:
                tmp.parent.left = None
            if tmp.parent.right == tmp:
                tmp.parent.right = None

            pass

    def successor(self, node):
        node = node.right
        while node.left:
            node = node.left
        return node

    def display(self):
        #print(self.root, self.root.key, self.root.parent, self.root.left, self.root.right)
        self.inorder(self.root)
        self.preorder(self.root)
        print(' '+' '.join(map(str, self.inorder_list)))
        print(' '+' '.join(map(str, self.preorder_list)))
        pass

    def preorder(self, node):
        if node == None:
            return
        self.preorder_list.append(node.key)
        if node.left is not None:
            self.preorder(node.left)
        if node.right is not None:
            self.preorder(node.right)

    def inorder(self, node, depth=0):
        if node == None:
            return
        if node.left is not None:
            self.inorder(node.left)
        self.inorder_list.append(node.key)
        if node.right is not None:
            self.inorder(node.right)

n = int(input())
command_list = [list(input().split()) for _ in range(n)]

tree = Tree()
for command in command_list:
    if command[0] == 'insert':
        node = Node(int(command[1]))
        tree.insert(node)
        #print(node, node.key, node.parent, node.left, node.right)
    if command[0] == 'print':
        tree.display()
        tree.preorder_list = []
        tree.inorder_list = []
    if command[0] == 'find':
        if tree.find(Node(int(command[1]))) is None:
            print('no')
        else:
            print('yes')
    if command[0] == 'delete':
        result = tree.delete(Node(int(command[1])))





