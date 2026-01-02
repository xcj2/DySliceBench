#time limit exceed
n = int(input())
COM = [list(input().split()) for _ in range(n)]

class Node:
    def __init__(self,data):
        self.data = data #int
        self.left = None #Node
        self.right = None #Node
        self.parent = None #Node

    def inorder(self,List):
        if self.data != None:
            if self.left != None:
                self.left.inorder(List)
            List.append(self.data)
            if self.right != None:
                self.right.inorder(List)
        return List

    def preorder(self,List):
        if self.data != None:
            List.append(self.data)
            if self.left != None:
                self.left.preorder(List)
            if self.right != None:
                self.right.preorder(List)
        return List

class BTree:
    def __init__(self):
        self.root = None

    def insert(self,z):
        y = None
        x = self.root
        while x != None:
            y = x
            if z.data < x.data:
                x = x.left
            else:
                x = x.right
        z.parent = y
        if y == None:
            self.root = z
        elif z.data < y.data:
            y.left = z
        else:
            y.right = z

    def print(self):
        print(""," ".join(map(str,self.root.inorder([]))))
        print(""," ".join(map(str,self.root.preorder([]))))

btree = BTree()
cnt = 0
for i in range(n):
    if COM[i][0] == "insert":
        node = Node(int(COM[i][1]))
        btree.insert(node)
        cnt += 1
    else:
        btree.print()

