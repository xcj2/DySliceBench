import sys
from collections import Counter
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
            return True
        else:
            return False


N, M = map(int, readline().split())

AB = [tuple(map(int, readline().split())) for _ in range(N)]
AB.sort()

A, B = map(list, zip(*AB))
Sw = [0]*N
push = 0

for i in range(N):
    Sw[i] = B[i]^push
    push ^= Sw[i]

Code = Counter()
Edge = []
for m in range(M):
    l, r = map(int, readline().split())
    r += 1
    
    ng = -1
    ok = N
    while abs(ok-ng) > 1:
        med = (ok+ng)//2
        if l <= A[med]:
            ok = med
        else:
            ng = med
    
    L = ok
    
    ng = -1
    ok = N
    while abs(ok-ng) > 1:
        med = (ok+ng)//2
        if r <= A[med]:
            ok = med
        else:
            ng = med
    
    R = ok
    if L == R:
        continue
    if L == N or R == 0:
        continue
    if (L, R) in Code:
        continue
    Edge.append((L, R))
    Code[(L, R)] = m+1
    Code[(R, L)] = m+1
    
UE = [[] for _ in range(N+1)]

T = UF(N+1)

for l, r in Edge:
    if T.union(l, r):
        UE[l].append(r)
        UE[r].append(l)

seen = set()
stack = []

for i in range(N, -1, -1):
    ri = T.find(i)
    if ri not in seen:
        stack.append(i)
        seen.add(ri)
        

used = set(stack)
Lord = []
par = [-1]*(N+1)
while stack:
    vn = stack.pop()
    Lord.append(vn)
    for vf in UE[vn]:
        if vf not in used:
            used.add(vf)
            stack.append(vf)
            par[vf] = vn
Col = Sw[:] + [0]
anse = []

for l in Lord[::-1]:
    p = par[l]
    if p == -1:
        continue
    if Col[l]:
        Col[l] = 0
        Col[p] ^= 1
        anse.append(Code[(l, p)])


if any(Col[:-1]):
    print(-1)

else:
    anse.sort()
    print(len(anse))
    print(*anse)