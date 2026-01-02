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

N = int(readline())
A = list(map(int, readline().split()))
A2, C = compress(A)
A = [C[a] for a in A]
ok = 0
ng = max(A)+1
T = BIT(ng)
ma = min(A)+1
while abs(ok-ng) > 1:
    med = (ok+ng)//2
    B = [1 if a >= med else -1 for a in A]
    for i in range(1, N):
        B[i] += B[i-1]
    
    
    mb = -min(0, min(B))+1
    T = BIT(max(B)+mb)
    T.add(mb, 1)
    res = 0
    for b in B:
        res += T.get(mb+b)
        T.add(mb+b, 1)
    if res >= N*(N+1)//4:
        ok = med
    else:
        ng = med
print(A2[ok])