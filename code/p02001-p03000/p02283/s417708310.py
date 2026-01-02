class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.nodes = []

    def insert(self, z):
        z = Node(z)
        self.nodes.append(z)
        y = None
        x = self.root
        while x is not None:
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
    
    def dfs(self, node):
        self.preorder.append(node.key)
        if node.left is not None:
            self.dfs(node.left)

        self.inorder.append(node.key)

        if node.right is not None:
            self.dfs(node.right)

    def out(self):
        self.preorder = []
        self.inorder = []
        self.dfs(self.root)

        print("", *self.inorder)
        print("", *self.preorder)


class Node:
    def __init__(self, v):
        self.key = v
        self.left = None
        self.right = None
        self.parent = None


def main():
    global preorder
    global inorder
    preorder = []
    inorder = []
    T = BinarySearchTree()
    n = int(input())
    for i in range(n):
        command = input().split()
        if command[0] == "print":
            T.out()
        else:
            T.insert(int(command[1]))



if __name__ == "__main__":
    main()
