import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


class BIT():
    def __init__(self, n, x=1):
        self.n = n
        self.T = [0]*(n+1)

    def add(self, i, x):
        i += 1
        while i <= self.n:
            self.T[i] += x
            i += i & -i

    def sum(self, i):
        i += 1
        ret = 0
        while i > 0:
            ret += self.T[i]
            i -= i & -i
        return ret

    def sump(self, l, r):
        return self.sum(r-1)-self.sum(l-1)


N = int(input())

C = [[] for _ in [0]*N]
for i, c in enumerate(map(int, input().split())):
    C[c-1].append(i)

G = [[] for _ in [0]*N]
for _ in [0]*(N-1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    G[a].append(b)
    G[b].append(a)


pin = [-1]*N
pout = [-1]*N
k = 0


def dfs(v=0, p=-1):
    global k
    pin[v] = k
    k += 1
    for u in G[v]:
        if u == p:
            continue
        dfs(u, v)
    pout[v] = k


def f(x):
    return x*(x+1)//2


dfs()

b = BIT(N)
for i in range(N):
    b.add(i, 1)


total = f(N)
for c in C:
    c.sort(key=lambda x: pin[x], reverse=True)
    history = []
    ans = total
    for v in c:

        sub = 1
        for u in G[v]:
            if pin[u] < pin[v]:
                continue
            num = b.sump(pin[u], pout[u])
            ans -= f(num)
            sub += num

        b.add(pin[v], -sub)
        history.append((pin[v], sub))

    ans -= f(b.sump(0, N))
    for h in history:
        b.add(*h)
    print(ans)
