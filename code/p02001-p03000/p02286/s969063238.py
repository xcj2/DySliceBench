class Node:
    def __init__(self, key, priority):
        self.right = None
        self.left = None
        self.parent = None
        self.key = key
        self.priority = priority

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


class Treap:
    def __init__(self):
        self.root = None

    def right_rotate(self, t):
        s = t.left
        t.left = s.right
        s.right = t
        return s

    def left_rotate(self, t):
        s = t.right
        t.right = s.left
        s.left = t
        return s

    def insert(self, k, p):
        self.root = self._insert(self.root, k, p)

    def _insert(self, t, k, p):
        if t is None:
            return Node(k, p)
        if k == t.key:
            return t
        if k < t.key:
            t.left = self._insert(t.left, k, p)
            if t.priority < t.left.priority:
                t = self.right_rotate(t)
        else:
            t.right = self._insert(t.right, k, p)
            if t.priority < t.right.priority:
                t = self.left_rotate(t)
        return t

    def print(self):
        if self.root is None:
            print()
        else:
            print('', ' '.join(map(str, self.root.inorder())))
            print('', ' '.join(map(str, self.root.preorder())))

    def find(self, k):
        if self.root is None:
            return None
        else:
            return self.root.find(k)

    def delete(self, k):
        self.root = self._delete(self.root, k)

    def _delete(self, t, k):
        if t is None:
            return None
        if k < t.key:
            t.left = self._delete(t.left, k)
        elif k > t.key:
            t.right = self._delete(t.right, k)
        else:
            return self._else_delete(t, k)
        return t

    def _else_delete(self, t, k):
        if t.left is None and t.right is None:
            return None
        elif t.left is None:
            t = self.left_rotate(t)
        elif t.right is None:
            t = self.right_rotate(t)
        else:
            if t.left.priority > t.right.priority:
                t = self.right_rotate(t)
            else:
                t = self.left_rotate(t)
        return self._delete(t, k)


m = int(input())
treap = Treap()
for _ in range(m):
    s = input().split()
    if s[0] == "insert":
        treap.insert(int(s[1]), int(s[2]))
    elif s[0] == "find":
        if treap.find(int(s[1])):
            print("yes")
        else:
            print("no")
    elif s[0] == "delete":
        treap.delete(int(s[1]))
    else:
        treap.print()
