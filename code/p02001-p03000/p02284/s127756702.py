# coding: utf-8

class Node:
    def __init__(self, me, left, right):
        self.me = me
        self.left = left
        self.right = right
        self.parent = None

class NodeTree:
    def __init__(self, root=None):
        self.root = root
        
    def insert(self,z):
        y = None
        x = self.root
        while x != None:
            y = x
            if z.me < x.me:
                x = x.left
            else:
                x = x.right
        z.parent = y
        
        if y == None:
            self.root = z
        elif z.me < y.me:
            y.left = z
        else:
            y.right = z

    def find(self, z):
        y = None
        x = self.root
        while True:
            if x.me == z.me:
                return True
            elif x.me > z.me:
                if x.left != None:
                    x = x.left
                else:
                    return False
            else:
                if x.right != None:
                    x = x.right
                else:
                    return False
            
    
    def getPreorder(self, node, ans):
        ans.append(node)
        if node.left != None:
            self.getPreorder(node.left, ans)
        if node.right != None:
            self.getPreorder(node.right, ans)
            
    def getInorder(self, node, ans):
        if node.left != None:
            self.getInorder(node.left, ans)
        ans.append(node)
        if node.right != None:
            self.getInorder(node.right, ans)

        
def printAns(ans):
    for a in ans:
        print(" " + str(a.me),end="")
    print()
    
m = int(input().rstrip())
nt = NodeTree()
for i in range(m):
    line = input().rstrip().split()
    if line[0] == "insert":
        nt.insert(Node(int(line[1]),None,None))
    elif line[0] == "find":
        if nt.find(Node(int(line[1]),None,None)):
            print("yes")
        else:
            print("no")
    else:
        ans = []
        nt.getInorder(nt.root,ans)
        printAns(ans)
        ans = []
        nt.getPreorder(nt.root,ans)
        printAns(ans)
