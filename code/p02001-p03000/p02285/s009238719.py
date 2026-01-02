import sys

class BinarySearchTree:
    class Node:
        __slots__ = ('value', 'left', 'right')

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

    def find(self, value):
        if self.root is None:
            return False

        node = self.root
        while True:
            if node.value > value:
                if node.has_left():
                    node = node.left
                else:
                    return False
            elif node.value < value:
                if node.has_right():
                    node = node.right
                else:
                    return False
            else:
                return True

    def delete(self, value):
        def _delete(node):
            if not node.has_left():
                right = node.right
                node.right = None
                return right
            elif not node.has_right():
                left = node.left
                node.left = None
                return left
            elif not node.right.has_left():
                right = node.right
                right.left = node.left
                node.left = None
                node.right = None
                return right
            else:
                repl = node.right
                while repl.has_left() and repl.left.has_left():
                    repl = repl.left

                left = repl.left
                node.value = left.value
                repl.left = left.right
                left.right = None
                return node

        if self.root is None:
            return
        elif self.root.value == value:
            self.root = _delete(self.root)
            return

        node = self.root
        while True:
            if node.value > value:
                if not node.has_left():
                    break
                if node.left.value == value:
                    node.left = _delete(node.left)
                    break
                else:
                    node = node.left
            elif node.value < value:
                if not node.has_right():
                    break
                if node.right.value == value:
                    node.right = _delete(node.right)
                    break
                else:
                    node = node.right
            else:
                raise Exception('should not reached')

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
        if line.startswith('insert'):
            tree.insert(int(line[7:]))
        elif line.startswith('find'):
            if tree.find(int(line[5:])):
                print("yes")
            else:
                print("no")
        elif line.startswith('delete'):
            tree.delete(int(line[7:]))
        elif line.startswith('print'):
            print(' {}'.format(' '.join([str(n) for n in tree.inorder()])))
            print(' {}'.format(' '.join([str(n) for n in tree.preorder()])))
        else:
            raise ValueError('invalid command')


if __name__ == '__main__':
    run()

