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
u = UnionFind(N)
for i in range(M):
    a,b = map(int,input().split())
    a -= 1
    b -= 1
    u.union(a,b)

ans = 0
for i in range(N):
    ans = max(ans,u.size(i))

print(ans)