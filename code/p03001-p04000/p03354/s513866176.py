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

    def print(self):
        print(self.p)
        
def readinput():
    n,m=list(map(int,input().split()))
    p=list(map(int,input().split()))
    p.insert(0,0)
    pairs=[]
    for _ in range(m):
        pair=list(map(int,input().split()))
        pairs.append(pair)
    return n,m,p,pairs

def main(n,m,p,pairs):
    uft=DisjointSet(n+1)
    for x,y in pairs:
        if uft.same(x, y):
            pass
        else:
            uft.unite(x, y)

    #uft.print()

    #print(p)
    count=0
    for i in range(1,n+1):
        if uft.same(i,p[i]):
            #p[i],p[j] = p[j], p[i]
            count+=1
    
    return count

if __name__=='__main__':
    n,m,p,pairs=readinput()
    ans=main(n,m,p,pairs)
    print(ans)
