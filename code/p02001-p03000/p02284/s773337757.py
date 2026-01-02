import sys
my_input = sys.stdin.readline


class BinarySearchTree:
    class Node:
        def __init__(self, key):
            __slots__ = ['key', 'left', 'right', 'parent']
            self.key = key
            self.left = None
            self.right = None
            self.parent = None

    def __init__(self):
        self.root = None

    def insert(self, target_key):
        parent = None
        attention = self.root
        target = self.Node(target_key)

        while attention:
            parent = attention
            if target.key < attention.key:
                attention = attention.left
            else:
                attention = attention.right
        target.parent = parent

        if parent is None:
            self.root = target
        elif target.key < parent.key:
            parent.left = target
        else:
            parent.right = target

    def find(self, target_key):
        attention = self.root
        while attention:
            if attention and (attention.key == target_key):
                return attention

            if target_key < attention.key:
                attention = attention.left
            else:
                attention = attention.right

        return False

    def preorder_walk(self, node):
        if node is None:
            return []
        return [node.key] + self.preorder_walk(node.left) + self.preorder_walk(node.right)

    def inorder_walk(self, node):
        if node is None:
            return []
        return self.inorder_walk(node.left) + [node.key] + self.inorder_walk(node.right)


N = int(my_input())
BST = BinarySearchTree()
for _ in range(N):
    command = my_input().split()
    if command[0] == 'insert':
        BST.insert(int(command[1]))

    elif command[0] == 'find':
        print('yes' if BST.find(int(command[1])) else 'no')

    elif command[0] == 'print':
        print(' ' + ' '.join(map(str, BST.inorder_walk(BST.root))))
        print(' ' + ' '.join(map(str, BST.preorder_walk(BST.root))))

