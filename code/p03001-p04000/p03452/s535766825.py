import sys
readline = sys.stdin.readline
class UFP():
    def __init__(self, num):
        self.par = [-1]*num
        self.dist = [0]*num
    def find(self, x):
        if self.par[x] < 0:
            return x
        else:
            res = 0
            xo = x
            while self.par[x] >= 0:
                res += self.dist[x]
                x = self.par[x]
            self.dist[xo] = res
            self.par[xo] = x
            return x
    
    def union(self, x, y, d):
        rx = self.find(x)
        ry = self.find(y)
        if rx != ry:
            if self.par[rx] > self.par[ry]:
                rx, ry = ry, rx
                x, y = y, x
                d = -d
            self.par[rx] += self.par[ry]
            self.par[ry] = rx
            self.dist[ry] = d + self.dist[x] - self.dist[y]
            return True
        else:
            if d + self.dist[x] - self.dist[y]:
                return False
            return True

N, M = map(int, readline().split())
T = UFP(N)
ans = 'No'
for _ in range(M):
    l, r, d = map(int, readline().split())
    l -= 1
    r -= 1
    if not T.union(l, r, d):
        break
else:
    ans = 'Yes'
print(ans)
