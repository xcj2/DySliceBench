from collections import Counter,defaultdict,deque
from heapq import heappop,heappush,heapify
import sys,bisect,math,itertools,fractions,pprint
sys.setrecursionlimit(10**8)
mod = 10**9+7
mod2 = 998244353
INF = float('inf')
def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))
def inpln(n): return list(int(sys.stdin.readline()) for i in range(n))


h,w = inpl()
s = [input() for i in range(h)]
d = dict()
ld = dict()
i = 0
dx = [-1,0,1,0]
dy = [0,1,0,-1]
class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    #根を返す
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

#初期化
uf = UnionFind(h*w)
for y in range(h):
    for x in range(w):
        if s[y][x] == '.':
            d[(y,x)] = i
            i += 1
for y in range(h):
    for x in range(w):
        if s[y][x] == '.':
            continue
        l = []
        for dir in range(4):
            nx = x+dx[dir]; ny = y+dy[dir]
            if nx<0 or nx>=w or ny<0 or ny>=h:
                continue
            if s[ny][nx] == '#':
                continue
            if l == []:
                ld[(y,x)] = d[(ny,nx)]
            l.append(d[(ny,nx)])            
            uf.union(l[0],d[(ny,nx)])

# print(ld)
res = 0
for key,value in ld.items():
    res += uf.size(value)
print(res)