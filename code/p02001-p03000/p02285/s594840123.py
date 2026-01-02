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

    def find(self, key):
        x = self.root
        while x is not None and key != x.key:
            if key < x.key:
                x = x.left
            else:
                x = x.right
        return x

    def delete(self, key):
        z = self.find(key)
        if z is not None:
            if z.left is not None and z.right is not None:
                temp = self.getMinimum(z.right)
                self.delete(temp.key)
                z.key = temp.key
            elif z.left is not None:
                if z.parent is None:
                    self.root = z.left
                    z.left.parent = None
                else:
                    if z.parent.left is z:
                        z.parent.left = z.left
                    else:
                        z.parent.right = z.left
                    z.left.parent = z.parent
            elif z.right is not None:
                if z.parent is None:
                    self.root = z.right
                    z.right.parent = None
                else:
                    if z.parent.left is z:
                        z.parent.left = z.right
                    else:
                        z.parent.right = z.right
                    z.right.parent = z.parent
            else:
                if z.parent is None:
                    self.root = None
                else:
                    if z.parent.left is z:
                        z.parent.left = None
                    else:
                        z.parent.right = None

    def getMinimum(self, node):
        while node.left is not None:
            node = node.left
        return node

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
        elif inp[0] == "find":
            if tree.find(int(inp[1])) is None:
                print("no")
            else:
                print("yes")
        elif inp[0] == "delete":
            tree.delete(int(inp[1]))
        else:
            tree.print()