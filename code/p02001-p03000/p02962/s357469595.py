from collections import deque
def gcd(m, n):
    r = m % n
    return gcd(n, r) if r else n
s = input()
t = input()
class RollingHash:
    def __init__(self, s, base, MOD):
        self.s = s
        self.l = l = len(s)
        self.base = base
        self.MOD = MOD
        self.h = h = [0]*(l + 1)
        for i in range(l):
            h[i+1] = (h[i] * base + ord(s[i])) % MOD
    def get(self, l, r):
        MOD = self.MOD
        return ((self.h[r] - self.h[l]*pow(self.base, r-l, MOD) + MOD)) % MOD
base = 3
g = gcd(len(s), len(t))
s = s * ((len(t) + len(s) - 1)//len(s))
MOD = 1004535809
rh0 = RollingHash(s, base, MOD)
rh1 = RollingHash(t, base, MOD)
N = len(s)
M = len(t)
B = rh1.get(0, M)
R = [0]*N
r = 0
for i in range(N-M+1):
    if rh0.get(i, i+M) == B:
        R[i] = r = 1
for i in range(N-M+1, N):
    if (rh0.get(i, N)*pow(base, M-(N-i), MOD) + rh0.get(0, M-(N-i))) % MOD == B:
        R[i] = r = 1
if not r:
    print(0)
    exit(0)
D = [0]*N
que = deque()
for i in range(N):
    if R[i] and R[(i+M)%N] == 0:
        que.append(i)
        D[i] = 1
if not que:
    print(-1)
    exit(0)
while que:
    v = que.popleft()
    if R[v-M]:
        que.append((v-M)% N)
        D[v-M] = D[v] + 1
print(max(D))