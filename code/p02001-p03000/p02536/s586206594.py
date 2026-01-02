#dt = {} for i in x: dt[i] = dt.get(i,0)+1
import sys;input = sys.stdin.readline
#import io,os; input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline #for pypy
inp,ip = lambda :int(input()),lambda :[int(w) for w in input().split()]

class DisjSet: 
    def __init__(self,n): 
        self.rank = [1]*n 
        self.parent = [i for i in range(n)] 

    def find(self,x): 
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x]) 
        return self.parent[x]

    def Union(self,x,y):
        xset = self.find(x) 
        yset = self.find(y)
        if xset == yset: return

        if self.rank[xset] < self.rank[yset]: 
            self.parent[xset] = yset 
        elif self.rank[xset] > self.rank[yset]: 
            self.parent[yset] = xset 
        else: 
            self.parent[yset] = xset 
            self.rank[xset] += 1

n,m = ip()
obj = DisjSet(n)
for i in range(m):
    a,b = ip()
    obj.Union(a-1,b-1)
dt = {}
for i in range(n):
    p = obj.find(i)
    dt[p] = dt.get(p,0)+1
print(len(dt.keys())-1)
    
