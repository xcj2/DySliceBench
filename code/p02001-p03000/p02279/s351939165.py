#left child right siberings representation
#left : index of the most left children
#right : index of the nearest right siberings


class node:
    def __init__(self,parent, left, right):
        self.parent=parent
        self.left=left
        self.right=right


class tree:
    #give some list to define the tree structure
    def __init__(self, list):
        #root initialization
        self.root=None
        self.T=[]
        self.insert(list)

    #parse data to tree structure
    def insert(self,list):
        nnodes=len(list)
        for i in range(nnodes):
            self.T.append(node(None, None, None))
        for i in range(nnodes):
            #n=node index
            n=int(list[i][0])
            nch=list[i][1]
            for j in range(nch):
                chnode=list[i][2+j]
                #set the parent in the each child node
                self.T[chnode].parent=n
                if (j==0):
                    #most left children
                    self.T[n].left=chnode

                #define the nearest right siberings in the child node
                if (j < nch-1):
                    self.T[chnode].right=list[i][j+3]

    def getDepth(self, index):
        d=0
        u=index
        while self.T[u].parent !=None:
            u=self.T[u].parent
            d=d+1

        return d

    def getChildrens(self, index):
        ch=[]
        c=self.T[index].left
        ic=c
        while ic!=None:
            ch.append(ic)
            ic=self.T[ic].right

        return ch

    def printNode(self, index):
        print("parent="+str(self.T[index].parent)+",depth="+str(self.getDepth(index)) +\
              ",right="+str(self.T[index].right)+ ",left="+str(self.T[index].left))
        print(self.getChildrens(index))
        return

    def stringForAOJ(self,index):
        #node index
        strs=""
        strs=strs+"node "+str(index)+":"

        #parent
        if self.T[index].parent==None:
            strs=strs+" parent = -1,"
        else:
            strs = strs + " parent = "+str(self.T[index].parent)+","

        #depth
        strs=strs+" depth = "+str(self.getDepth(index))+","

        #type
        if self.T[index].parent==None:
            strs=strs+" root,"
        elif self.T[index].left==None:
            strs = strs + " leaf,"
        else:
            strs = strs + " internal node,"

        #childrens
        strs=strs+" ["
        ch=self.getChildrens(index)
        for i in range(len(ch)):
            strs=strs+str(ch[i])
            if (i < len(ch)-1):
                strs=strs+", "

        strs=strs+"]"

        return strs





n=int(input())
dlist=[]
for i in range(n):
    dlist.append(list(map(int,(input().split()))))

#print(dlist)
t=tree(dlist)

for i in range(n):
    print(t.stringForAOJ(i))



