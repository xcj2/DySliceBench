class Node:
    def __init__(self, parent, lchild, sibling):
        self.parent = parent
        self.lchild = lchild
        self.sibling = sibling
        self.depth = None

    def __repr__(self):
        return "{" + str(self.parent) + " " + str(self.lchild) + " " + str(self.sibling) + "}"

class NodeList:
    def __init__(self,size):
        self.nlist = [Node(None,None,None) for i in range(size)]

    def add(self, id, sibs):
        #print(self)
        self.nlist[id].lchild = sibs[0]
        #print(self)
        for i in range(len(sibs)-1):
            self.nlist[sibs[i]].parent = id
            self.nlist[sibs[i]].sibling = sibs[i+1]
            #print(self)
        self.nlist[sibs[-1]].parent = id

    def calcDepth(self, idx):
        cnt = -1
        while  idx != None:
            #print("depth",self.nlist[idx])
            idx = self.nlist[idx].parent
            cnt += 1
        return cnt

    def getChilds(self, lchild):
        res = []
        while lchild != None:
            #print("childs",self.nlist[lchild])
            res.append(lchild)
            lchild = self.nlist[lchild].sibling
        return res

    def calcStatus(self, node):
        if node.parent == None:
            return "root"
        if node.lchild == None:
            return "leaf"
        return "internal node"

    def print(self):
        for idx, node in enumerate(self.nlist):
            parent = node.parent
            if parent == None:
                parent = -1
            depth = self.calcDepth(idx)
            childs = self.getChilds(node.lchild)
            status = self.calcStatus(node)
            print("node "+str(idx)+": parent = "+str(parent)+", depth = "+str(depth)+", "+str(status)+", "+str(childs))


    def __repr__(self):
        return str(self.nlist)

            


N = int(input())
NL = NodeList(N)

for i in range(N):
    D = list(map(int, input().split()))
    if len(D) is not 2:
        NL.add(D[0], D[2:])
NL.print()
    





