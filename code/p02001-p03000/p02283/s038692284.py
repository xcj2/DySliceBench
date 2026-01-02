NIL = -1
class Node():
    def __init__(self, val):
        self.val = val
        self.parent = NIL
        self.left = NIL
        self.right = NIL
    def __str__(self):
        return "val:{}, parent:{}, left:{}, right:{}".format(self.val, self.parent, self.left, self.right)
        
class Tree():
    def __init__(self):
        self.Nodes = {}
        self.Nodes[NIL] = Node(NIL)
        self.root = self.Nodes[NIL]
        
    def insert(self, node):
        y = self.Nodes[NIL]
        x = self.root
        while x.val != NIL:
            y = x
            if(node.val < x.val):
                x = self.Nodes[x.left]
            else:
                x = self.Nodes[x.right]
        node.parent = y.val
        
        if(y.val == NIL):
            self.root = node
        elif(node.val < y.val):
            y.left = node.val
        else:
            y.right = node.val
        self.Nodes[node.val] = node

    def getPreOrder(self):
        return self.preParse(self.root.val, [])    
        
    def getInOrder(self):
        return self.inParse(self.root.val, [])
    
    def getPostOrder(self):
        return self.postParse(self.root.val, [])
        
    def inParse(self, u, res):
        if(u == NIL):
            return
        self.inParse(self.Nodes[u].left, res)
        res += [u]
        self.inParse(self.Nodes[u].right, res)
        return res

    def postParse(self, u, res):
        if(u == NIL):
            return
        self.postParse(self.Nodes[u].left, res)
        self.postParse(self.Nodes[u].right, res)
        res += [u]
        return res
    
    def preParse(self, u, res):
        if(u == NIL):
            return 
        res += [u]
        self.preParse(self.Nodes[u].left, res)
        self.preParse(self.Nodes[u].right, res)
        return res
        
n = int(input())

tree = Tree()
for row in range(n):
    operate = input().split()
    if(operate[0] == "insert"):
        tree.insert(Node(int(operate[1])))
        
    if(operate[0] == "print"):
        print(" {}".format( " ".join([str(ss) for ss in tree.getInOrder()])))
        print(" {}".format( " ".join([str(ss) for ss in tree.getPreOrder()])))
