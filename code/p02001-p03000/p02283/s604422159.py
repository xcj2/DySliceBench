class Node:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None

    def append(self, node):
        if self.value > node.value:
            if self.left is None:
                node.parent = self
                self.left = node
            else:
                self.left.append(node)
        else:
            if self.right is None:
                node.parent = self
                self.right = node
            else:
                self.right.append(node)

    def in_parse(self, node, lst):
        if node is None:
            return
        self.in_parse(node.left, lst)
        lst.append(str(node.value))
        self.in_parse(node.right, lst)

    def pre_parse(self, node, lst):
        if node is None:
            return
        lst.append(str(node.value))
        self.pre_parse(node.left, lst)
        self.pre_parse(node.right, lst)


class BinaryTree:

    def __init__(self):
        self.root = None

    def insert(self, value):
        node = Node(value)
        if self.root is None:
            self.root = node
        else:
            self.root.append(node)

    def in_parse(self):
        lst = []
        self.root.in_parse(self.root, lst)
        return lst

    def pre_parse(self):
        lst = []
        self.root.pre_parse(self.root, lst)
        return lst


def main():
    n = int(input())
    tree = BinaryTree()

    for _ in range(n):
        line = input().split(' ')
        command = line[0]
        if command == 'insert':
            v = int(line[1])
            tree.insert(v)
        else:
            print(' ' + ' '.join(tree.in_parse()))
            print(' ' + ' '.join(tree.pre_parse()))


if __name__ == '__main__':
    main()

