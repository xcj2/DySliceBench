num = int(input())
NIL = -1
MAX = 10000

class Node():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BST():
    def __init__(self):
        self.root = None
        self.In = []
        self.Pr = []
    
    def insert(self, data):
        n = self.root
        if n == None:
            self.root = Node(data)
            return 
        else:
            while True:
                entry = n.data
                if data < entry:
                    if n.left == None:
                        n.left = Node(data)
                        return
                    n = n.left
                elif data > entry:
                    if n.right == None:
                        n.right = Node(data)
                        return
                    n = n.right
                else:
                    n.data =data
                    return
                
    def inorder(self, node):
        if node != None:
            self.inorder(node.left)
            self.In.append(node.data)
            self.inorder(node.right)
        return self
    
    def preorder(self, node):
        if node != None:
            self.Pr.append(node.data)
            self.preorder(node.left)
            self.preorder(node.right)
        return self

a = BST()
for i in range(num):
    order = input().split()
    
    if order[0] == 'print':
        a.In = []
        a.Pr = []
        a.inorder(a.root)
        In = [str(j) for j in a.In]
        a.preorder(a.root)
        Pr = [str(j)  for j in a.Pr]
        print(' ' + ' '.join(In))
        print(' ' + ' '.join(Pr))
    else:
        order[1] = int(order[1])
        if i == 0:
            root = order[1]
        a.insert(order[1])
