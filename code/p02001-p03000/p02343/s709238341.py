class DisjointSet:
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

def main():
    n,q=list(map(int,input().split()))
    disjointSet = DisjointSet(n)
    for _ in range(q):
        cmds=list(input().split())
        if cmds[0] == '0':
            x,y=list(map(int,cmds[1:]))
            disjointSet.unite(x,y)
        elif cmds[0]=='1':
            x,y=list(map(int,cmds[1:]))
            if disjointSet.same(x,y) == True:
                print(1)
            else:
                print(0)
    
if __name__=='__main__':
    main()

