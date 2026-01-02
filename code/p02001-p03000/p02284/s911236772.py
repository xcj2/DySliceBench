from sys import stdin

class Node(object):
    def __init__(self, parent=None, left=None, right=None):
        self.parent = parent
        self.left = left
        self.right = right

class BinarySearchTree(object):
    def __init__(self):
        self.tree = {}
        self.root = None

    def insert(self, z):
        if not self.tree:
            self.tree[z] = Node(parent=-1)
            self.root = z
        else:
            x = self.root
            while x != None:
                y = x
                if z < x:
                    x = self.tree[x].left
                else:
                    x = self.tree[x].right

            self.tree[z] = Node(parent=y)
            if z < y:
                self.tree[y].left = z
            else:
                self.tree[y].right = z

    def print_nodes(self):
        A = [] # Preorder
        B = [] # Inorder
        def walk_tree(u):
            if u == None:
                return
            r = self.tree[u].right
            l = self.tree[u].left
            A.append(u)
            walk_tree(l)
            B.append(u)
            walk_tree(r)

        walk_tree(self.root)
        print(" ", end="")
        print(*B, sep=" ")
        print(" ", end="")
        print(*A, sep=" ")

    def find(self, k):
        x = self.root
        while x != None and k != x:
            if k < x:
                x = self.tree[x].left
            else:
                x = self.tree[x].right
        return x

    def find_print(self, k):
        if self.find(k) != None:
            print("yes")
        else:
            print("no")

def read_and_print_BSTree(bst, n):
    for _ in range(n):
        cmd = stdin.readline().strip().split()
        if cmd[0] == 'insert':
            bst.insert(int(cmd[1]))
        elif cmd[0] == 'print':
            bst.print_nodes()
        elif cmd[0] == 'find':
            bst.find_print(int(cmd[1]))

n = int(input())
bst = BinarySearchTree()
read_and_print_BSTree(bst, n)
