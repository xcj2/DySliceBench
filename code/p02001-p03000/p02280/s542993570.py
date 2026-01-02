class node:
    def __init__(self,parent, left, right):
        self.parent=parent
        self.left=left
        self.right=right

class binaryTree:

    def __init__(self, datas):
        #format of datas
        #id, left, right
        self.T=[]
        for d in datas:
            self.T.append(node(-1, -1, -1))

        for d in datas:
            self.T[d[0]].left=d[1]
            self.T[d[0]].right=d[2]

        for d in datas:

            id=d[0]
            if(self.T[id].left != -1):
                self.T[self.T[id].left].parent = id
            if (self.T[id].right != -1):
                self.T[self.T[id].right].parent = id

        rootid=-1
        for d in datas:
            if(self.T[d[0]].parent == -1):
                rootid = d[0]
                #print(rootid)

        self.Depth=[-1 for _ in range(len(datas))]
        self.Height=[-1 for _ in range(len(datas))]

        self.setDepth(rootid,0)

        for i in range(len(datas)):
            self.setHeight(i)


    def setDepth(self,id,depth):
        if(id!=-1):
            self.Depth[id]=depth
            self.setDepth(self.T[id].left, depth+1)
            self.setDepth(self.T[id].right, depth + 1)
            return
        return

    def setHeight(self, id):
        h1=0
        h2=0

        if(self.T[id].left != -1):
            h1=self.setHeight(self.T[id].left)+1
        if(self.T[id].right !=-1):
            h2=self.setHeight(self.T[id].right)+1
        self.Height[id]=max(h1,h2)
        return max(h1,h2)

    def getSibring(self,id):
        p=self.T[id].parent
        right=-1
        left=-1

        if(p!=-1):
            right=int(self.T[p].right)
        if(p!=-1):
            left=int(self.T[p].left)

        #print("id="+str(id)+"r="+ str(right) +" l="+str(left))

        if(p == -1):
            return -1
        elif id != left and left != -1 :
            return left
        elif id != right and right != -1 :
            return right
        else:
            return -1


    def printNode(self,id):
        p=self.T[id].parent
        r=self.T[id].right
        l=self.T[id].left

        strs=""
        strs = strs+"node "+ str(id)+":"

        if(p==-1):
            strs=strs+" parent = -1"
        else:
            strs = strs + " parent = " + str(self.T[id].parent)
        strs=strs+", sibling = "+str(self.getSibring(id))

        deg=0
        if(r!=-1):
            deg=deg+1
        if(l!=-1):
            deg=deg+1
        strs=strs+", degree = "+str(deg)
        strs=strs+", depth = "+str(self.Depth[id])
        strs=strs+", height = "+str(self.Height[id])

        if(self.T[id].parent == -1):
            strs=strs+", root"
        elif(self.T[id].right == -1 and self.T[id].left == -1):
            strs=strs+", leaf"
        else:
            strs=strs+", internal node"

        return strs

n=int(input())
dlist=[]
for i in range(n):
    dlist.append(list(map(int,(input().split()))))
t=binaryTree(dlist)
for i in range(n):
    print(t.printNode(i))


















