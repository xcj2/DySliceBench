class node:
    def __init__(self, parent, left, right):
        self.parent=parent
        self.left=left
        self.right=right

class tree:

    def __init__(self, datas):
        #format of datas
        #id, left, right
        self.T=[]
        self.rootID=None
        for d in datas:
            self.T.append(node(None,None, None))

        for d in datas:
            if(d[1]!=-1):
                self.T[d[0]].left=d[1]
            if(d[2]!=-1):
                self.T[d[0]].right=d[2]

        for d in datas:

            id=d[0]
            if(self.T[id].left is not None):
                self.T[self.T[id].left].parent = id
            if (self.T[id].right is not None):
                self.T[self.T[id].right].parent = id


        for d in datas:
            if(self.T[d[0]].parent is None):
                self.rootID = d[0]
                #print(rootid)

        self.Preorder = [None for _ in datas]
        self.Inorder =[None for _ in datas]
        self.Postorder=[None for _ in datas]

        self.setPreorder(self.rootID)
        self.setInorder(self.rootID)
        self.setPostorder(self.rootID)

        #print(self.Preorder)
        #print(self.Inorder)
        #print(self.Postorder)


    def setPreorder(self, id):
        if id is None:
            return
        else:
            self.Preorder.append(id)
            self.setPreorder(self.T[id].left)
            self.setPreorder(self.T[id].right)

    def setInorder(self,id):
        if id is None:
            return
        else:
            self.setInorder(self.T[id].left)
            self.Inorder.append(id)
            self.setInorder(self.T[id].right)

    def setPostorder(self,id):
        if id is None:
            return
        else:
            self.setPostorder(self.T[id].left)
            self.setPostorder(self.T[id].right)
            self.Postorder.append(id)

n=int(input())
dlist=[]
for i in range(n):
    dlist.append(list(map(int,(input().split()))))
t=tree(dlist)
print("Preorder")
print(" "+" ".join([str(_) for _ in t.Preorder if _ is not None]))
print("Inorder")
print(" "+" ".join([str(_) for _ in t.Inorder if _ is not None]))
print("Postorder")
print(" "+" ".join([str(_) for _ in t.Postorder if _ is not None]))



