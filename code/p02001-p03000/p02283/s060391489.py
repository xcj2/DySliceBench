import sys


class BinarySearchTree:
    class Node:
        def __init__(self, value):
            self.value = value
            self.left = None
            self.right = None

        def has_left(self):
            return self.left is not None

        def has_right(self):
            return self.right is not None

        def __str__(self):
            return str(self.value)

    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = self.Node(value)
            return

        node = self.root
        while True:
            if node.value > value:
                if node.has_left():
                    node = node.left
                else:
                    node.left = self.Node(value)
                    break
            else:
                if node.has_right():
                    node = node.right
                else:
                    node.right = self.Node(value)
                    break

    def preorder(self):
        def _preorder(node):
            yield node
            if node.has_left():
                yield from _preorder(node.left)
            if node.has_right():
                yield from _preorder(node.right)
        if self.root is not None:
            yield from _preorder(self.root)

    def inorder(self):
        def _inorder(node):
            if node.has_left():
                yield from _inorder(node.left)
            yield node
            if node.has_right():
                yield from _inorder(node.right)
        if self.root is not None:
            yield from _inorder(self.root)

    def postorder(self):
        def _postorder(node):
            if node.has_left():
                yield from _postorder(node.left)
            if node.has_right():
                yield from _postorder(node.right)
            yield node
        if self.root is not None:
            yield from _postorder(self.root)


def run():
    _ = int(input())
    tree = BinarySearchTree()

    for line in sys.stdin:
        command = line.split()
        if command[0] == 'insert':
            tree.insert(int(command[1]))
        elif command[0] == 'print':
            inorder = ''
            for node in tree.inorder():
                inorder += " {}".format(node)
            print(inorder)
            preorder = ''
            for node in tree.preorder():
                preorder += " {}".format(node)
            print(preorder)
        else:
            raise ValueError('invalid command')


if __name__ == '__main__':
    run()

