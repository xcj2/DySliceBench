class Node:
    def __init__(self, key):
        self.right = None
        self.left = None
        self.parent = None
        self.key = key

    def preorder(self):
        ret = [self.key]
        if self.left:
            ret += self.left.preorder()
        if self.right:
            ret += self.right.preorder()
        return ret

    def inorder(self):
        ret = []
        if self.left:
            ret += self.left.inorder()
        ret += [self.key]
        if self.right:
            ret += self.right.inorder()
        return ret

    def find(self, k):
        if self.key == k:
            return self
        elif self.key < k:
            if self.right:
                return self.right.find(k)
            else:
                return None
        else:
            if self.left:
                return self.left.find(k)
            else:
                return None


class Tree:
    def __init__(self):
        self.root = None

    def insert(self, k):
        z = Node(k)
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
        print('', ' '.join(map(str, self.root.inorder())))
        print('', ' '.join(map(str, self.root.preorder())))

    def find(self, k):
        if self.root is None:
            return None
        else:
            return self.root.find(k)

    def delete(self, k):
        z = self.find(k)
        if z.left is None:
            self.transparent(z, z.right)
        elif z.right is None:
            self.transparent(z, z.left)
        else:
            y = self.minimum(z.right)
            if y.parent != z:
                self.transparent(y, y.right)
                y.right = z.right
                y.right.parent = y
            self.transparent(z, y)
            y.left = z.left
            y.left.parent = y

    def successor(self, x):
        if x.right:
            return self.minimum(x.right)
        y = x.parent
        while y and x == y.right:
            x = y
            y = y.parent
        return y

    def minimum(self, x):
        while x.left:
            x = x.left
        return x

    def maximum(self, x):
        while x.right:
            x = x.right
        return x

    def transparent(self, u, v):
        if u.parent is None:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        if v:
            v.parent = u.parent


m = int(input())
tree = Tree()
for _ in range(m):
    s = input().split()
    if s[0] == "insert":
        tree.insert(int(s[1]))
    elif s[0] == "find":
        if tree.find(int(s[1])):
            print("yes")
        else:
            print("no")
    elif s[0] == "delete":
        tree.delete(int(s[1]))
    else:
        tree.print()
