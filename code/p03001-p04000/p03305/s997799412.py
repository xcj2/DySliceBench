from heapq import heappush, heappop
 
 
class Dijk:
    def __init__(self, n):
        self.table = [[] for i in range(n+1)]
        self.n = n+1
 
    def add(self, x, y, f):
        self.table[x].append((y, f))
 
    def di(self, s):
        inf = float('inf')
        self.val = [inf] * self.n
        self.val[s] = 0
        h = []
        heappush(h, (0, s))
        while h:
            q, i = heappop(h)
            if self.val[i] < q:
                continue
            for x, c in self.table[i]:
                if self.val[x] > self.val[i] + c:
                    self.val[x] = self.val[i] + c
                    heappush(h, (self.val[x], x))
 
    def dist(self, s, t):
        return self.val[t]
 
n, m, s, t = map(int, input().split())
en=Dijk(n)
snu=Dijk(n)
for i in range(m):
    a,b,c,d=map(int,input().split())
    en.add(a,b,c)
    en.add(b,a,c)
    snu.add(a,b,d)
    snu.add(b,a,d)
en.di(s)
snu.di(t)

mod=10**15
t=float('inf')
ans=[]
for i in range(n,0,-1):
    t=min(t,en.dist(s,i)+snu.dist(t,i))
    ans.append(mod-t)
for i in ans[::-1]:
    print(i)
