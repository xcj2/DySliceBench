class UnionFind:
    def __init__(self, num):
        self.table = [-1 for _ in range(num)]

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
            if self.table[s1] <= self.table[s2]:
                self.table[s1] += self.table[s2]
                self.table[s2] = s1
            else:
                self.table[s2] += self.table[s1]
                self.table[s1] = s2
            return True
        return False
from collections import defaultdict

N = int(input())
u = UnionFind(N)
xy = [list(map(int,input().split())) for _ in range(N)]
x_d = defaultdict(lambda:[])
y_d = defaultdict(lambda:[])
for i in range(N):
    x,y = xy[i]
    x_d[x].append(i)
    y_d[y].append(i)
for x in x_d:
    j = x_d[x][0]
    for i in x_d[x]:
        u.union(i,j)
for y in y_d:
    j = y_d[y][0]
    for i in y_d[y]:
        u.union(i,j)

d = defaultdict(lambda:[])
for i in range(N):
    d[u.find(i)].append(i)

ans = 0
for f in d:
    x_l = []
    y_l = []
    for i in d[f]:
        x,y = xy[i]
        x_l.append(x)
        y_l.append(y)
    x_s = set(x_l)
    y_s = set(y_l)
    ans += len(x_s)*len(y_s)-len(d[f])

print(ans)