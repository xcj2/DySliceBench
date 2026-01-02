from heapq import heappush, heappop


class Dijk:
    def __init__(self, n):
        self.table = [[] for i in range(n)]
        self.n = n

    def add(self, x, y, f):
        self.table[x].append((y, f))

    def di(self, s):
        inf = 10 ** 20
        self.val = [inf] * self.n
        self.val[s] = 0
        h = []
        heappush(h, (0, s))
        while h:
            q, i = heappop(h)
            if self.val[i] < q:
                continue
            for x, c in self.table[i]:
                if self.val[x] > self.val[i] + c:
                    self.val[x] = self.val[i] + c
                    heappush(h, (self.val[x], x))

    def dist(self, s, t):
        return self.val[t]


N, M, s, t = map(int, input().split())
stra = Dijk(N)
rstra = Dijk(N)
for i in range(M):
    u, v, a, b = map(int, input().split())
    stra.add(u - 1, v - 1, a)
    stra.add(v - 1, u - 1, a)
    rstra.add(u - 1, v - 1, b)
    rstra.add(v - 1, u - 1, b)
stra.di(s - 1)
rstra.di(t - 1)
ans = []
T = 10 ** 15
mod = 10 ** 15
for i in range(N - 1, -1, -1):
    T = min(stra.dist(s - 1, i) + rstra.dist(t - 1, i), T)
    ans.append(mod - T)
print('\n'.join(map(str, ans[::-1])))