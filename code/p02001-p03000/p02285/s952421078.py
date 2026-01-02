class Tree:
    def __init__(self, orders):
        self.root = None
        for order in orders:
            if len(order) == 1:
                self.inorder_print()
                self.preorder_print()
            else:
                fchr = order[0][0]
                key = int(order[1])
                if fchr == 'f':
                    self.find(key)
                elif fchr == 'i':
                    self.insert(key)
                else:
                    self.delete(key)

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
        if not y:
            self.root = z
        elif z.key < y.key:
            y.left = z
        else:
            y.right = z

    def find(self, key):
        x = self.root
        while True:
            if key == x.key:
                print('yes')
                break
            elif key < x.key:
                if x.left:
                    x = x.left
                else:
                    print('no')
                    break
            else:
                if x.right:
                    x = x.right
                else:
                    print('no')
                    break

    def delete(self, key):
        z = self.root
        while z.key != key:
            if key < z.key:
                z = z.left
            else:
                z = z.right

        if not z.left or not z.right:
            y = z
        else:
            y = self.get_successor(z)

        if y.left:
            x = y.left
        else:
            x = y.right

        if x:
            x.parent = y.parent

        if not y.parent:
            self.root = x
        elif y == y.parent.left:
            y.parent.left = x
        else:
            y.parent.right = x

        if y != z:
            z.key = y.key

        del (y)

    def get_successor(self, x):
        if x.right:
            return self.get_minimum(x.right)

        y = x.parent
        while y and x == y.right:
            x = y
            y = y.parent
        return y

    def get_minimum(self, x):
        while x.left:
            x = x.left
        return x

    def inorder_print(self):
        self.root.inorder_print()
        print()

    def preorder_print(self):
        self.root.preorder_print()
        print()


class Node:
    def __init__(self, key):
        self.key = key
        self.parent = None
        self.left = None
        self.right = None

    def inorder_print(self):
        if self.left:
            self.left.inorder_print()
        print(' {}'.format(self.key), end='')
        if self.right:
            self.right.inorder_print()

    def preorder_print(self):
        print(' {}'.format(self.key), end='')
        if self.left:
            self.left.preorder_print()
        if self.right:
            self.right.preorder_print()


if __name__ == '__main__':
    import sys
    m = int(input())
    orders = [line.strip().split() for line in sys.stdin]
    Tree(orders)

