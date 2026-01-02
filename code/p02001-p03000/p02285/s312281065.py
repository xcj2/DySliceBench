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
            # print(z.key, y.key)
            return y
        else:
            x = z.right
            while x is not None:
                y = x
                x = x.left
            return y

    def delete(self, k):
        z = self.find(k)
        if z.left is None and z.right is None:
            if z.p.key > z.key:
                z.p.left = None
            else:
                z.p.right = None
        elif z.left is not None and z.right is not None:
            y = self.next_node(z)
            tmp = y.key
            self.delete(y.key)
            z.key = tmp
        else:
            if z.right is None:
                z_child = z.left
            else:
                z_child = z.right
            z_child.p = z.p
            if z.p.key > z.key:
                z.p.left = z_child
            else:
                z.p.right = z_child
            
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
            z = Node(k)
            T.insert(z)
        elif q[0]=='find':
            k = int(q[1])
            if T.find(k):
                print('yes')
            else:
                print('no')
        elif q[0]=='delete':
            k = int(q[1])
            T.delete(k)
        else:
            T.print_nodes()
    # print(T.next_node(T.find(1)).key)
    # print(T.next_node(T.find(2)).key)
    # print(T.next_node(T.find(3)).key)
    # print(T.next_node(T.find(7)).key)
    # print(T.next_node(T.find(8)).key)
    # print(T.next_node(T.find(22)).key)

if __name__ == '__main__':
    resolve()

