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
        for _ in range(num): return []
    elif num==1:
        return [I() for _ in range(N)]
    else:
        read_all = [tuple(II()) for _ in range(N)]
        return map(list,zip(*read_all))

#################

from operator import itemgetter
from bisect import bisect_left

class Range_SegmentTree:
    def __init__(self,N):
        self.N0 = 2**(N-1).bit_length()
        self.tree = [None]*(2*self.N0)    
        self.INF = (-1, 2**31-1)

    #区間[l,r]の値をvに書き換える
    #vは(t,value)という値にする (新しい値ほどtは大きくなる)
    def update(self,l,r,v):
        L = l + self.N0; R = r + self.N0 + 1
        while L < R:
            if R & 1:
                R -= 1
                self.tree[R-1] = v
            if L & 1:
                self.tree[L-1] = v
                L += 1
            L >>= 1; R >>= 1

    #a[k]の現在の値を更新時刻と共に取得
    def _query(self,k):
        k += self.N0-1
        s = self.INF
        while k >= 0:
            if self.tree[k]:
                s = max(s, self.tree[k])
            k = (k - 1) // 2
        return s

    #a[k]を返す
    def query(self,k):
        return self._query(k)[1]
      
N,Q = II()
a = []
for _ in range(N):
    s,t,x = II()
    a.append((x, s-x-0.5, t-x-0.5))
D = Line(Q,1)
 
a.sort(key=itemgetter(0),reverse=True)
 
seg = Range_SegmentTree(Q)
for i,b in enumerate(a):
    l = bisect_left(D,b[1])
    r = bisect_left(D,b[2])
    seg.update(l,r-1,(i,b[0]))
    
for i in range(Q):
    x = seg.query(i)
    if x == 2**31-1:
        print(-1)
    else:
        print(x)