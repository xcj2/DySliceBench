#BinarySearchTree
class TreeNode():
    def __init__(self):
        self.key = None
        self.parent = None
        self.left = None
        self.right = None
    def inoder(self):
        r=[]
        if self.left:
            r += self.left.inoder()
        r += [self.key]
        if self.right:
            r += self.right.inoder()
        return r
 
    def preoder(self):
        r = [self.key]
        if self.left:
            r += self.left.preoder()
        if self.right:
            r += self.right.preoder()
        return r
 
class BinaryTree():
    def __init__(self):
        self.root = None
 
    def insert(self, z):
        y = None
        x = self.root
        while x != None:
            y = x
            if z.key < x.key:
                x = x.left
            else:
                x = x.right
        z.parent = y
        if y == None:
            self.root = z
        elif z.key < y.key:
            y.left = z
        else:
            y.right = z
 
    def show(self):
        x = self.root
        print(" " + " ".join(map(str, self.root.inoder())))
        print(" " + " ".join(map(str, self.root.preoder())))
 
    def find(self, key):
        currentNode = self.root
        while currentNode:
            if key == currentNode.key:
                return currentNode
            else:
                if key < currentNode.key:
                    currentNode = currentNode.left
                else:
                    currentNode = currentNode.right
        return False
    def next(self, key):
        return self.min(key.right)
    def min (self, key):
        while key.left is not None:
           key = key.left
        return key
     
    def delete(self, key):
        z = self.find(key)
        if z == False: return
        if z.left and z.right:
            y = self.next(z)
        else:
            y = z
            if z == self.root:
                self.root = None
         
        if z.left:
            x = y.left
        else:
            x = y.right

        if x:
            x.parent = y.parent
        if y.parent is None:
            self.root = x
        elif y == y.parent.left:
            y.parent.left = x
        else:
            y.parent.right = x
        if y != z:
            z.key = y.key

n = int(input())
Tree = BinaryTree()
for i in range(n):
    L = input().split()
    if L[0] == "insert":
        Node = TreeNode()
        Node.key = int(L[1])
        Tree.insert(Node)
    if L[0] =="print":
        Tree.show()
    if L[0] =="find":
        if Tree.find(int(L[1])) == False:
            print("no")
        else:
            print("yes")
    if L[0] =="delete":
        Tree.delete(int(L[1]))