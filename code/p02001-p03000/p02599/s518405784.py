import sys
input = sys.stdin.readline
# Binary Indexed Tree (Fenwick Tree)
class BIT:
    def __init__(self, n):
        self.n = n
        self.data = [0]*(n+1)
        self.el = [0]*(n+1)
    def sum(self, i):
        s = 0
        while i > 0:
            s += self.data[i]
            i -= i & -i
        return s
    def add(self, i, x):
        # assert i > 0
        self.el[i] += x
        while i <= self.n:
            self.data[i] += x
            i += i & -i
    def get(self, i, j=None):
        if j is None:
            return self.el[i]
        return self.sum(j) - self.sum(i)

n,q=map(int,input().split())
c=list(map(int,input().split()))
ques=[]
from collections import defaultdict
ans=defaultdict(int)
for _ in range(q):
    l,r=map(int,input().split())
    ques.append((l,r))

sortques=sorted(ques, key=lambda x:x[1])

good=BIT(n+1)
goodind=[-1]*n
last=0
for x in range(q):
    l,r=sortques[x]
    if last!=r:
        for i in range(last, r):
            if goodind[c[i]-1]==-1:
                goodind[c[i]-1]=i
                good.add(i+1, 1)
            else:
                j=goodind[c[i]-1]
                good.add(j+1, -1)
                goodind[c[i]-1]=i
                good.add(i+1, 1)
    ans[(l,r)]=good.get(l-1,r)
    last=r

for i in range(q):
    print(ans[ques[i]])