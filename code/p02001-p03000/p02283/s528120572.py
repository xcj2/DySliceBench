from sys import stdin

class Node:
    def __init__(self, v, parent=None, left=None, right=None):
        self.value = v
        self.parent = parent
        self.left = left
        self.right = right

class BST:
    def __init__(self):
        self.root = None

    def insert(self, v):
        cur = self.root
        cur_p = None
        while cur != None:
            cur_p = cur
            if v < cur.value:
                cur = cur.left
            elif v > cur.value:
                cur = cur.right

        n = Node(v, cur_p)
        if cur_p == None:
            self.root = n
        elif v < cur_p.value:
            cur_p.left = n
        else:
            cur_p.right = n

    def preorder(self):

        def rec_preorder(t=self.root):
            if t != None:
                print(" ", t.value, sep="", end="")
                rec_preorder(t.left)
                rec_preorder(t.right)

        rec_preorder()
        print()

    def inorder(self):

        def rec_inorder(t=self.root):
            if t != None:
                rec_inorder(t.left)
                print(" ", t.value, sep="", end="")
                rec_inorder(t.right)

        rec_inorder()
        print()

m = int(stdin.readline().rstrip())
t = BST()
for _ in range(m):
    q = stdin.readline().rstrip().split()
    if q[0] == "insert":
        t.insert(int(q[1]))
    elif q[0] == "print":
        t.inorder()
        t.preorder()
