import sys
readline = sys.stdin.readline

class BIT:
    #1-indexed
    def __init__(self, n):
        self.size = n
        self.tree = [0] * (n + 1)
        self.p = 2**(n.bit_length() - 1)
        self.dep = n.bit_length()
    def get(self, i):
        s = 0
        while i > 0:
            s += self.tree[i]
            i -= i & -i
        return s
 
    def add(self, i, x):
        while i <= self.size:
            self.tree[i] += x
            i += i & -i
    
    def bl(self, v):
        if v <= 0:
            return -1
        s = 0
        k = self.p
        for _ in range(self.dep):
            if s + k <= self.size and self.tree[s+k] < v:
                s += k
                v -= self.tree[s+k]
            k //= 2
        return s + 1

def compress(L):
    L2 = list(set(L))
    L2.sort()
    C = {v : k for k, v in enumerate(L2)}
    return L2, C


MOD = 998244353
N = int(readline())
XY = [list(map(int, readline().split())) for _ in range(N)]
XY.sort()

Z = [-10**10]
for x, y in XY:
    Z.append(y)

_, CC = compress(Z)
XY = [(x, CC[y]) for x, y in XY] 

SS, SB, BS, BB = [None]*N, [None]*N, [None]*N, [None]*N

T = BIT(N)
for i in range(N):
    k = i
    y = XY[i][1]
    l = T.get(y)
    SS[i] = l
    SB[i] = k-l
    T.add(y, 1)
T = BIT(N)
for i in range(N-1, -1, -1):
    k = N-1-i
    y = XY[i][1]
    l = T.get(y)
    BS[i] = l
    BB[i] = k-l
    T.add(y, 1)

P2 = [1]*1341398
for i in range(1, len(P2)):
    P2[i] = P2[i-1]*2%MOD

ans = 0
for i in range(N):
    ss = SS[i]
    sb = SB[i]
    bs = BS[i]
    bb = BB[i]
    ans = (ans + P2[N-1])%MOD
    ans = (ans + P2[N-1-ss-bb]*(P2[ss]-1)*(P2[bb]-1))%MOD
    ans = (ans + P2[N-1-sb-bs]*(P2[sb]-1)*(P2[bs]-1))%MOD
    ans = (ans - (P2[sb]-1)*(P2[bs]-1)*(P2[ss]-1)*(P2[bb]-1))%MOD
    
print(ans)
    