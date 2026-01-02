import sys
input = lambda: sys.stdin.buffer.readline()

L = 26
D = int(input())
C = list(map(int, input().split()))
S = [list(map(int, input().split())) for _ in range(D)]

T = [int(input()) for _ in range(D)]

M = int(input())

class BinaryIndexedTree:
    def __init__(self, n):
        self.n = n
        self.data = [0] * (self.n+1)
    
    def sum(self, i):
        res = 0
        while i > 0:
            res += self.data[i]
            i -= i & -i
        return res
    
    def add(self, i, x):
        if i <= 0: raise IndexError
        while i <= self.n:
            self.data[i] += x
            i += i & -i
    
    def lower_bound(self, x):
        if x <= 0: return 0
        cur, s, k = 0, 0, 1 << (self.n.bit_length()-1)
        while k:
            nxt = cur + k 
            if nxt <= self.n and s + self.data[nxt] < x:
                s += self.data[nxt]
                cur = nxt
            k >>= 1
        return cur + 1

def rsum(x):
    return x*(x+1)//2

b = [BinaryIndexedTree(D) for _ in range(L)]

score = 0
for d, cont in enumerate(T):
    cont -= 1
    b[cont].add(d+1, 1)
    score += S[d][cont]

for i in range(L):
    m = b[i].sum(D)
    tmp = 0
    s = [0]
    for j in range(1, m+1):
        s.append(b[i].lower_bound(j))
    s.append(D+1)

    for j in range(len(s)-1):
        x = s[j+1] - s[j] - 1
        tmp += rsum(x)
    
    score -= tmp*C[i]


def chg(d, q):
    diff = 0
    p = T[d]-1
    d += 1

    o = b[p].sum(d)
    d1 = b[p].lower_bound(o-1)
    d2 = b[p].lower_bound(o+1)

    diff += rsum(d-d1) * C[p]
    diff += rsum(d2-d) * C[p]
    diff -= rsum(d2-d1) * C[p]

    o = b[q].sum(d)
    d1 = b[q].lower_bound(o)
    d2 = b[q].lower_bound(o+1)

    diff += rsum(d2-d1) * C[q]
    diff -= rsum(d-d1) * C[q]
    diff -= rsum(d2-d) * C[q]

    b[p].add(d, -1)
    b[q].add(d, 1)

    d -= 1
    T[d] = q+1
    diff -= S[d][p]
    diff += S[d][q] 

    return diff

for _ in range(M):
    d, q = map(lambda x: int(x)-1, input().split())
    diff = chg(d, q)
    score += diff
    print(score)
