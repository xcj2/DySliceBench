class Tree():
    def __init__(self):
        self.root = None

    def insert(self, z):
        y = None
        x = self.root
        while x:
            y = x
            if z.key < x.key:
                x = x.left
            else:
                x = x.right
        z.p = y

        if not y:
            self.root = z
        elif z.key < y.key:
            y.left = z
        else:
            y.right = z

    def find(self, key):
        node = self.root
        while node:
            if node.key == key:
                return True
            if key < node.key:
                node = node.left
            else:
                node = node.right
        return False

    def show(self):
        self.root.inorder()
        print()
        self.root.preorder()
        print()


class Node():
    def __init__(self, key):
        self.key = key
        self.p, self.left, self.right = None, None, None

    def inorder(self):
        if self.left:
            self.left.inorder()
        print(" {}".format(self.key), end="")
        if self.right:
            self.right.inorder()

    def preorder(self):
        print(" {}".format(self.key), end="")
        if self.left:
            self.left.preorder()
        if self.right:
            self.right.preorder()


tree = Tree()
n = int(input())
for _ in range(n):
    cmd = input().split()
    if cmd[0] == "insert":
        tree.insert(Node(int(cmd[1])))
    elif cmd[0] == "find":
        print("yes" if tree.find(int(cmd[1])) else "no")
    else:
        tree.show()