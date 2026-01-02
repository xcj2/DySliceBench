class HeapNode():
    def __init__(self):
        self.id = None
        self.key = None
        self.left = None
        self.right = None
        self.parent = None
    
    def show(self):
        print("node {0}: key = {1}, ".format(self.id,self.key), end="")
        if self.parent:
            print("parent key = {}, ".format(self.parent.key), end="")
        if self.left:
            print("left key = {}, ".format(self.left.key), end="")
        if self.right:
            print("right key = {}, ".format(self.right.key), end="")
        print("")

class HeapTree():
    def __init__(self, n):
        self.root = None
        self.n = n + 1
        self.T = [None] * (2 * n + 2)

    def insert(self, x):
        for i in range(len(x)):
            Node = HeapNode()
            if self.root is None:
                self.root = Node
            Node.id = i + 1
            Node.key = x[i]
            self.T[i+1] = Node
            
    def setPLR(self):
        for i in range(1, self.n):
            Node = self.T[i]
            Node.left = self.T[i * 2]
            Node.right = self.T[i * 2 + 1]
            Node.parent = self.T[i // 2]

    def TreePrint(self):
        for i in self.T[1 : self.n]:
            i.show()

n = int(input())
L = list(map(int, input().split()))
Tree = HeapTree(n)
Tree.insert(L)
Tree.setPLR()
Tree.TreePrint()