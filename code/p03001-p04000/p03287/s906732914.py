n, m = map(int, input().split())
a = list(map(int , input().split()))

class Cumulative_Sum:
    def __init__(self, a):
        la = len(a)
        self.s = [0] * (la + 1)
        for i in range(la):
            self.s[i+1] = self.s[i] + a[i]
    # s[l]からs[r]までの和
    def sum(self, l, r):
        return self.s[r] - self.s[l]

def nCr(n, r, mod=67280421310721):
    r = min(r, n-r)
    numer = denom = 1
    for i in range(1, r+1):
        numer = numer * (n+1-i) % mod
        denom = denom * i % mod
    return numer * pow(denom, mod-2, mod) % mod


cs = Cumulative_Sum(a)
from collections import defaultdict
b = defaultdict(int)

for i in range(n+1):
    b[cs.s[i] % m] += 1
#print(cs.s)
#print(b)
ans = 0
for bi in b:
    if b[bi] > 1:
        ans += nCr(b[bi], 2)
        #print(bi, b[bi])
    #    ans += b[bi]
print(ans)

"""
for i in range(n+1):
    if cs.s[i] % m == 0:
        ans += 1
    print(cs.s[i] % m)
print(ans)
"""
"""
print('---')
ans = 0
for i in range(n):
    for j in range(i+1, n+1):
        if cs.sum(i, j) % m == 0:
            print(i, j, cs.s[i]%m, cs.s[j]%m)
            #ans += 1
#print(ans)
"""