import sys
readline = sys.stdin.readline

class UF():
    def __init__(self, num):
        self.par = [-1]*num
        self.comp = [False]*num
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
            if self.comp[rx] and self.comp[ry]:
                return False
            if self.par[rx] > self.par[ry]:
                rx, ry = ry, rx
            self.comp[rx] |= self.comp[ry]
            self.par[rx] += self.par[ry]
            self.par[ry] = rx
            return True
        elif not self.comp[rx]:
            self.comp[rx] = True
            return True
        return False


N, H, W = map(int, readline().split())

geta = 10**5

Edge = []
for _ in range(N):
    h, w, a = map(int, readline().split())
    h -= 1
    w -= 1
    Edge.append((a, h, geta+w))

Edge.sort(reverse = True)

T = UF(2*geta)

ans = 0
for cost, a, b in Edge:
    if T.union(a, b):
        ans += cost
print(ans)
