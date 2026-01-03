from collections import defaultdict
class myUnionFind():
    def __init__(self,size):
        self.table = [-1 for i in range(size)]

    def find(self,x):
        if self.table[x]<0:
            return x
        self.table[x] = self.find(self.table[x])
        return self.table[x]

    def is_same(self,x,y):
        return self.table[x]==self.table[y]

    def union(self,x,y):
        x,y = self.find(x),self.find(y)
        if x != y:
            if self.table[x] > self.table[y]:
                y,x = x,y
            self.table[x] += self.table[y]
            self.table[y] = x
        return x!=y

N,K,L = map(int,input().split())
R,T = myUnionFind(N),myUnionFind(N)
for i in range(K):
    p,q = map(int,input().split())
    R.union(p-1,q-1)
for i in range(L):
    r,s = map(int,input().split())
    T.union(r-1,s-1)
both = defaultdict(int)
for i in range(N):
    both[(R.find(i),T.find(i))] += 1
ans = [both[(R.find(i),T.find(i))] for i in range(N)]
print(*ans)
