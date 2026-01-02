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
    p = None
    left = None
    right = None

    def __init__(self, key):
        self.key = key

class BinarySearchTree():
    root = None

    def insert(self, z):
        y = None
        x = self.root
        while x is not None:
            y = x
            if z.key < x.key:
                x = x.left
            else:
                x = x.right
        
        z.p = y

        if y is None:
            self.root = z
        elif z.key < y.key:
            y.left = z
        else:
            y.right = z

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
    n = I()
    T = BinarySearchTree()
    for _ in range(n):
        q = LSS()
        if q[0]=='insert':
            z = Node(int(q[1]))
            T.insert(z)
        else:
            T.print_nodes()

if __name__ == '__main__':
    resolve()

