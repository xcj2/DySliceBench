import sys
import math
from collections import defaultdict
from bisect import bisect_left, bisect_right

sys.setrecursionlimit(10**7)
def input():
    return sys.stdin.readline()[:-1]

mod = 10**9 + 7

def I(): return int(input())
def LI(): return list(map(int, input().split()))
def LIR(row,col):
    if row <= 0:
        return [[] for _ in range(col)]
    elif col == 1:
        return [I() for _ in range(row)]
    else:
        read_all = [LI() for _ in range(row)]
        return map(list, zip(*read_all))

#################

# 全て-Kして，和が0以上かどうかを判定する
# 累積和の座圧→bitで出来る

from operator import itemgetter
def compress(A,reduction=True,start=0):
    if reduction:
        d = {}
        A_sort = sorted(list(set(A)))
        for i,a in enumerate(A_sort):
            d[a] = i+start
        return [d[a] for a in A]
    else:
        A_sort = sorted(enumerate(A),key=itemgetter(1,0))
        A_compress = [0]*len(A)
        for i,(j,_) in enumerate(A_sort):
            A_compress[j] = i+start
        return A_compress

class BIT:
    """
    a[1]~a[n]の数列を想定
    """

    def __init__(self,n):
        self.size = n
        self.tree = [0]*(n+1)
 
    def add(self,index,x):
        """
        a[index]にxを加算
        """
        while index <= self.size:
            self.tree[index] += x
            index += index & (-index)
 
    def sum(self,index):
        """
        a[1]~a[index]の和
        """
        s = 0
        while index:
            s += self.tree[index]
            index -= index & (-index)
        return s
 
    def search(self,value):
        """
        sum(index) >= value を満たす最小のindex
        sum(n) < value のとき n+1 を返す
        """
        i = 0
        s = 0
        step = 1 << (self.size.bit_length() - 1)
        while step:
            if i+step <= self.size and s + self.tree[i+step] < value:
                i += step
                s += self.tree[i]
            step >>= 1
        return i + 1


N,K = LI()
a = LIR(N,1)
a = list(map(lambda x: x-K, a))
ca = [0]
for i in range(N):
    ca.append(ca[-1]+a[i])

A = compress(ca,start=1)
bit = BIT(max(A))

ans = 0
for i in range(N+1):
    ans += bit.sum(A[i])
    bit.add(A[i],1)

print(ans)