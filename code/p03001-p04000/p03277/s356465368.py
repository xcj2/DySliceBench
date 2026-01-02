class Fenwick:
    def __init__(self, size):
        self.arr = [0]*size
    
    def update(self, i, val):
        while i < len(self.arr): self.arr[i] += val; i |= i+1
    
    def getsum(self, i):
        res = 0
        while i >= 0: res+= self.arr[i]; i = (i&(i+1))-1
        return res

def paramin(F, l, r):
    while l <= r:
        mid = (l+r)//2
        if F(mid): ans, r = mid, mid-1
        else: l = mid+1
    return ans

from itertools import accumulate
def medleq(i):
    x = vals[i]
    M = [(y<=x)*2-1 for y in L]
    MA = list(accumulate(M))
    cnt = sum(y>0 for y in MA)
    F = Fenwick(2*n+3)
    for y in MA:
        c = y+n+1
        cnt+= F.getsum(c-1)
        F.update(c, 1)
    return cnt >= target

n = int(input())
L = list(map(int,input().split()))
tot = n + n*(n-1)//2
target = tot//2 + 1
vals = sorted(set(L))
print(vals[paramin(medleq, 0, len(vals)-1)])