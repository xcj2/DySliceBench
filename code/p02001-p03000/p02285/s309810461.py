class BSTree:
    def __init__(self):
        self.value, self.left, self.right = (None,) * 3

    def add(self, x):
        if self.value is None:
            self.value = x
        elif x < self.value:
            if self.left is None:
                self.left = BSTree()
            self.left.add(x)
        else:
            if self.right is None:
                self.right = BSTree()
            self.right.add(x)

    def find(self, x):
        if self.value == x:
            return True
        if self.left is not None and x < self.value:
            return self.left.find(x)
        if self.right is not None and self.value < x:
            return self.right.find(x)
        return False

    def delete_min(self):
        if self.left is None:
            return self.value, None
        else:
            value, self.left = self.left.delete_min()
            return value, self

    def delete(self, x):
        if self.value == x:
            if self.left is not None and self.right is not None:
                self.value, self.right = self.right.delete_min()
            else:
                return self.left or self.right
        elif x < self.value and self.left is not None:
            self.left = self.left.delete(x)
        elif self.value < x and self.right is not None:
            self.right = self.right.delete(x)
        return self

    def preorder(self):
        def get(t):
            return [] if t is None else t.preorder()
        return [self.value] + get(self.left) + get(self.right)

    def inorder(self):
        def get(t):
            return [] if t is None else t.inorder()
        return get(self.left) + [self.value] + get(self.right)


def print_list(l):
    print(' ' + ' '.join(map(str, l)))


def main():
    n = input()
    t = BSTree()
    for _ in range(int(n)):
        ip = input().split()
        if len(ip) == 1:
            print_list(t.inorder())
            print_list(t.preorder())
        else:
            command, k = ip[0], int(ip[1])
            if command == 'insert':
                t.add(k)
            elif command == 'find':
                print('yes' if t.find(k) else 'no')
            else:
                t = t.delete(k)


if __name__ == '__main__':
    main()

