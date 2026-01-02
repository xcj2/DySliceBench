class BinarySearchTree:
    class __Node:
        def __init__(self, key=-1, parent=-1, left=-1, right=-1):
            self.key = key
            self.parent = parent
            self.left = left
            self.right = right

    def __init__(self):
        self.root = -1

    def insert(self, z):
        node = BinarySearchTree.__Node(key=z)
        x, y = self.root, -1
        while x != -1:
            y = x
            if z < x.key:
                x = x.left
            else:
                x = x.right

        node.parent = y

        if y == -1:
            self.root = node
        elif z < y.key:
            y.left = node
        else:
            y.right = node

    def find(self, k):
        x = self.root
        while x != -1 and k != x.key:
            if k < x.key:
                x = x.left
            else:
                x = x.right

        return x

    def print_tree(self):
        def in_order(z):
            if z == -1:
                return

            in_order(z.left)
            print(" {}".format(z.key), end="")
            in_order(z.right)

        def pre_order(z):
            if z == -1:
                return

            print(" {}".format(z.key), end="")
            pre_order(z.left)
            pre_order(z.right)

        in_order(self.root)
        print()
        pre_order(self.root)
        print()


def main():
    n = int(input())
    bst = BinarySearchTree()

    for i in range(n):
        order = input().split()
        if order[0][0] == "i":
            bst.insert(int(order[1]))
        elif order[0][0] == "f":
            if bst.find(int(order[1])) == -1:
                print("no")
            else:
                print("yes")
        else:
            bst.print_tree()


if __name__ == '__main__':
    main()

