import sys
readline = sys.stdin.readline

class UF():
    def __init__(self, num):
        self.par = [-1]*num
    def find(self, x):
        if self.par[x] < 0:
            return x
        else:
            stack = []
            while self.par[x] >= 0:
                stack.append(x)
                x = self.par[x]
            for xi in stack:
                self.par[xi] = x
            return x
    
    def union(self, x, y):
        rx = self.find(x)
        ry = self.find(y)
        if rx != ry:
            if self.par[rx] > self.par[ry]:
                rx, ry = ry, rx
            self.par[rx] += self.par[ry]
            self.par[ry] = rx
        return rx

N, M = map(int, readline().split())
T = UF(N)
for _ in range(M):
    a, b = map(int, readline().split())
    a -= 1
    b -= 1
    T.union(a, b)

print(-min(T.par))