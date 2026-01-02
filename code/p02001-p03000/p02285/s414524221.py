# 二分探索　データの削除から　クラス定義を用いて
class Node:
    def __init__(self, key):
        self.key = key
        self.parent = None
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        root_node = self.root
        insert_node = Node(key)
        parent_node = None

        while root_node:
            parent_node = root_node
            if insert_node.key < root_node.key:
                root_node = root_node.left
            else:
                root_node = root_node.right
            
        insert_node.parent = parent_node

        if parent_node == None:
            self.root = insert_node
        elif insert_node.key < parent_node.key:
            parent_node.left = insert_node
        else:
            parent_node.right = insert_node
        
    def find(self, key):
        node = self.root

        while node:
            if node.key == key:
                return node
            elif node.key < key:
                node = node.right
            else:
                node = node.left 

        return None

    def delete(self, key):
        node = self.find(key)

        if node == None:
            return 
        
        if node.left and node.right:
            next_node = node.right

            while next_node.left:
                next_node = next_node.left

            node.key = next_node.key
            node = next_node

        if node.left:
            node.left.parent = node.parent
            if node.parent.left == node:
                node.parent.left = node.left
            else:
                node.parent.right = node.left
        elif node.right:
            node.right.parent = node.parent
            if node.parent.left == node:
                node.parent.left = node.right
            else:
                node.parent.right = node.right
        else:
            if node.parent.left == node:
                node.parent.left = None
            else:
                node.parent.right = None

    def show_inorder(self, node):
        if node == None:
            return 
        self.show_inorder(node.left)
        print(' ' + str(node.key), end = '')
        self.show_inorder(node.right)

    def show_preorder(self, node):
        if node == None:
            return 
        print(' ' + str(node.key), end = '')
        self.show_preorder(node.left)
        self.show_preorder(node.right)

tree = BinarySearchTree()
n = int(input())

for i in range(n):
    command = input().split()

    if command[0] == 'insert':
        tree.insert(int(command[1]))
    elif command[0] == 'find':
        a = tree.find(int(command[1]))
        if a != None:
            print('yes')
        else:
            print('no')        
    elif command[0] == 'delete':
        tree.delete(int(command[1]))
    elif command[0] == 'print':
        tree.show_inorder(tree.root)
        print()
        tree.show_preorder(tree.root)
        print()
