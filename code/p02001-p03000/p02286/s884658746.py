import sys, collections
input = lambda: sys.stdin.readline().rstrip() 
sys.setrecursionlimit(10**7)
INF = 10**10
def I(): return int(input())
def F(): return float(input())
def SS(): return input()
def LI(): return [int(x) for x in input().split()]
def LI_(): return [int(x)-1 for x in input().split()]
def LF(): return [float(x) for x in input().split()]
def LSS(): return input().split()

class Node():
    key = None
    priority = None
    p = None
    left = None
    right = None

    def __init__(self, key, priority):
        self.key = key
        self.priority = priority

class BinarySearchTree():
    root = None

    def rightRotate(self, t):
        s = t.left
        t.left = s.right
        s.right = t
        return s

    def leftRotate(self, t):
        s = t.right
        t.right = s.left
        s.left = t
        return s

    def insert(self, t, key, priority):
        if t is None:
            return Node(key, priority)
        if key==t.key:
            return t

        if key < t.key:
            t.left = self.insert(t.left, key, priority)
            if t.priority < t.left.priority:
                t = self.rightRotate(t)
        else:
            t.right = self.insert(t.right, key, priority)
            if t.priority < t.right.priority:
                t = self.leftRotate(t)
        
        return t

    def find(self, k):
        x = self.root
        while x is not None:
            if x.key==k:
                return x
            elif x.key>k:
                x = x.left
            else:
                x = x.right
        return None

    def next_node(self, z):
        if z.right is None:
            x = z
            y = z.p
            while y is not None and y.left!=x:
                x = y
                y = y.p
            return y
        else:
            x = z.right
            while x is not None:
                y = x
                x = x.left
            return y

    def delete(self, t, key):
        if t is None:
            return None
        if key < t.key:
            t.left = self.delete(t.left, key)
        elif key > t.key:
            t.right = self.delete(t.right, key)
        else:
            return self._delete(t, key)
        return t

    def _delete(self, t, key):
        if t.left is None and t.right is None:
            return None
        elif t.left is None:
            t = self.leftRotate(t)
        elif t.right is None:
            t = self.rightRotate(t)
        else:
            if t.left.priority > t.right.priority:
                t = self.rightRotate(t)
            else:
                t = self.leftRotate(t)
        return self.delete(t, key)
            
    def print_nodes(self):
        inorder = []
        preorder = []

        def dfs(v):
            v_key = v.key
            preorder.append(v_key)
            if v.left is not None:
                dfs(v.left)
            inorder.append(v_key)
            if v.right is not None:
                dfs(v.right)

        dfs(self.root)

        print('', *inorder)
        print('', *preorder)

def resolve():
    m = I()
    T = BinarySearchTree()
    for _ in range(m):
        q = LSS()
        if q[0]=='insert':
            k = int(q[1])
            p = int(q[2])
            T.root = T.insert(T.root, k, p)
        elif q[0]=='find':
            k = int(q[1])
            if T.find(k):
                print('yes')
            else:
                print('no')
        elif q[0]=='delete':
            k = int(q[1])
            T.root = T.delete(T.root, k)
        else:
            T.print_nodes()

if __name__ == '__main__':
    resolve()

