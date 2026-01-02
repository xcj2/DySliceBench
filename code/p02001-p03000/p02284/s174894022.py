class Tree:
    root = None

    def insert(self, node):
        y = None
        x = self.root
        while x:
            y = x
            x = x.left if node.key < x.key else x.right

        if not y:
            self.root = node
        elif node.key < y.key:
            y.left = node
        else:
            y.right = node

    def find(self, value):
        print('yes' if self.root.find(value) else 'no')

    def print(self):
        print(' ', end='')
        print(*self.root.print_in())
        print(' ', end='')
        print(*self.root.print_pre())


class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.key = key

    def find(self, value):
        diff = self.key - value
        if diff == 0:
            return True
        elif diff > 0:
            return self.left and self.left.find(value)
        else:
            return self.right and self.right.find(value)

    def print_pre(self):
        yield self.key
        if self.left:
            for k in self.left.print_pre(): yield k
        if self.right:
            for k in self.right.print_pre(): yield k

    def print_in(self):
        if self.left:
            for k in self.left.print_in(): yield k
        yield self.key
        if self.right:
            for k in self.right.print_in(): yield k


tree = Tree()
m = int(input())

while m:
    l = input()
    f = l[0]
    if f == 'i':
        tree.insert(Node(int(l.split()[1])))
    elif f == 'f':
        tree.find(int(l.split()[1]))
    else:
        tree.print()
    m -= 1