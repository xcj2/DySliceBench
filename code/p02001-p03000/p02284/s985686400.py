import sys

class Node:
    def __init__(self, x):
        self.key = x
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, x):
        if self.root is None:
            self.root = Node(x)
            return self

        node = self.root
        while True:
            if x > node.key:
                if node.right is None:
                    node.right = Node(x)
                    break
                else:
                    node = node.right
            elif x < node.key:
                if node.left is None:
                    node.left = Node(x)
                    break
                else:
                    node = node.left
            else:
                break

        return self

    def find(self, x):
        node = self.root
        while node is not None:
            if x == node.key:
                return True
            elif x < node.key:
                node = node.left
            else:
                node = node.right
        return False

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
    else:
        raise 'unknown command: ' + command[0]