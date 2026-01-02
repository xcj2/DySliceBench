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

    def find(self, key, x=0):
        while x != -1 and key != self.tree[x].key:
            if key < self.tree[x].key:
                x = self.tree[x].l
            else:
                x = self.tree[x].r
        return x

    def delete(self, key):
        node = self.find(key)
        self.delete_node(node)

    def delete_node(self, z):
        if self.tree[z].l == -1 or self.tree[z].r == -1:
            y = z
        else:
            y = self.get_successor(z)
        if self.tree[y].l != -1:
            x = self.tree[y].l
        else:
            x = self.tree[y].r
        if x != -1:
            self.tree[x].p = self.tree[y].p
        if self.tree[y].p == -1:
            self.root = x
        elif y == self.tree[self.tree[y].p].l:
            self.tree[self.tree[y].p].l = x
        else:
            self.tree[self.tree[y].p].r = x
        if y != z:
            self.tree[z].key = self.tree[y].key

    def get_successor(self, x):
        if self.tree[x].r != -1:
            return self.get_minimum(self.tree[x].r)
        y = self.tree[x].p
        while y != -1 and x == self.tree[y].r:
            x = y
            y = self.tree[y].p
        return y

    def get_minimum(self, x):
        while self.tree[x].l != -1:
            x = self.tree[x].l
        return x

    def preorder_traversal(self, u=0):
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
        elif order[0] == 'find':
            key = int(order[1])
            print('yes' if bst.find(key) != -1 else 'no')
        elif order[0] == 'delete':
            key = int(order[1])
            bst.delete(key)


if __name__ == '__main__':
    main()

