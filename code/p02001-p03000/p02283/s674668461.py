import sys

class Node:
    def __init__(self, x, parent=None):
        self.key = x
        self.left = None
        self.right = None
        self.parent = parent

    def append_child(self, child):
        if self.key > child.key:
            self.left = child
            child.parent = self
        elif self.key < child.key:
            self.right = child
            child.parent = self
        else:
            pass

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, x):
        inserted = Node(x)
        if self.root is None:
            self.root = inserted
            return inserted

        node = self.root
        parent = None
        while node is not None:
            if x > node.key:
                parent = node
                node = node.right
            elif x < node.key:
                parent = node
                node = node.left
            else:
                return node

        parent.append_child(inserted)
        return inserted

    def delete(self, x):
        pass

    def find(self, x):
        node = self.root
        while node is not None:
            if x == node.key:
                return node
            elif x > node.key:
                node = node.right
            else:
                node = node.left
        return None

    def pre_order(self):
        keys = []
        self.do_pre_order(self.root, keys)
        print(' ' + ' '.join(map(str, keys)))

    def do_pre_order(self, node, keys):
        if node is None:
            return
        keys.append(node.key)
        self.do_pre_order(node.left, keys)
        self.do_pre_order(node.right, keys)

    def in_order(self):
        keys = []
        self.do_in_order(self.root, keys)
        print(' ' + ' '.join(map(str, keys)))

    def do_in_order(self, node, keys):
        if node is None:
            return
        self.do_in_order(node.left, keys)
        keys.append(node.key)
        self.do_in_order(node.right, keys)

# main
tree = BinaryTree()
lines = sys.stdin.readlines()

for line in lines[1:]:
    if len(line.rstrip()) == 0:
        continue

    command = line.rstrip().split(' ')

    if command[0] == 'insert':
        tree.insert(int(command[1]))
    elif command[0] == 'print':
        tree.in_order()
        tree.pre_order()
    elif command[0] == 'find':
        if (tree.find(int(command[1]))):
            print('yes')
        else:
            print('no')
    elif command[0] == 'delete':
        tree.remove(int(command[1]))
    else:
        raise 'unknown command: ' + command[0]