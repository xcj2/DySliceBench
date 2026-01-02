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

    def find(self,data,sw):
        pt = self.root
        flag = 0
        while pt != None:
            if pt.data == data:
                flag = 1
                if sw == 1:
                    print("yes")
                return 1
            elif pt.data > data:
                pt = pt.left
            else:
                pt = pt.right
        if flag == 0:
            if sw == 1:
                print("no")
            return 0

    def delete(self,data):
        if self.find(data,0) == 1:
            pt = self.root
            while pt != None:
                if pt.data == data:
                    break
                elif pt.data > data:
                    pt = pt.left
                else:
                    pt = pt.right
            if pt.left == None and pt.right == None: #子0個
                if pt.data < pt.parent.data:
                    pt.parent.left , pt = None , None
                else:
                    pt.parent.right , pt = None , None
            elif pt.left != None and pt.right == None: #子1個
                if pt.data < pt.parent.data:
                    pt.parent.left , pt.left.parent , pt = pt.left , pt.parent , None
                else:
                    pt.parent.right , pt.left.parent , pt = pt.left , pt.parent , None
            elif pt.left == None and pt.right != None: #子1個
                if pt.data < pt.parent.data:
                    pt.parent.left , pt.right.parent , pt = pt.right , pt.parent , None
                else:
                    pt.parent.right , pt.right.parent , pt = pt.right , pt.parent , None
            else: #子2個
                y = self.getSuccessor(pt) #ptを根とする右部分木のnode.dataの最小値
                pt.data = y.data
                if y.right == None:
                    if y.data < y.parent.data:
                        y.parent.left , y = None , None
                    else:
                        y.parent.right , y = None , None
                else:
                    if y.data < y.parent.data:
                        y.parent.left , y.right.parent , y = y.right , y.parent , None
                    else:
                        y.parent.right , y.right.parent , y = y.right , y.parent , None
    def getSuccessor(self,x): #次節点
        if x.right != None:
            return self.getMinimum(x.right)
        y = x.parent
        while y != None and x == y.right:
            x = y
            y = y.parent
        return y

    def getMinimum(self,x):
        while x.left != None:
            x = x.left
        return x

    def print(self):
        print(""," ".join(map(str,self.root.inorder([])))) #なぜかjoinを使ったら速くなった
        print(""," ".join(map(str,self.root.preorder([]))))

btree = BTree()
cnt = 0
for i in range(n):
    if COM[i][0] == "insert":
        node = Node(int(COM[i][1]))
        btree.insert(node)
        cnt += 1
    elif COM[i][0] == "find":
        btree.find(int(COM[i][1]),1)
    elif COM[i][0] == "delete":
        btree.delete(int(COM[i][1]))
    else:
        btree.print()

