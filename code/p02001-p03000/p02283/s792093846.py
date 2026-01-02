import sys


class Node():
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None

    def preorder(self):
        nodeList = [self.key]
        if self.left:
            nodeList += self.left.preorder()
        if self.right:
            nodeList += self.right.preorder()
        return nodeList

    def inorder(self):
        nodeList = []
        if self.left:
            nodeList += self.left.inorder()
        nodeList += [self.key]
        if self.right:
            nodeList += self.right.inorder()
        return nodeList


class BinaryTree():
    def __init__(self):
        self.root = None

    def insert(self, key):
        z = Node(key)
        y = None
        x = self.root
        while x:
            y = x
            if z.key < x.key:
                x = x.left
            else:
                x = x.right
        z.parent = y

        if y is None:
            self.root = z
        elif z.key < y.key:
            y.left = z
        else:
            y.right = z

    def print(self):
        print(" " + " ".join(map(str, self.root.inorder())))
        print(" " + " ".join(map(str, self.root.preorder())))


if __name__ == "__main__":
    tree = BinaryTree()
    n = int(sys.stdin.readline())
    for inp in sys.stdin.readlines():
        inp = inp.split()
        if inp[0] == "insert":
            tree.insert(int(inp[1]))
        else:
            tree.print()