from collections import defaultdict
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

N = int(input())
dx = defaultdict(list)
dy = defaultdict(list)
xy = []

for i in range(N):
    x,y = map(int,input().split())
    dx[x].append(i)
    dy[y].append(i)
    xy.append([x,y])

u = UnionFind(N)

for x in dx:
    i = dx[x][0]
    for j in dx[x]:
        u.union(i,j)

for y in dy:
    i = dy[y][0]
    for j in dy[y]:
        u.union(i,j)

dx = defaultdict(list)
dy = defaultdict(list)

for i in range(N):
    dx[u.find(i)].append(xy[i][0])
    dy[u.find(i)].append(xy[i][1])

ans = -N
for i in dx:
    ans += len(set(dx[i]))*len(set(dy[i]))

print(ans)