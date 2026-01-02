from collections import defaultdict
class UnionFind:
    def __init__(self, num):
        self.table = [-1 for _ in range(num)]
        self.sz = defaultdict(lambda:1)

    def find(self, x):
        if self.table[x] < 0:
            return x
        else:
            self.table[x] = self.find(self.table[x])
            return self.table[x]

    def union(self, x, y):
        s1 = self.find(x)
        s2 = self.find(y)

        if s1 != s2:
            size = self.sz[s1]+self.sz[s2]
            if self.table[s1] <= self.table[s2]:
                self.table[s1] += self.table[s2]
                self.table[s2] = s1
            else:
                self.table[s2] += self.table[s1]
                self.table[s1] = s2
            s = self.find(x)
            self.sz[s] = size
            return True
        return False

    def size(self, x):
        s = self.find(x)
        return self.sz[s]
N,M = map(int,input().split())
AB = [tuple(map(lambda x:int(x)-1,input().split())) for i in range(M)]
ans = N*(N-1)//2
l = []
u = UnionFind(N)
for i in range(M-1,-1,-1):
    l.append(ans)
    a,b = AB[i]
    if u.find(a)!=u.find(b):
        ans -= u.size(a)*u.size(b)
        u.union(a,b)
for i in range(M-1,-1,-1):
    print(l[i])
