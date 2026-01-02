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
        return [[] for _ in range(num)]
    elif num==1:
        return [I() for _ in range(N)]
    else:
        read_all = [tuple(II()) for _ in range(N)]
        return map(list, zip(*read_all))

#################

def solve():
    from bisect import bisect_right

    N,D,A = II()
    X,H = Line(N,2)
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

    #インデックス付きソート
    #(index,value)の順に格納
    from operator import itemgetter
    def index_sort(A):
        return sorted(enumerate(A),key=itemgetter(1))

    num = [math.ceil(H[i]/A) for i in range(N)]
    temp = index_sort(X)

    X2 = [temp[i][1] for i in range(N)]
    num = [num[t[0]] for t in temp]

    bit = Range_BIT(N)
    for i in range(1,N+1):
        bit.add(i,i+1,num[i-1])

    ans = 0
    for i in range(1,N+1):
        c = bit.query(i,i+1)
        if c<=0:
            continue
        p = bisect_right(X2,X2[i-1]+2*D)
        bit.add(i,p+1,-c)
        ans += c

    print(ans)

solve()