class Node():
    def __init__(self, key, p, l, r):
        self.key, self.p, self.l, self.r = key, p, l, r


class BinarySearchTree():
    def __init__(self):
        self.tree = []
        self.root = -1

    def insert(self, key):
        y = -1  # parent of x
        x = self.root
        while x != -1:
            y = x
            if key < self.tree[x].key:
                x = self.tree[x].l
            else:
                x = self.tree[x].r
        self.tree.append(Node(key, y, -1, -1))
        z = len(self.tree) - 1
        if y == -1:
            self.root = z
        elif key < self.tree[y].key:
            self.tree[y].l = z
        else:
            self.tree[y].r = z

    def preorder_traversal(self, u):
        if u == -1:
            return
        print(' ' + str(self.tree[u].key), end='')
        self.preorder_traversal(self.tree[u].l)
        self.preorder_traversal(self.tree[u].r)

    def inorder_traversal(self, u):
        if u == -1:
            return
        self.inorder_traversal(self.tree[u].l)
        print(' ' + str(self.tree[u].key), end='')
        self.inorder_traversal(self.tree[u].r)


def main():
    n = int(input())
    bst = BinarySearchTree()
    for _ in range(n):
        order = input().split()
        if order[0] == 'insert':
            key = int(order[1])
            bst.insert(key)
        elif order[0] == 'print':
            bst.inorder_traversal(0)
            print('')
            bst.preorder_traversal(0)
            print('')


if __name__ == '__main__':
    main()

