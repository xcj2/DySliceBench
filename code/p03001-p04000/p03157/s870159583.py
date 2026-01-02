from collections import Counter
class uf(object):
    def __init__(self, n=1):
        self.par = [i for i in range(n)]
        self.rank = [0 for _ in range(n)]
    def find(self, x):
        if self.par[x] == x:
            return x
        else:
            self.par[x] = self.find(self.par[x])
            return self.par[x]
    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x != y:
            if self.rank[x] < self.rank[y]:
                x, y = y, x
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1
            self.par[y] = x
    def is_same(self, x, y):
        return self.find(x) == self.find(y)

def alte(h,w,s):
    ufa=uf(h*w)

    for x in range(h):
        for y in range(w):
            if s[x][y]!=s[min(x+1,h-1)][y]:
                ufa.union(x*w+y,x*w+y+w)
            if s[x][y]!=s[x][min(y+1,w-1)]:
                ufa.union(x*w+y,x*w+y+1)

    cnta=Counter()
    cntb=Counter()

    for x in range(h):
        for y in range(w):
            k = x*w+y
            if s[x][y] == '.':
                cnta[ufa.find(k)] += 1
            else:
                cntb[ufa.find(k)] += 1

    cnt=0
    for i in range(h*w):
        cnt+=cnta[i]*cntb[i]

    return cnt

h,w=map(int,input().split())
print(alte(h,w,[input() for i in range(h)]))