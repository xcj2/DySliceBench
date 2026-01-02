import sys
import math
from collections import defaultdict

sys.setrecursionlimit(10**7)
def input():
    return sys.stdin.readline()[:-1]

mod = 10**9 + 7

def I(): return int(input())
def II(): return map(int, input().split())
def III(): return list(map(int, input().split()))
def Line(N,num):
    if N<=0:
        return [[]]*num
    elif num==1:
        return [I() for _ in range(N)]
    else:
        read_all = [tuple(II()) for _ in range(N)]
        return map(list, zip(*read_all))

#################

from bisect import bisect_left

#Binary Indexed Tree（区間加算）
#1-indexed
class Range_BIT():
    def __init__(self, N):
        self.size = N
        self.data0 = [0]*(N+1)
        self.data1 = [0]*(N+1)

    def _add(self, data, k, x):
        while k <= self.size:
            data[k] += x
            k += k & -k

    # 区間[l,r)にxを加算
    def add(self, l, r, x):
        self._add(self.data0, l, -x*(l-1))
        self._add(self.data0, r, x*(r-1))
        self._add(self.data1, l, x)
        self._add(self.data1, r, -x)

    def _get(self, data, k):
        s = 0
        while k:
            s += data[k]
            k -= k & -k
        return s

    # 区間[l,r)の和を求める
    def query(self, l, r):
        return self._get(self.data1, r-1)*(r-1)+self._get(self.data0, r-1)\
                -self._get(self.data1, l-1)*(l-1)-self._get(self.data0, l-1)

N,M = II()
A = III()
A.sort()

def is_ok(x):
    num = 0
    for a in A:
        p = bisect_left(A,x-a)
        num += N-p
    if num>=M:
        return True
    else:
        return False

#l：その値以上の幸福度の握手がM通り以上ある最大値
l = 0
r = 2*10**5 + 1
while abs(r-l)>1:
    mid = (l+r)//2
    if is_ok(mid):
        l = mid
    else:
        r = mid

#値l以上の握手で用いるA[i]の個数を調べる
bit = Range_BIT(N)
for i in range(1,N+1):
    p = bisect_left(A,l-A[i-1])
    if p!=N:
        bit.add(p+1,N+1,1)
        bit.add(i,i+1,N-p)
x = [0]*N
for i in range(N):
    x[i] = bit.query(i+1,i+2)

ans = 0
for i in range(N):
    ans += A[i]*x[i]

#握手の回数がM回になるように調整
ans -= l*((sum(x)-2*M)//2)

print(ans)