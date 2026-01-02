def gcd(x, y):
    if y == 0:
        return x
    while y != 0:
        x, y = y, x % y
    return x
class segment_gcd():
    def __init__(self,A,n,num):
        #####単位元######
        self.ide_ele = 0
        self.seg = [self.ide_ele] * 2 * num
        self.num = num
        # set_val
        for i in range(n):
            self.seg[i +num -1] = A[i]
            # built
        for i in range(num - 2, -1, -1):
            self.seg[i] = gcd(self.seg[2*i +1], self.seg[2*i +2])

    def update(self,k, x):
        k += num - 1
        self.seg[k] = x
        while k:
            k = (k - 1)//2
            self.seg[k] = gcd(self.seg[k*2 +1], self.seg[k*2 +2])

    def query(self,p, q):
        num = self.num; ide_ele = self.ide_ele
        if q <= p:
            return self.ide_ele
        p += num - 1
        q += num - 2
        res = ide_ele
        while q - p > 1:
            if p & 1 == 0:
                res = gcd(res, self.seg[p])
            if q & 1 == 1:
                res = gcd(res, self.seg[q])
                q -= 1
            p = p // 2
            q = (q - 1) // 2
        if p == q:
            res = gcd(res, self.seg[p])
        else:
            res = gcd(gcd(res, self.seg[p]), self.seg[q])
        return res

def examC():
    N = I()
    A = LI()
    # num:n以上の最小の2のべき乗
    num = 2 ** (N - 1).bit_length()
    Seggcd = segment_gcd(A,N,num)
    ans = -1
    for i in range(N):
        ans = max(ans, gcd(Seggcd.query(0, i), Seggcd.query(i + 1, N)))
    print(ans)


import sys,copy,bisect,itertools,heapq,math
from heapq import heappop,heappush,heapify
from collections import Counter,defaultdict,deque
def I(): return int(sys.stdin.readline())
def LI(): return list(map(int,sys.stdin.readline().split()))
def LSI(): return list(map(str,sys.stdin.readline().split()))
def LS(): return sys.stdin.readline().split()
def S(): return sys.stdin.readline().strip()
mod = 10**9 + 7
inf = float('inf')

examC()
