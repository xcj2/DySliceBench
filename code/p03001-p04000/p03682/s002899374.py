import sys
sys.setrecursionlimit(10**8)
def ii(): return int(sys.stdin.readline())
def mi(): return map(int, sys.stdin.readline().split())
def li(): return list(map(int, sys.stdin.readline().split()))
def li2(N): return [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
def dp2(ini, i, j): return [[ini]*i for _ in range(j)]
def dp3(ini, i, j, k): return [[[ini]*i for _ in range(j)] for _ in range(k)]
#import bisect #bisect.bisect_left(B, a)
#from collections import defaultdict #d = defaultdict(int) d[key] += value
#from itertools import accumulate #list(accumulate(A))

class UnionFind:
    def __init__(self, n):
        self.d = [-1]*n
    
    def find(self, x):
        if self.d[x] < 0:
            return x
        else:
            self.d[x] = self.find(self.d[x])
            return self.find(self.d[x])
    
    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x==y:
            return False
        if self.d[x] > self.d[y]:
            x, y = y, x
        self.d[x] += self.d[y]
        self.d[y] = x
        return True
    
    def same(self, x, y):
        if self.find(x)==self.find(y):
            return True
        return False
    
    def size(self, x):
        return (-1) * self.d[self.find(x)]

N = ii()

l_x = []
l_y = []
for i in range(N):
    x, y = mi()
    l_x.append([i, x])
    l_y.append([i, y])
l_x.sort(key=lambda x:x[1])
l_y.sort(key=lambda x:x[1])

path = []
for i in range(N-1):
    path.append([l_x[i][0], l_x[i+1][0], l_x[i+1][1]-l_x[i][1]])
    path.append([l_y[i][0], l_y[i+1][0], l_y[i+1][1]-l_y[i][1]])
path.sort(key=lambda x:x[2])

T = UnionFind(N)
cnt = 0
for i in range(2*N-2):
    s, t, d = path[i][0], path[i][1], path[i][2]
    if not T.same(s, t):
        T.unite(s, t)
        cnt += d

print(cnt)