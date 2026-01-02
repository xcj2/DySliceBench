from operator import itemgetter

class UnionFindTree:
    def __init__(self,size):
        self.rank=[0]*size
        self.p=[0]*size
        for i in range(size):
            self.makeSet(i)
    
    def makeSet(self,i):
        self.p[i]=i
        self.rank[i]=0
    
    def same(self,x,y):
        return self.findSet(x) == self.findSet(y)
    
    def unite(self, x,y):
        self.link(self.findSet(x), self.findSet(y))
    
    def link(self, x, y):
        if(self.rank[x] > self.rank[y]):
            self.p[y] = x
        else:
            self.p[x] = y
            if self.rank[x] == self.rank[y]:
                self.rank[y]+=1
     
    def findSet(self, x):
        if(x!=self.p[x]):
            self.p[x]=self.findSet(self.p[x])
        return self.p[x]

    def print(self):
        print(self.p)


def readinput():
    nv, ne=list(map(int,input().split()))
    nList=[]
    for _ in range(ne):
        s,t,w=list(map(int,input().split()))
        nList.append((s,t,w))
    return nv,ne,nList

def Kruskal(nv,nList):
    sortedList=sorted(nList, key=itemgetter(2))
    S=UnionFindTree(nv)
    K=[]

    for e in sortedList:
        s=e[0]
        t=e[1]
        if S.same(s,t)==False:
            S.unite(s,t)
            K.append(e)
    
    return K

def main(nv,ne,nList):
    K=Kruskal(nv,nList)
    total=0
    for e in K:
        total+=e[2]
    return total


if __name__=='__main__':
    nv,ne,nList=readinput()
    ans=main(nv,ne,nList)
    print(ans)

