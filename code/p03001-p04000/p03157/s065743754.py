def I(): return int(input())
def MI(): return map(int, input().split())
def SI(): return input().rstrip()
from collections import defaultdict

#https://note.nkmk.me/python-union-find/

class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        return -self.parents[self.find(x)]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        return {r: self.members(r) for r in self.roots()}

    def __str__(self):
        return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())

h,w=MI()
uf=UnionFind(h*w)
lis=[[0]*w for i in range(h)]
for i in range(h):
    s=SI()
    for j in range(w):
        if s[j]=="#":
            lis[i][j]=1
step=[[0,1],[0,-1],[-1,0],[1,0]]
for i in range(h):
    for j in range(w):
        for x,y in step:
            if not (0<=i+x<h and 0<=j+y<w):
                continue
            if lis[i][j]!=lis[i+x][j+y]:
                uf.union(w*i+j,w*(i+x)+(j+y))
ans=0
dic=defaultdict(lambda:[0,0])
for i in range(h):
    for j in range(w):
        dic[uf.find(w*i+j)][lis[i][j]==1]+=1
for p in dic.keys():
    ans+=dic[p][0]*dic[p][1]
print(ans)

            
            
                
                
    
        
    
            
            










            
            
                
                
    
        
    
            
            

