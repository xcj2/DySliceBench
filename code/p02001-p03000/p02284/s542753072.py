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
            return True
        elif self.key < k:
            if self.right:
                return self.right.find(k)
            else:
                return False
        else:
            if self.left:
                return self.left.find(k)
            else:
                return False


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
            return False
        else:
            return self.root.find(k)

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
    else:
        tree.print()
