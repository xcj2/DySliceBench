class Node:
    def __init__(self,left,right):
        self.parent = None
        self.left = left
        self.right = right
    
    def __repr__(self):
        return str(self.parent) + ' ' + str(self.left) + ' ' + str(self.right)

class Tree:
    def __init__(self,n):
        self.T = [Node(None,None) for i in range(n)]
    
    def insert(self,key,left,right):
        self.T[key].left = left
        self.T[key].right = right
        if right != -1:
            self.T[right].parent = key
        if left != -1:
            self.T[left].parent = key
    
    def beforePrint(self):
        self.root = None
        for i in range(len(self.T)):
            if self.T[i].parent == None:
                self.root = i
                break
        return self.root

    def printAll(self):
        #print(self.T)
        root = self.beforePrint()
        #print(root)
        print("Preorder")
        self.printPreOrder(root)
        print()
        print("Inorder")
        self.printInOrder(root)
        print()
        print("Postorder")
        self.printPostOrder(root)
        print()

    
    def printPreOrder(self,key):
        if key == None or key == -1:
            return
        print('',key,end='')
        self.printPreOrder(self.T[key].left)
        self.printPreOrder(self.T[key].right)
    
    def printInOrder(self,key):
        if key == None or key == -1:
            return
        self.printInOrder(self.T[key].left)
        print('',key,end='')
        self.printInOrder(self.T[key].right)
    
    def printPostOrder(self,key):
        if key == None or key == -1:
            return
        self.printPostOrder(self.T[key].left)
        self.printPostOrder(self.T[key].right)
        print('',key,end='')

    


N = int(input())
T = Tree(N)
for i in range(N):
    Q = list(map(int,input().split()))
    T.insert(Q[0], Q[1], Q[2])
T.printAll()




